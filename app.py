import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from werkzeug.security import generate_password_hash, check_password_hash
import requests

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# ==========================================
# MongoDB Connection & Mock DB Fallback Setup
# ==========================================
USE_MOCK_DB = False
db = None

try:
    # 3-second timeout so it doesn't block startup if local MongoDB is stopped
    client = MongoClient(app.config['MONGO_URI'], serverSelectionTimeoutMS=3000)
    # Trigger connection check
    client.server_info()
    db = client.get_default_database()
    print("Database connected successfully to MongoDB.")
except (ServerSelectionTimeoutError, Exception) as e:
    print(f"Warning: Failed to connect to MongoDB: {e}")
    print("Switching automatically to IN-MEMORY MOCK DATABASE for presentation safety!")
    USE_MOCK_DB = True

# Simulated Mock database collections
mock_db = {
    "users": [],
    "shops": [],
    "safety_reports": []
}

# Pre-populate some listed partner shops in the mock DB for demo demonstration
def seed_mock_data():
    if len(mock_db["shops"]) == 0:
        # Shop 1 (New Delhi Premium Restaurant)
        mock_db["shops"].append({
            "_id": "mock_shop_1",
            "owner_id": "mock_owner_1",
            "name": "The Royal Spice Kitchen",
            "email": "royal@spice.com",
            "category": "Restaurant",
            "address": "Connaught Place, Radial Road 3, New Delhi",
            "landmarks": "Opposite Rajiv Chowk Metro Gate No 4",
            "ways_to_reach": "Step out of metro Gate 4, walk 50m straight towards block B.",
            "latitude": 28.6304,
            "longitude": 77.2177,
            "subscription_plan": "premium",
            "fancy_description": "Award-winning traditional Awadhi and Mughlai cuisines curated by master chefs.",
            "deals": [
                {
                    "title": "Flat 20% OFF",
                    "description": "Get 20% off on all non-alcoholic bills above ₹999."
                }
            ]
        })
        # Shop 2 (New Delhi Basic Souvenir Shop)
        mock_db["shops"].append({
            "_id": "mock_shop_2",
            "owner_id": "mock_owner_2",
            "name": "Delhi Heritage Souvenirs",
            "email": "contact@delhiheritage.com",
            "category": "Souvenir",
            "address": "Janpath Market, Stall 42, New Delhi",
            "landmarks": "Adjacent to the main police assistance kiosk",
            "ways_to_reach": "Take Janpath road, walk inside market lane, first left stall.",
            "latitude": 28.6270,
            "longitude": 77.2198,
            "subscription_plan": "basic",
            "fancy_description": "Authentic handicrafts and marble miniatures.",
            "deals": [
                {
                    "title": "Free Keychain",
                    "description": "Get a free hand-crafted heritage keychain on purchases above ₹300."
                }
            ]
        })
        # Shop 3 (Goa Premium Beach Shack)
        mock_db["shops"].append({
            "_id": "mock_shop_3",
            "owner_id": "mock_owner_3",
            "name": "Sunset Seafood Grill",
            "email": "grill@sunsetgoa.com",
            "category": "Restaurant",
            "address": "Baga Beach Road, Goa",
            "landmarks": "Next to the water sports booking counter",
            "ways_to_reach": "Take local cab to Baga Beach parking, walk 200m towards beach front.",
            "latitude": 15.5535,
            "longitude": 73.7530,
            "subscription_plan": "premium",
            "fancy_description": "Catch your own fish and let our Goan chefs barbecue it live by the sunset.",
            "deals": [
                {
                    "title": "Buy 1 Get 1 Cocktail",
                    "description": "Order any mocktail or cocktail and get another free between 4 PM to 7 PM."
                }
            ]
        })

# ==========================================
# Real Weather & News Integration Helpers
# ==========================================
def get_live_weather(lat, lon, travel_date):
    """
    Fetches real-time weather from Open-Meteo API.
    Only called if travel_date is within a 14-day window.
    """
    try:
        dt_obj = datetime.strptime(travel_date, '%Y-%m-%d')
        today = datetime.utcnow().date()
        days_diff = (dt_obj.date() - today).days
        
        # Open-Meteo offers up to 16 days of daily forecast
        if 0 <= days_diff <= 14:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,weathercode&forecast_days=16&timezone=auto"
            response = requests.get(url, timeout=3).json()
            
            daily = response.get('daily', {})
            dates = daily.get('time', [])
            
            if travel_date in dates:
                idx = dates.index(travel_date)
                temp_max = daily.get('temperature_2m_max', [])[idx]
                temp_min = daily.get('temperature_2m_min', [])[idx]
                wcode = daily.get('weathercode', [])[idx]
                
                # WMO Weather Code to Condition & Icon map
                condition_map = {
                    0: ('Clear Sky', 'fa-sun', 'Excellent weather. Enjoy outdoor sightseeing, wear sunscreen, and stay hydrated.'),
                    1: ('Partly Cloudy', 'fa-cloud-sun', 'Good weather for travel. Occasional clouds, pleasant visibility.'),
                    2: ('Partly Cloudy', 'fa-cloud-sun', 'Good weather for travel. Occasional clouds, pleasant visibility.'),
                    3: ('Overcast', 'fa-cloud', 'Overcast skies. Pleasant temperatures for walking, but carry a light layer.'),
                    45: ('Foggy', 'fa-smog', 'Foggy conditions. Driving visibility might be reduced in morning hours.'),
                    48: ('Foggy', 'fa-smog', 'Foggy conditions. Driving visibility might be reduced in morning hours.'),
                    51: ('Light Drizzle', 'fa-cloud-rain', 'Light drizzle expected. Carry an umbrella or rain poncho.'),
                    53: ('Light Drizzle', 'fa-cloud-rain', 'Light drizzle expected. Carry an umbrella or rain poncho.'),
                    55: ('Light Drizzle', 'fa-cloud-rain', 'Light drizzle expected. Carry an umbrella or rain poncho.'),
                    61: ('Rain Showers', 'fa-cloud-showers-heavy', 'Rain expected. High chance of waterlogging in low-lying roads. Carry rain gear.'),
                    63: ('Heavy Rain', 'fa-cloud-showers-heavy', 'Heavy rain expected. High chance of waterlogging in low-lying roads. Carry rain gear.'),
                    65: ('Heavy Torrential Rain', 'fa-cloud-showers-heavy', 'Heavy torrential rain forecast. Avoid mountain hikes or beach fronts. Expect travel delays.'),
                    80: ('Rain Showers', 'fa-cloud-showers-heavy', 'Passing rain showers. Keep an umbrella handy.'),
                    81: ('Rain Showers', 'fa-cloud-showers-heavy', 'Passing rain showers. Keep an umbrella handy.'),
                    82: ('Violent Rain Showers', 'fa-cloud-showers-heavy', 'Violent rain showers. Avoid long travel on national highways.'),
                    95: ('Thunderstorm', 'fa-cloud-bolt', 'Thunderstorms forecast. Stay indoors during lightning strikes.'),
                    96: ('Thunderstorm', 'fa-cloud-bolt', 'Thunderstorms forecast. Stay indoors during lightning strikes.'),
                    99: ('Thunderstorm with Hail', 'fa-cloud-bolt', 'Severe thunderstorms. Stay indoors, expect transport disruptions.')
                }
                
                cond_text, icon, advisory = condition_map.get(wcode, ('Variable Conditions', 'fa-cloud-sun', 'Variable weather. Check local reports before starting.'))
                avg_temp = round((temp_max + temp_min) / 2)
                
                return {
                    'temp': avg_temp,
                    'condition': f"{cond_text} ({temp_min}°C - {temp_max}°C)",
                    'icon_class': icon,
                    'advisory': advisory,
                    'is_historical': False
                }
    except Exception as e:
        print(f"Weather API fetch failed: {e}")
    return None

def get_live_news(search_location):
    """
    Attempts to fetch real-time news from GNews API using an environment key.
    Falls back to pre-seeded local safety advisory feeds if no key or error.
    """
    news_api_key = os.getenv('NEWS_API_KEY')
    if not news_api_key:
        return None
        
    try:
        # Search for location-specific safety, weather, or travel news
        query = f'"{search_location}" AND (weather OR rain OR flood OR warning OR safety)'
        url = f"https://gnews.io/api/v4/search?q={query}&lang=en&country=in&max=3&apikey={news_api_key}"
        response = requests.get(url, timeout=3).json()
        
        articles = response.get('articles', [])
        if articles:
            news_results = []
            for art in articles:
                news_results.append({
                    'title': art.get('title', 'Local Update'),
                    'content': art.get('description', 'Read full article on source website.'),
                    'severity': 'General Alert',
                    'source': art.get('source', {}).get('name', 'GNews API')
                })
            return news_results
    except Exception as e:
        print(f"News API fetch failed: {e}")
    return None

seed_mock_data()

# Database Helper Functions
def db_find_one(collection, query):
    if USE_MOCK_DB:
        for doc in mock_db[collection]:
            match = True
            for k, v in query.items():
                if doc.get(k) != v:
                    match = False
                    break
            if match:
                return doc
        return None
    else:
        return db[collection].find_one(query)

def db_find(collection, query):
    if USE_MOCK_DB:
        results = []
        for doc in mock_db[collection]:
            match = True
            for k, v in query.items():
                if doc.get(k) != v:
                    match = False
                    break
            if match:
                results.append(doc)
        return results
    else:
        return list(db[collection].find(query))

def db_insert_one(collection, doc):
    if USE_MOCK_DB:
        doc["_id"] = f"mock_{collection}_{len(mock_db[collection]) + 1}"
        mock_db[collection].append(doc)
        return doc
    else:
        result = db[collection].insert_one(doc)
        doc["_id"] = result.inserted_id
        return doc

def db_update_one(collection, query, new_values):
    if USE_MOCK_DB:
        doc = db_find_one(collection, query)
        if doc:
            for k, v in new_values.items():
                doc[k] = v
            return True
        return False
    else:
        db[collection].update_one(query, {"$set": new_values})
        return True


# ==========================================
# Authentication & Role Gateways
# ==========================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    role_hint = request.args.get('role_hint', 'tourist')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = db_find_one('users', {'email': email})
        
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = str(user['_id'])
            session['email'] = user['email']
            session['role'] = user['role']
            session['name'] = user['name']
            
            flash(f"Welcome back, {user['name']}!", "success")
            
            if user['role'] == 'tourist':
                return redirect(url_for('tourist_dashboard'))
            else:
                return redirect(url_for('shop_dashboard'))
        else:
            flash("Invalid email or password. Please try again.", "danger")
            
    return render_template('login.html', role_hint=role_hint)

@app.route('/register', methods=['GET', 'POST'])
def register():
    role_hint = request.args.get('role_hint', 'tourist')
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'tourist')
        
        # Check if user already exists
        existing_user = db_find_one('users', {'email': email})
        if existing_user:
            flash("Email already registered. Try logging in.", "danger")
            return redirect(url_for('login'))
        
        hashed_password = generate_password_hash(password)
        
        user_doc = {
            'name': name,
            'email': email,
            'password_hash': hashed_password,
            'role': role,
            'created_at': datetime.utcnow()
        }
        
        user = db_insert_one('users', user_doc)
        
        # If user is a shop owner, set up their business details
        if role == 'shop_owner':
            shop_name = request.form.get('shop_name', f"{name}'s Shop")
            category = request.form.get('category', 'Restaurant')
            plan = request.form.get('subscription_plan', 'basic')
            
            shop_doc = {
                'owner_id': str(user['_id']),
                'name': shop_name,
                'email': email,
                'category': category,
                'address': '',
                'landmarks': '',
                'ways_to_reach': '',
                'latitude': 28.6139,  # Default center coordinates (Delhi)
                'longitude': 77.2090,
                'subscription_plan': plan,
                'fancy_description': '',
                'deals': []
            }
            db_insert_one('shops', shop_doc)
            
        session['user_id'] = str(user['_id'])
        session['email'] = user['email']
        session['role'] = user['role']
        session['name'] = user['name']
        
        flash("Registration successful!", "success")
        
        if role == 'tourist':
            return redirect(url_for('tourist_dashboard'))
        else:
            return redirect(url_for('shop_dashboard'))
            
    return render_template('register.html', role_hint=role_hint)

@app.route('/logout')
def logout():
    session.clear()
    flash("You have successfully logged out.", "success")
    return redirect(url_for('index'))

@app.route('/google-login', methods=['GET', 'POST'])
def google_login():
    """
    Simulates Google OAuth2 single-sign-on (SSO).
    On GET: Renders a mock Google Account Selector.
    On POST: Authenticates/Registers the selected identity.
    """
    role_hint = request.args.get('role_hint', 'tourist')
    
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        role = request.form.get('role', 'tourist')
        
        # Try finding the user by email
        user = db_find_one('users', {'email': email})
        
        if not user:
            # Create Google account
            google_id = f"google_{email.split('@')[0]}"
            user_doc = {
                'name': name,
                'email': email,
                'password_hash': generate_password_hash("google_sso_pass_secure"),
                'google_id': google_id,
                'role': role,
                'created_at': datetime.utcnow()
            }
            user = db_insert_one('users', user_doc)
            
            # If user is a shop owner, set up their business details
            if role == 'shop_owner':
                shop_doc = {
                    'owner_id': str(user['_id']),
                    'name': f"{name}'s Shop",
                    'email': email,
                    'category': 'Restaurant',
                    'address': '',
                    'landmarks': '',
                    'ways_to_reach': '',
                    'latitude': 28.6139,  # Default center coordinates (Delhi)
                    'longitude': 77.2090,
                    'subscription_plan': 'basic',
                    'fancy_description': '',
                    'deals': []
                }
                db_insert_one('shops', shop_doc)
        
        session['user_id'] = str(user['_id'])
        session['email'] = user['email']
        session['role'] = user['role']
        session['name'] = user['name']
        
        flash(f"Signed in successfully as {name} via Google!", "success")
        
        if user['role'] == 'tourist':
            return redirect(url_for('tourist_dashboard'))
        else:
            return redirect(url_for('shop_dashboard'))
            
    return render_template('google_login.html', role_hint=role_hint)


# ==========================================
# Tourist Hub & Planner Logic
# ==========================================
@app.route('/tourist-dashboard')
def tourist_dashboard():
    if not session.get('user_id') or session.get('role') != 'tourist':
        flash("Please login as a Tourist first.", "danger")
        return redirect(url_for('login', role_hint='tourist'))
        
    search_location = request.args.get('location', '')
    travel_date = request.args.get('travel_date', '')
    
    # Preloaded maps configurations
    map_center = [28.6139, 77.2090] # default Delhi
    unlisted_shops = []
    sightseeing_spots = []
    listed_shops = []
    
    weather = {
        'temp': 32,
        'condition': 'Clear Sunny',
        'icon_class': 'fa-sun',
        'advisory': 'Perfect weather for traveling. Carry water, light clothing, and sun protection.'
    }
    
    news = [
        {
            'title': 'Monsoon Tourism Advisory Issued',
            'content': 'Local tourism board advises caution near waterfronts during high tides.',
            'severity': 'Warning',
            'source': 'State Emergency Desk'
        },
        {
            'title': 'Traffic Flow Smooth on High-Speed Corridor',
            'content': 'No traffic blockages reported in tourist central regions.',
            'severity': 'General Alert',
            'source': 'Traffic Control'
        }
    ]
    
    if search_location:
        loc_normalized = search_location.lower().strip()
        
        # 1. Coordinate lookup and Mock database mapping depending on city
        if 'delhi' in loc_normalized:
            map_center = [28.6139, 77.2090]
            
            # Fetch listed shops for Delhi
            listed_shops = db_find('shops', {})
            # Filter shops to make it look geographic
            listed_shops = [s for s in listed_shops if s.get('latitude', 0) > 28.5 and s.get('latitude', 0) < 28.7]
            
            # Famous Unlisted Restaurants
            unlisted_shops = [
                {
                    'name': "Karim's Historic Diner",
                    'category': 'Restaurant',
                    'rating': 4.6,
                    'address': 'Gali Kababian, Old Delhi',
                    'source': 'TripAdvisor Rating',
                    'latitude': 28.6500,
                    'longitude': 77.2330
                },
                {
                    'name': 'Indian Accent Fine Dine',
                    'category': 'Restaurant',
                    'rating': 4.8,
                    'address': 'The Lodhi Hotel, New Delhi',
                    'source': 'Google Reviews (12k+ votes)',
                    'latitude': 28.5912,
                    'longitude': 77.2290
                }
            ]
            # Sightseeing attractions
            sightseeing_spots = [
                {
                    'name': 'India Gate Heritage Arch',
                    'description': 'A prominent historical war memorial built in honors of soldiers.',
                    'ticket_price': 'Free Entry',
                    'latitude': 28.6129,
                    'longitude': 77.2295
                },
                {
                    'name': 'Qutub Minar Complex',
                    'description': 'Ancient Victory Tower standing 73 meters tall.',
                    'ticket_price': '₹40 (Indians), ₹600 (Foreigners)',
                    'latitude': 28.5244,
                    'longitude': 77.1855
                }
            ]
        elif 'goa' in loc_normalized:
            map_center = [15.4909, 73.8278]
            
            # Fetch Goa shops
            listed_shops = db_find('shops', {})
            listed_shops = [s for s in listed_shops if s.get('latitude', 0) > 15.0 and s.get('latitude', 0) < 15.7]
            
            unlisted_shops = [
                {
                    'name': "The Fisherman's Wharf",
                    'category': 'Restaurant',
                    'rating': 4.5,
                    'address': 'Panaji Riverside Road',
                    'source': 'Zomato gold selection',
                    'latitude': 15.4989,
                    'longitude': 73.8378
                },
                {
                    'name': "Mum's Goan Kitchen",
                    'category': 'Restaurant',
                    'rating': 4.3,
                    'address': 'Panaji central',
                    'source': 'Google business reviews',
                    'latitude': 15.4889,
                    'longitude': 73.8178
                }
            ]
            sightseeing_spots = [
                {
                    'name': 'Aguada Fort Lighthouse',
                    'description': 'A historic 17th-century Portuguese fort standing on Sinquerim Beach.',
                    'ticket_price': 'Free Entry',
                    'latitude': 15.4925,
                    'longitude': 73.7738
                },
                {
                    'name': 'Baga Beach Watersports Hub',
                    'description': 'Busy sand coast famous for parasailing, motor boat rides, and lounges.',
                    'ticket_price': 'Free Entry (Activities cost extra)',
                    'latitude': 15.5528,
                    'longitude': 73.7517
                }
            ]
        else:
            # Fallback coordinate for any other city using string hashing to avoid blank maps!
            hash_val = sum(ord(c) for c in loc_normalized)
            map_center = [20.0 + (hash_val % 10), 75.0 + (hash_val % 10)]
            
            listed_shops = db_find('shops', {})
            # Mock some items nearby the dynamic hash map center
            for s in listed_shops:
                s['latitude'] = map_center[0] + 0.005
                s['longitude'] = map_center[1] - 0.003
                
            unlisted_shops = [
                {
                    'name': f'Famous {search_location} Hub',
                    'category': 'Restaurant',
                    'rating': 4.7,
                    'address': f'Main Bazar, {search_location}',
                    'source': 'Popular local recommendation',
                    'latitude': map_center[0] - 0.008,
                    'longitude': map_center[1] + 0.006
                }
            ]
            sightseeing_spots = [
                {
                    'name': f'{search_location} City Garden',
                    'description': 'Quiet public park containing fountains and flower layouts.',
                    'ticket_price': '₹20 per visitor',
                    'latitude': map_center[0] + 0.002,
                    'longitude': map_center[1] + 0.008
                }
            ]
            
        # 2. Real Weather Integration (Open-Meteo) & Climate Fallback
        if travel_date:
            # Attempt to fetch live weather forecast (if within 14 days)
            live_weather = get_live_weather(map_center[0], map_center[1], travel_date)
            
            if live_weather:
                weather = live_weather
            else:
                # Fallback to monthly climatology average (since date is > 14 days or API offline)
                try:
                    dt_obj = datetime.strptime(travel_date, '%Y-%m-%d')
                    month = dt_obj.month
                    if month in [6, 7, 8, 9]: # Monsoon
                        weather = {
                            'temp': 28,
                            'condition': 'Typical Monsoon Season',
                            'icon_class': 'fa-cloud-showers-heavy',
                            'advisory': 'Historically a wet monsoon period. Expect frequent rains. Carry an umbrella and water-resistant footwear.',
                            'is_historical': True
                        }
                    elif month in [11, 12, 1, 2]: # Winter
                        weather = {
                            'temp': 16,
                            'condition': 'Typical Cool Season',
                            'icon_class': 'fa-snowflake',
                            'advisory': 'Historically a winter period. Light woolens or jackets recommended for evenings.',
                            'is_historical': True
                        }
                    else: # Summer
                        weather = {
                            'temp': 36,
                            'condition': 'Typical Hot Season',
                            'icon_class': 'fa-sun',
                            'advisory': 'Historically a hot summer period. Dress in light cottons, carry sunscreen, and stay hydrated.',
                            'is_historical': True
                        }
                except ValueError:
                    pass
                    
        # 3. Real News Integration (GNews) & Fallbacks
        if search_location:
            live_news = get_live_news(search_location)
            if live_news:
                # Add real news to the top of the alerts feed
                news = live_news + news
                
    return render_template('tourist_dashboard.html',
                           search_location=search_location,
                           travel_date=travel_date,
                           map_center=map_center,
                           unlisted_shops=unlisted_shops,
                           sightseeing_spots=sightseeing_spots,
                           listed_shops=listed_shops,
                           weather=weather,
                           news=news)


# ==========================================
# Shop Owner Dashboard & Deal APIs
# ==========================================
@app.route('/shop-dashboard')
def shop_dashboard():
    if not session.get('user_id') or session.get('role') != 'shop_owner':
        flash("Please login as a Shop Owner first.", "danger")
        return redirect(url_for('login', role_hint='shop_owner'))
        
    user_id = session.get('user_id')
    shop = db_find_one('shops', {'owner_id': user_id})
    
    if not shop:
        # Fallback in case of registration error, create a default shop document
        shop_doc = {
            'owner_id': user_id,
            'name': f"{session.get('name')}'s Shop",
            'email': session.get('email'),
            'category': 'Restaurant',
            'address': '',
            'landmarks': '',
            'ways_to_reach': '',
            'latitude': 28.6139,
            'longitude': 77.2090,
            'subscription_plan': 'basic',
            'fancy_description': '',
            'deals': []
        }
        shop = db_insert_one('shops', shop_doc)
        
    return render_template('shop_dashboard.html', shop=shop)

@app.route('/update-shop', methods=['POST'])
def update_shop():
    if not session.get('user_id') or session.get('role') != 'shop_owner':
        return redirect(url_for('index'))
        
    user_id = session.get('user_id')
    
    # Extract values
    name = request.form.get('name')
    address = request.form.get('address')
    landmarks = request.form.get('landmarks')
    ways_to_reach = request.form.get('ways_to_reach')
    
    # Safeguard coordinate numbers parsing
    try:
        latitude = float(request.form.get('latitude', 0.0))
        longitude = float(request.form.get('longitude', 0.0))
    except ValueError:
        latitude = 28.6139
        longitude = 77.2090
        
    fancy_desc = request.form.get('fancy_description', '')
    
    new_values = {
        'name': name,
        'address': address,
        'landmarks': landmarks,
        'ways_to_reach': ways_to_reach,
        'latitude': latitude,
        'longitude': longitude,
        'fancy_description': fancy_desc
    }
    
    db_update_one('shops', {'owner_id': user_id}, new_values)
    flash("Shop details updated successfully!", "success")
    return redirect(url_for('shop_dashboard'))

@app.route('/upgrade-plan', methods=['POST'])
def upgrade_plan():
    if not session.get('user_id') or session.get('role') != 'shop_owner':
        return redirect(url_for('index'))
        
    user_id = session.get('user_id')
    db_update_one('shops', {'owner_id': user_id}, {'subscription_plan': 'premium'})
    
    flash("Success! Upgraded to Featured Promotion (₹150 Plan). You can now post fancy taglines!", "success")
    return redirect(url_for('shop_dashboard'))

@app.route('/add-deal', methods=['POST'])
def add_deal():
    if not session.get('user_id') or session.get('role') != 'shop_owner':
        return redirect(url_for('index'))
        
    user_id = session.get('user_id')
    title = request.form.get('title')
    description = request.form.get('description')
    
    shop = db_find_one('shops', {'owner_id': user_id})
    if shop:
        deals = shop.get('deals', [])
        deals.append({
            'title': title,
            'description': description
        })
        db_update_one('shops', {'owner_id': user_id}, {'deals': deals})
        flash("Coupon posted successfully!", "success")
        
    return redirect(url_for('shop_dashboard'))

@app.route('/delete-deal/<int:index>', methods=['POST'])
def delete_deal(index):
    if not session.get('user_id') or session.get('role') != 'shop_owner':
        return redirect(url_for('index'))
        
    user_id = session.get('user_id')
    shop = db_find_one('shops', {'owner_id': user_id})
    if shop:
        deals = shop.get('deals', [])
        if 0 <= index < len(deals):
            deals.pop(index)
            db_update_one('shops', {'owner_id': user_id}, {'deals': deals})
            flash("Coupon removed successfully.", "success")
            
    return redirect(url_for('shop_dashboard'))

# ==========================================
# Run application
# ==========================================
if __name__ == '__main__':
    # Bind to all network interfaces so friends/teachers on same WiFi can access it!
    app.run(host='0.0.0.0', debug=True, port=5000)
