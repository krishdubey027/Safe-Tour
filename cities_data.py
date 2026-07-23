# cities_data.py

CITIES = {
    'delhi': {
        'name': 'New Delhi',
        'state': 'Delhi',
        'tagline': 'The Heart of India',
        'description': 'A vibrant mix of old-world charm and modern dynamism, Delhi is a city of historical monuments, bustling markets, and diverse culinary experiences.',
        'coordinates': [28.6139, 77.2090],
        'best_season': 'October to March',
        'languages': ['Hindi', 'English', 'Punjabi'],
        'famous_food': [
            {'name': 'Chole Bhature', 'description': 'Fluffy fried bread served with spiced chickpeas.', 'where_to_eat': 'Sitaram Diwan Chand, Paharganj'}
        ],
        'instagram_spots': [
            {'name': 'India Gate at Sunset', 'tip': 'Golden hour at 6:30 PM for best shots'}
        ],
        'trip_cost': {
            'budget': {'per_day': 800, 'hotel': 400, 'food': 250, 'transport': 150},
            'standard': {'per_day': 2500, 'hotel': 1500, 'food': 700, 'transport': 300},
            'luxury': {'per_day': 8000, 'hotel': 5500, 'food': 1800, 'transport': 700}
        },
        'attractions': [
            {
                'id': 'india-gate', 'name': 'India Gate', 'category': 'Monument', 'tags': ['family', 'history', 'photography'],
                'description': 'An iconic war memorial located astride the Rajpath.', 'history': 'Built to commemorate 70,000 soldiers of the British Indian Army.',
                'why_famous': 'A symbol of sacrifice and a prominent landmark of New Delhi.', 'interesting_facts': ['Designed by Sir Edwin Lutyens', 'Amar Jawan Jyoti burns here'],
                'coordinates': [28.6129, 77.2295], 'address': 'Rajpath, India Gate, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 50, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'India Gate New Delhi',
                'tips': ['Visit at sunset', 'Avoid Republic Day'], 'nearby': ['National Museum'], 'reviews': []
            },
            {
                'id': 'red-fort', 'name': 'Red Fort', 'category': 'Monument', 'tags': ['history', 'photography'],
                'description': 'A historic fort in the city of Delhi that served as the main residence of the Mughal Emperors.', 'history': 'Constructed in 1639 by the fifth Mughal Emperor Shah Jahan.',
                'why_famous': 'Known for its massive enclosing walls of red sandstone.', 'interesting_facts': ['UNESCO World Heritage Site', 'Designated by Shah Jahan'],
                'coordinates': [28.6562, 77.2410], 'address': 'Netaji Subhash Marg, Chandni Chowk, New Delhi',
                'ticket': {'adult': 35, 'child': 35, 'foreign': 550, 'student': 35, 'camera': 0, 'parking': 50, 'is_free': False},
                'timings': {'open': '9:30 AM', 'close': '4:30 PM', 'weekly_off': 'Monday', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Red Fort',
                'tips': ['Buy tickets online to avoid lines'], 'nearby': ['Jama Masjid'], 'reviews': []
            },
            {
                'id': 'qutub-minar', 'name': 'Qutub Minar', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A towering 73-meter high minaret built by Qutb-ud-din Aibak.', 'history': 'Built in 1193 as a victory tower.',
                'why_famous': 'Highest tower in India.', 'interesting_facts': ['UNESCO World Heritage Site', 'Contains a famous iron pillar'],
                'coordinates': [28.5244, 77.1855], 'address': 'Mehrauli, New Delhi',
                'ticket': {'adult': 40, 'child': 0, 'foreign': 600, 'student': 40, 'camera': 0, 'parking': 50, 'is_free': False},
                'timings': {'open': '7:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1-2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Qutub Minar',
                'tips': ['Carry water'], 'nearby': ['Mehrauli Archaeological Park'], 'reviews': []
            },
            {
                'id': 'humayun-tomb', 'name': 'Humayun Tomb', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'The tomb of the Mughal Emperor Humayun in Delhi.', 'history': 'Commissioned by Humayun\'s first wife.',
                'why_famous': 'First garden-tomb on the Indian subcontinent.', 'interesting_facts': ['Inspired the Taj Mahal'],
                'coordinates': [28.5933, 77.2507], 'address': 'Mathura Road, New Delhi',
                'ticket': {'adult': 40, 'child': 0, 'foreign': 600, 'student': 40, 'camera': 0, 'parking': 50, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Afternoon', 'visit_duration': '1.5 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'Humayun Tomb',
                'tips': ['Great for photography'], 'nearby': ['Lodi Garden'], 'reviews': []
            },
            {
                'id': 'lotus-temple', 'name': 'Lotus Temple', 'category': 'Temple', 'tags': ['architecture', 'peace'],
                'description': 'A Bahá\'í House of Worship notable for its flowerlike shape.', 'history': 'Dedicated in December 1986.',
                'why_famous': 'Lotus-shaped structure.', 'interesting_facts': ['Open to all religions'],
                'coordinates': [28.5535, 77.2588], 'address': 'Lotus Temple Rd, Bahapur, Shambhu Dayal Bagh, Kalkaji, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '9:00 AM', 'close': '5:30 PM', 'weekly_off': 'Monday', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Lotus Temple',
                'tips': ['Keep silent inside'], 'nearby': ['ISKCON Temple'], 'reviews': []
            },
            {
                'id': 'akshardham', 'name': 'Akshardham', 'category': 'Temple', 'tags': ['culture', 'architecture'],
                'description': 'A spiritual-cultural campus in New Delhi.', 'history': 'Opened in 2005.',
                'why_famous': 'Intricate carvings and exhibitions.', 'interesting_facts': ['Largest Hindu temple in Delhi'],
                'coordinates': [28.6127, 77.2773], 'address': 'Noida Mor, Pandav Nagar, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:00 AM', 'close': '6:30 PM', 'weekly_off': 'Monday', 'best_time': 'Evening', 'visit_duration': '3-4 hours'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.8, 'photo_keyword': 'Akshardham Temple',
                'tips': ['Phones are not allowed inside'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'jama-masjid', 'name': 'Jama Masjid', 'category': 'Mosque', 'tags': ['religion', 'history'],
                'description': 'One of the largest mosques in India.', 'history': 'Built by Mughal Emperor Shah Jahan.',
                'why_famous': 'Grand architecture and scale.', 'interesting_facts': ['Can accommodate 25,000 worshippers'],
                'coordinates': [28.6507, 77.2334], 'address': 'Jama Masjid Rd, Chandni Chowk, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 300, 'parking': 0, 'is_free': True},
                'timings': {'open': '7:00 AM', 'close': '12:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Jama Masjid',
                'tips': ['Dress modestly'], 'nearby': ['Red Fort', 'Chandni Chowk'], 'reviews': []
            },
            {
                'id': 'lodi-garden', 'name': 'Lodi Garden', 'category': 'Park', 'tags': ['nature', 'history'],
                'description': 'A city park situated in New Delhi, containing Mohammed Shah\'s Tomb.', 'history': 'Protected by the Archaeological Survey of India.',
                'why_famous': 'Historical tombs in a lush park.', 'interesting_facts': ['Spread over 90 acres'],
                'coordinates': [28.5931, 77.2197], 'address': 'Lodhi Rd, Lodhi Gardens, Lodhi Estate, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '6:00 AM', 'close': '8:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1.5 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'Lodi Garden',
                'tips': ['Great for morning walks'], 'nearby': ['Safdarjung Tomb'], 'reviews': []
            },
            {
                'id': 'iskcon-temple', 'name': 'ISKCON Temple Delhi', 'category': 'Temple', 'tags': ['religion'],
                'description': 'A well known Vaishnav temple of Lord Krishna and Radharani.', 'history': 'Opened in 1998.',
                'why_famous': 'Spiritual programs and architecture.', 'interesting_facts': ['One of the largest temple complexes in India'],
                'coordinates': [28.5562, 77.2536], 'address': 'Hare Krishna Hill, East of Kailash, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '4:30 AM', 'close': '9:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'ISKCON Delhi',
                'tips': ['Attend the evening aarti'], 'nearby': ['Lotus Temple'], 'reviews': []
            },
            {
                'id': 'national-museum', 'name': 'National Museum', 'category': 'Museum', 'tags': ['history', 'culture'],
                'description': 'One of the largest museums in India.', 'history': 'Established in 1949.',
                'why_famous': 'Vast collection of artifacts.', 'interesting_facts': ['Holds over 200,000 works of art'],
                'coordinates': [28.6119, 77.2193], 'address': 'Janpath, New Delhi',
                'ticket': {'adult': 20, 'child': 0, 'foreign': 650, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '6:00 PM', 'weekly_off': 'Monday', 'best_time': 'Anytime', 'visit_duration': '2-3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Low', 'rating': 4.6, 'photo_keyword': 'National Museum Delhi',
                'tips': ['Free guided tours are available'], 'nearby': ['India Gate'], 'reviews': []
            },
            {
                'id': 'chandni-chowk', 'name': 'Chandni Chowk', 'category': 'Market', 'tags': ['shopping', 'food'],
                'description': 'One of the oldest and busiest markets in Old Delhi.', 'history': 'Built in the 17th century by Shah Jahan.',
                'why_famous': 'Street food and wholesale goods.', 'interesting_facts': ['Designed by Shah Jahan\'s daughter'],
                'coordinates': [28.6560, 77.2310], 'address': 'Chandni Chowk, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:00 AM', 'close': '8:00 PM', 'weekly_off': 'Sunday', 'best_time': 'Evening', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'Very High', 'rating': 4.3, 'photo_keyword': 'Chandni Chowk Street',
                'tips': ['Use metro as parking is difficult'], 'nearby': ['Jama Masjid'], 'reviews': []
            },
            {
                'id': 'connaught-place', 'name': 'Connaught Place', 'category': 'Market', 'tags': ['shopping', 'food'],
                'description': 'A major commercial and business centre.', 'history': 'Developed during British rule.',
                'why_famous': 'Georgian-style architecture.', 'interesting_facts': ['Named after the Duke of Connaught'],
                'coordinates': [28.6304, 77.2177], 'address': 'Connaught Place, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:00 AM', 'close': '11:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Connaught Place',
                'tips': ['Great for dining out'], 'nearby': ['Jantar Mantar Delhi'], 'reviews': []
            },
            {
                'id': 'hauz-khas-village', 'name': 'Hauz Khas Village', 'category': 'Neighborhood', 'tags': ['nightlife', 'history'],
                'description': 'An affluent neighborhood with historic ruins and modern cafes.', 'history': 'Dates back to the Delhi Sultanate.',
                'why_famous': 'Nightlife and boutiques.', 'interesting_facts': ['Contains a medieval reservoir'],
                'coordinates': [28.5555, 77.1950], 'address': 'Hauz Khas, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:00 AM', 'close': '12:00 AM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2-4 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Hauz Khas Village',
                'tips': ['Best to visit for dinner and drinks'], 'nearby': ['Deer Park'], 'reviews': []
            },
            {
                'id': 'dilli-haat', 'name': 'Dilli Haat', 'category': 'Market', 'tags': ['shopping', 'culture'],
                'description': 'An open-air food plaza and craft bazaar.', 'history': 'Established to promote Indian handicrafts.',
                'why_famous': 'Regional foods and crafts.', 'interesting_facts': ['Stalls are rotated every 15 days'],
                'coordinates': [28.5727, 77.2081], 'address': 'INA Market, Dilli Haat, Kidwai Nagar West, Kidwai Nagar, New Delhi',
                'ticket': {'adult': 30, 'child': 10, 'foreign': 100, 'student': 30, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:30 AM', 'close': '10:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Dilli Haat Crafts',
                'tips': ['Bargaining is common for crafts'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'rashtrapati-bhavan', 'name': 'Rashtrapati Bhavan', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'The official residence of the President of India.', 'history': 'Designed by Edwin Lutyens.',
                'why_famous': 'Largest residence of any head of state.', 'interesting_facts': ['Has 340 rooms'],
                'coordinates': [28.6143, 77.1994], 'address': 'Rashtrapati Bhawan, President\'s Estate, New Delhi',
                'ticket': {'adult': 50, 'child': 0, 'foreign': 50, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '4:00 PM', 'weekly_off': 'Monday, Tuesday, Wednesday', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'Rashtrapati Bhavan',
                'tips': ['Requires prior online booking'], 'nearby': ['India Gate'], 'reviews': []
            },
            {
                'id': 'purana-qila', 'name': 'Purana Qila', 'category': 'Monument', 'tags': ['history'],
                'description': 'One of the oldest forts in Delhi.', 'history': 'Built by Sher Shah Suri and Humayun.',
                'why_famous': 'Massive walls and gateways.', 'interesting_facts': ['Site of the ancient city of Indraprastha'],
                'coordinates': [28.6096, 77.2437], 'address': 'Mathura Rd, Near Delhi Zoo, New Delhi',
                'ticket': {'adult': 30, 'child': 0, 'foreign': 300, 'student': 30, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '7:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1.5 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Purana Qila',
                'tips': ['Enjoy the light and sound show in the evening'], 'nearby': ['National Zoological Park'], 'reviews': []
            },
            {
                'id': 'safdarjung-tomb', 'name': 'Safdarjung Tomb', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A sandstone and marble mausoleum built in 1754.', 'history': 'Tomb of Nawab Safdarjung.',
                'why_famous': 'Last monumental tomb garden of the Mughals.', 'interesting_facts': ['Designed by an Ethiopian architect'],
                'coordinates': [28.5893, 77.2106], 'address': 'Airforce Golf Course, Delhi Race Club, New Delhi',
                'ticket': {'adult': 25, 'child': 0, 'foreign': 300, 'student': 25, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '7:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Low', 'rating': 4.5, 'photo_keyword': 'Safdarjung Tomb',
                'tips': ['Less crowded alternative to Humayun\'s Tomb'], 'nearby': ['Lodi Garden'], 'reviews': []
            },
            {
                'id': 'jantar-mantar-delhi', 'name': 'Jantar Mantar Delhi', 'category': 'Monument', 'tags': ['history', 'science'],
                'description': 'An equinoctial sundial and observatory.', 'history': 'Built by Maharaja Jai Singh II of Jaipur in 1724.',
                'why_famous': 'Astronomical instruments.', 'interesting_facts': ['Contains 13 architectural astronomy instruments'],
                'coordinates': [28.6271, 77.2166], 'address': 'Connaught Place, New Delhi',
                'ticket': {'adult': 25, 'child': 0, 'foreign': 300, 'student': 25, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.3, 'photo_keyword': 'Jantar Mantar Delhi',
                'tips': ['Visit on a sunny day to see the shadows'], 'nearby': ['Connaught Place'], 'reviews': []
            },
            {
                'id': 'national-zoological-park', 'name': 'National Zoological Park', 'category': 'Zoo', 'tags': ['nature', 'family'],
                'description': 'A 176-acre zoo in New Delhi.', 'history': 'Inaugurated in 1959.',
                'why_famous': 'Wide variety of animal species.', 'interesting_facts': ['Home to a white tiger'],
                'coordinates': [28.6033, 77.2471], 'address': 'Mathura Rd, New Delhi',
                'ticket': {'adult': 80, 'child': 40, 'foreign': 400, 'student': 80, 'camera': 0, 'parking': 50, 'is_free': False},
                'timings': {'open': '9:30 AM', 'close': '4:30 PM', 'weekly_off': 'Friday', 'best_time': 'Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.2, 'photo_keyword': 'Delhi Zoo',
                'tips': ['Book tickets online in advance'], 'nearby': ['Purana Qila'], 'reviews': []
            },
            {
                'id': 'garden-of-five-senses', 'name': 'Garden of Five Senses', 'category': 'Park', 'tags': ['nature', 'art'],
                'description': 'A park developed by Delhi Tourism to stimulate the five senses.', 'history': 'Opened in 2003.',
                'why_famous': 'Beautiful landscaping and public art.', 'interesting_facts': ['Hosts various cultural festivals'],
                'coordinates': [28.5135, 77.1983], 'address': 'Westend Marg, Saidulajab, Saket, New Delhi',
                'ticket': {'adult': 35, 'child': 15, 'foreign': 35, 'student': 35, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '7:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.1, 'photo_keyword': 'Garden of Five Senses',
                'tips': ['Great place for a romantic walk'], 'nearby': ['Qutub Minar'], 'reviews': []
            },
            {
                'id': 'agrasen-ki-baoli', 'name': 'Agrasen ki Baoli', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A 60-meter long and 15-meter wide historical step well.', 'history': 'Rebuilt in the 14th century.',
                'why_famous': 'Unique architecture right in the middle of the city.', 'interesting_facts': ['Has 108 steps'],
                'coordinates': [28.6261, 77.2250], 'address': 'Hailey Road, KG Marg, near Diwanchand Imaging Centre, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '9:00 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '30 mins'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'Medium', 'rating': 4.4, 'photo_keyword': 'Agrasen ki Baoli',
                'tips': ['Featured in many Bollywood movies'], 'nearby': ['Connaught Place'], 'reviews': []
            },
            {
                'id': 'mehrauli-archaeological-park', 'name': 'Mehrauli Archaeological Park', 'category': 'Park', 'tags': ['history', 'nature'],
                'description': 'An archaeological area spread over 200 acres.', 'history': 'Contains ruins from various eras of Delhi.',
                'why_famous': 'Over 100 historically significant monuments.', 'interesting_facts': ['Adjacent to Qutub Minar'],
                'coordinates': [28.5186, 77.1857], 'address': 'Mehrauli, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '5:00 AM', 'close': '6:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': False, 'parking': True},
                'crowd': 'Low', 'rating': 4.6, 'photo_keyword': 'Mehrauli Archaeological Park',
                'tips': ['Hire a guide to understand the history'], 'nearby': ['Qutub Minar'], 'reviews': []
            },
            {
                'id': 'rail-museum', 'name': 'National Rail Museum', 'category': 'Museum', 'tags': ['family', 'history'],
                'description': 'A museum focusing on the rail heritage of India.', 'history': 'Opened in 1977.',
                'why_famous': 'Collection of vintage trains.', 'interesting_facts': ['Has a working toy train ride'],
                'coordinates': [28.5855, 77.1793], 'address': 'Chanakyapuri, New Delhi',
                'ticket': {'adult': 50, 'child': 10, 'foreign': 50, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '4:30 PM', 'weekly_off': 'Monday', 'best_time': 'Anytime', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'National Rail Museum',
                'tips': ['Great place for kids'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'khan-market', 'name': 'Khan Market', 'category': 'Market', 'tags': ['shopping', 'food'],
                'description': 'One of the most expensive high-street commercial locations in India.', 'history': 'Established in 1951.',
                'why_famous': 'High-end cafes, restaurants, and boutiques.', 'interesting_facts': ['Named after Khan Abdul Jabbar Khan'],
                'coordinates': [28.6001, 77.2274], 'address': 'Humayun Road, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:00 AM', 'close': '12:00 AM', 'weekly_off': 'Sunday', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Khan Market',
                'tips': ['Try the bakeries'], 'nearby': ['Lodi Garden'], 'reviews': []
            },
            {
                'id': 'majnu-ka-tila', 'name': 'Majnu Ka Tila', 'category': 'Neighborhood', 'tags': ['culture', 'food'],
                'description': 'A Tibetan refugee colony known for its authentic culture and food.', 'history': 'Established around 1950.',
                'why_famous': 'Tibetan cafes and monasteries.', 'interesting_facts': ['Often called Little Tibet of Delhi'],
                'coordinates': [28.7011, 77.2263], 'address': 'North Delhi, near ISBT Kashmere Gate, New Delhi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '9:00 AM', 'close': '10:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'High', 'rating': 4.3, 'photo_keyword': 'Majnu Ka Tila',
                'tips': ['Try Laping and Momos'], 'nearby': [], 'reviews': []
            }
        ]
    },
    'mumbai': {
        'name': 'Mumbai',
        'state': 'Maharashtra',
        'tagline': 'The City of Dreams',
        'description': 'India’s financial powerhouse and home to Bollywood, Mumbai is a fast-paced city on the coast of the Arabian Sea.',
        'coordinates': [19.0760, 72.8777],
        'best_season': 'November to February',
        'languages': ['Marathi', 'Hindi', 'English'],
        'famous_food': [
            {'name': 'Vada Pav', 'description': 'Deep fried potato dumpling placed inside a bread bun.', 'where_to_eat': 'Ashok Vada Pav, Dadar'}
        ],
        'instagram_spots': [
            {'name': 'Marine Drive', 'tip': 'Queen\'s Necklace view at night'}
        ],
        'trip_cost': {
            'budget': {'per_day': 1000, 'hotel': 500, 'food': 300, 'transport': 200},
            'standard': {'per_day': 3000, 'hotel': 1800, 'food': 800, 'transport': 400},
            'luxury': {'per_day': 10000, 'hotel': 7000, 'food': 2000, 'transport': 1000}
        },
        'attractions': [
            {
                'id': 'gateway-of-india', 'name': 'Gateway of India', 'category': 'Monument', 'tags': ['history', 'photography'],
                'description': 'An arch-monument built in the early 20th century.', 'history': 'Built to commemorate the landing of King George V in 1911.',
                'why_famous': 'The city\'s most famous landmark.', 'interesting_facts': ['Built from yellow basalt and concrete'],
                'coordinates': [18.9220, 72.8347], 'address': 'Apollo Bandar, Colaba, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Early Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'Very High', 'rating': 4.6, 'photo_keyword': 'Gateway of India',
                'tips': ['Take a boat ride from here to Elephanta Caves'], 'nearby': ['Colaba Causeway'], 'reviews': []
            },
            {
                'id': 'marine-drive', 'name': 'Marine Drive', 'category': 'Beach', 'tags': ['nature', 'photography'],
                'description': 'A 3.6-kilometre-long boulevard along the coast.', 'history': 'Built on reclaimed land in the 1920s.',
                'why_famous': 'Known as the Queen\'s Necklace.', 'interesting_facts': ['C-shaped six-lane concrete road'],
                'coordinates': [18.9440, 72.8229], 'address': 'Netaji Subhash Chandra Bose Road, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Sunset', 'visit_duration': '1-2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'High', 'rating': 4.8, 'photo_keyword': 'Marine Drive Mumbai',
                'tips': ['Best enjoyed with a walk during sunset'], 'nearby': ['Chowpatty Beach'], 'reviews': []
            },
            {
                'id': 'elephanta-caves', 'name': 'Elephanta Caves', 'category': 'Monument', 'tags': ['history', 'culture'],
                'description': 'A collection of cave temples predominantly dedicated to the Hindu god Shiva.', 'history': 'Dates back to the 5th-7th centuries.',
                'why_famous': 'Rock-cut stone sculptures.', 'interesting_facts': ['UNESCO World Heritage Site'],
                'coordinates': [18.9633, 72.9315], 'address': 'Elephanta Island, Mumbai',
                'ticket': {'adult': 40, 'child': 0, 'foreign': 600, 'student': 40, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '5:00 PM', 'weekly_off': 'Monday', 'best_time': 'Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Elephanta Caves',
                'tips': ['Beware of monkeys'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'juhu-beach', 'name': 'Juhu Beach', 'category': 'Beach', 'tags': ['nature', 'family'],
                'description': 'One of the most famous beaches in Mumbai.', 'history': 'Popularized over decades as a prime hangout spot.',
                'why_famous': 'Street food like Pav Bhaji and Bhel Puri.', 'interesting_facts': ['Surrounded by celebrity homes'],
                'coordinates': [19.0988, 72.8267], 'address': 'Juhu Tara Road, Juhu, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Very High', 'rating': 4.2, 'photo_keyword': 'Juhu Beach',
                'tips': ['Try the local street food'], 'nearby': ['ISKCON Temple Juhu'], 'reviews': []
            },
            {
                'id': 'chhatrapati-shivaji-terminus', 'name': 'Chhatrapati Shivaji Terminus', 'category': 'Monument', 'tags': ['architecture', 'history'],
                'description': 'A historic railway terminus.', 'history': 'Built in 1887 to commemorate Queen Victoria\'s Golden Jubilee.',
                'why_famous': 'Victorian Italianate Gothic Revival architecture.', 'interesting_facts': ['UNESCO World Heritage Site'],
                'coordinates': [18.9398, 72.8355], 'address': 'Chhatrapati Shivaji Terminus Area, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Night', 'visit_duration': '30 mins'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'Very High', 'rating': 4.6, 'photo_keyword': 'CST Mumbai',
                'tips': ['Looks beautiful when lit up at night'], 'nearby': ['Crawford Market'], 'reviews': []
            },
            {
                'id': 'haji-ali-dargah', 'name': 'Haji Ali Dargah', 'category': 'Monument', 'tags': ['religion'],
                'description': 'A mosque and dargah located on an islet off the coast of Worli.', 'history': 'Constructed in 1431.',
                'why_famous': 'Its location in the sea.', 'interesting_facts': ['Only accessible during low tide'],
                'coordinates': [18.9827, 72.8089], 'address': 'Dargah Rd, Haji Ali, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '5:30 AM', 'close': '10:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Haji Ali Dargah',
                'tips': ['Check tide timings before visiting'], 'nearby': ['Mahalaxmi Temple'], 'reviews': []
            },
            {
                'id': 'sanjay-gandhi-national-park', 'name': 'Sanjay Gandhi National Park', 'category': 'Nature', 'tags': ['nature', 'wildlife'],
                'description': 'A large protected area in the northern part of Mumbai city.', 'history': 'Established in 1969.',
                'why_famous': 'Dense forests and Kanheri Caves inside the city.', 'interesting_facts': ['One of the most visited national parks in the world'],
                'coordinates': [19.2298, 72.8997], 'address': 'Borivali East, Mumbai',
                'ticket': {'adult': 85, 'child': 45, 'foreign': 85, 'student': 85, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '7:30 AM', 'close': '6:30 PM', 'weekly_off': 'Monday', 'best_time': 'Morning', 'visit_duration': '4 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.4, 'photo_keyword': 'Sanjay Gandhi National Park',
                'tips': ['Rent a cycle to explore'], 'nearby': ['Kanheri Caves'], 'reviews': []
            },
            {
                'id': 'siddhivinayak-temple', 'name': 'Siddhivinayak Temple', 'category': 'Temple', 'tags': ['religion'],
                'description': 'A Hindu temple dedicated to Lord Shri Ganesha.', 'history': 'Originally built in 1801.',
                'why_famous': 'One of the richest temples in Mumbai.', 'interesting_facts': ['Frequent visits by Bollywood celebrities'],
                'coordinates': [19.0166, 72.8300], 'address': 'SK Bole Marg, Prabhadevi, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '5:30 AM', 'close': '10:00 PM', 'weekly_off': 'None', 'best_time': 'Early Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'Very High', 'rating': 4.7, 'photo_keyword': 'Siddhivinayak Temple',
                'tips': ['Expect long queues, especially on Tuesdays'], 'nearby': ['Dadar'], 'reviews': []
            },
            {
                'id': 'colaba-causeway', 'name': 'Colaba Causeway', 'category': 'Market', 'tags': ['shopping', 'food'],
                'description': 'A commercial street, and a major causeway.', 'history': 'Built in 1838 to connect Colaba with the Old Woman\'s Island.',
                'why_famous': 'Street shopping and vintage cafes.', 'interesting_facts': ['Houses the famous Cafe Mondegar and Leopold Cafe'],
                'coordinates': [18.9168, 72.8268], 'address': 'Colaba, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:00 AM', 'close': '10:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Colaba Causeway',
                'tips': ['Bargain hard'], 'nearby': ['Gateway of India'], 'reviews': []
            },
            {
                'id': 'bandstand-bandra', 'name': 'Bandstand Bandra', 'category': 'Promenade', 'tags': ['nature', 'celebrity'],
                'description': 'A 1.2 kilometer long walkway along the sea on the western coast of Mumbai.', 'history': 'A popular spot for locals for decades.',
                'why_famous': 'Celebrity homes like Shah Rukh Khan\'s Mannat.', 'interesting_facts': ['Has a "Walk of the Stars"'],
                'coordinates': [19.0469, 72.8193], 'address': 'Bandstand Promenade, Bandra West, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Sunset', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Bandstand Promenade',
                'tips': ['Great place to chill with friends'], 'nearby': ['Mount Mary Church'], 'reviews': []
            },
            {
                'id': 'global-vipassana-pagoda', 'name': 'Global Vipassana Pagoda', 'category': 'Monument', 'tags': ['religion', 'peace'],
                'description': 'A Meditation Hall near Gorai, North-west of Mumbai.', 'history': 'Inaugurated by Pratibha Patil, then President of India on 8 February 2009.',
                'why_famous': 'Monument of peace and harmony.', 'interesting_facts': ['Contains bone relics of Gautama Buddha'],
                'coordinates': [19.2284, 72.8058], 'address': 'Global Pagoda Road, Gorai, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '9:00 AM', 'close': '7:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'Global Vipassana Pagoda',
                'tips': ['Take a ferry from Gorai creek for a scenic route'], 'nearby': ['EsselWorld'], 'reviews': []
            },
            {
                'id': 'powai-lake', 'name': 'Powai Lake', 'category': 'Nature', 'tags': ['nature'],
                'description': 'An artificial lake situated in the Powai valley.', 'history': 'Created in 1890.',
                'why_famous': 'Scenic views and crocodiles.', 'interesting_facts': ['Near the IIT Bombay campus'],
                'coordinates': [19.1246, 72.9037], 'address': 'Powai, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'Medium', 'rating': 4.2, 'photo_keyword': 'Powai Lake',
                'tips': ['Do not get too close to the water'], 'nearby': ['Hiranandani Gardens'], 'reviews': []
            },
            {
                'id': 'bandra-worli-sea-link', 'name': 'Bandra Worli Sea Link', 'category': 'Architecture', 'tags': ['architecture', 'photography'],
                'description': 'A cable-stayed bridge that links Bandra in the Western Suburbs of Mumbai with Worli in South Mumbai.', 'history': 'Opened in 2009.',
                'why_famous': 'Engineering marvel and iconic city view.', 'interesting_facts': ['Weighs as much as 50,000 African elephants'],
                'coordinates': [19.0356, 72.8173], 'address': 'Bandra Worli Sea Link, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Night', 'visit_duration': '30 mins'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': False, 'parking': False},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'Bandra Worli Sea Link',
                'tips': ['Best experienced by driving across it'], 'nearby': ['Worli Sea Face'], 'reviews': []
            },
            {
                'id': 'chor-bazaar', 'name': 'Chor Bazaar', 'category': 'Market', 'tags': ['shopping', 'culture'],
                'description': 'One of the largest flea markets in India.', 'history': 'Existed for over 150 years.',
                'why_famous': 'Vintage items and antiques.', 'interesting_facts': ['Name means "Thieves Market"'],
                'coordinates': [18.9602, 72.8260], 'address': 'Mutton St, Kumbharwada, Mumbai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '11:00 AM', 'close': '7:30 PM', 'weekly_off': 'Friday', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.0, 'photo_keyword': 'Chor Bazaar Mumbai',
                'tips': ['Keep an eye on your belongings'], 'nearby': ['Mohammad Ali Road'], 'reviews': []
            },
            {
                'id': 'film-city', 'name': 'Film City Mumbai', 'category': 'Attraction', 'tags': ['entertainment'],
                'description': 'An integrated film studio complex.', 'history': 'Built in 1977 by the state government.',
                'why_famous': 'Heart of the Bollywood film industry.', 'interesting_facts': ['Has numerous sets like temples, villages, and cities'],
                'coordinates': [19.1601, 72.8804], 'address': 'Goregaon East, Mumbai',
                'ticket': {'adult': 599, 'child': 599, 'foreign': 599, 'student': 599, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Anytime', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.1, 'photo_keyword': 'Film City Mumbai',
                'tips': ['Guided tours must be booked in advance'], 'nearby': ['Sanjay Gandhi National Park'], 'reviews': []
            }
        ]
    },
    'goa': {
        'name': 'Goa',
        'state': 'Goa',
        'tagline': 'The Pearl of the Orient',
        'description': 'Famous for its beaches, nightlife, and Portuguese heritage.',
        'coordinates': [15.2993, 74.1240],
        'best_season': 'November to February',
        'languages': ['Konkani', 'English', 'Hindi'],
        'famous_food': [
            {'name': 'Goan Fish Curry', 'description': 'Spicy and tangy coconut-based curry.', 'where_to_eat': 'Ritz Classic, Panaji'}
        ],
        'instagram_spots': [
            {'name': 'Fontainhas', 'tip': 'Colorful Portuguese houses'}
        ],
        'trip_cost': {
            'budget': {'per_day': 1200, 'hotel': 600, 'food': 400, 'transport': 200},
            'standard': {'per_day': 3500, 'hotel': 2000, 'food': 1000, 'transport': 500},
            'luxury': {'per_day': 12000, 'hotel': 8000, 'food': 2500, 'transport': 1500}
        },
        'attractions': [
            {
                'id': 'baga-beach', 'name': 'Baga Beach', 'category': 'Beach', 'tags': ['nature', 'nightlife'],
                'description': 'One of the most popular beaches in North Goa.', 'history': 'Developed as a tourist destination in the 1960s.',
                'why_famous': 'Water sports and nightlife.', 'interesting_facts': ['Contains famous shacks like Britto\'s'],
                'coordinates': [15.5553, 73.7517], 'address': 'Baga, Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 50, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Very High', 'rating': 4.3, 'photo_keyword': 'Baga Beach Goa',
                'tips': ['Very crowded during peak season'], 'nearby': ['Calangute Beach'], 'reviews': []
            },
            {
                'id': 'anjuna-beach', 'name': 'Anjuna Beach', 'category': 'Beach', 'tags': ['nature', 'nightlife'],
                'description': 'Known for its trance parties and flea market.', 'history': 'Popularized by hippies in the 1970s.',
                'why_famous': 'Flea market and Curlies shack.', 'interesting_facts': ['Has interesting rock formations'],
                'coordinates': [15.5878, 73.7423], 'address': 'Anjuna, Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 50, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Anjuna Beach',
                'tips': ['Visit the Wednesday Flea Market'], 'nearby': ['Vagator Beach'], 'reviews': []
            },
            {
                'id': 'palolem-beach', 'name': 'Palolem Beach', 'category': 'Beach', 'tags': ['nature', 'peace'],
                'description': 'A crescent-shaped beach in South Goa.', 'history': 'Maintained its scenic beauty over the years.',
                'why_famous': 'Calm waters and silent noise parties.', 'interesting_facts': ['Featured in the movie The Bourne Supremacy'],
                'coordinates': [15.0100, 74.0232], 'address': 'Palolem, Canacona, Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 50, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Sunset', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.6, 'photo_keyword': 'Palolem Beach',
                'tips': ['Take a boat ride to see dolphins'], 'nearby': ['Agonda Beach'], 'reviews': []
            },
            {
                'id': 'basilica-of-bom-jesus', 'name': 'Basilica of Bom Jesus', 'category': 'Monument', 'tags': ['history', 'religion'],
                'description': 'A Roman Catholic basilica located in Old Goa.', 'history': 'Constructed in 1605.',
                'why_famous': 'Holds the mortal remains of St. Francis Xavier.', 'interesting_facts': ['UNESCO World Heritage Site'],
                'coordinates': [15.5009, 73.9116], 'address': 'Old Goa Road, Bainguinim, Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '9:00 AM', 'close': '6:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.7, 'photo_keyword': 'Basilica of Bom Jesus',
                'tips': ['Dress modestly'], 'nearby': ['Se Cathedral'], 'reviews': []
            },
            {
                'id': 'fort-aguada', 'name': 'Fort Aguada', 'category': 'Monument', 'tags': ['history', 'photography'],
                'description': 'A well-preserved seventeenth-century Portuguese fort.', 'history': 'Constructed in 1612.',
                'why_famous': 'Lighthouse and sea views.', 'interesting_facts': ['Was used as a prison during the Salazar administration'],
                'coordinates': [15.4935, 73.7663], 'address': 'Fort Aguada Rd, Aguada Fort Area, Candolim, Goa',
                'ticket': {'adult': 25, 'child': 0, 'foreign': 300, 'student': 25, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '8:30 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1-2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Fort Aguada',
                'tips': ['Sunset offers great views'], 'nearby': ['Sinquerim Beach'], 'reviews': []
            },
            {
                'id': 'dudhsagar-falls', 'name': 'Dudhsagar Falls', 'category': 'Nature', 'tags': ['nature', 'adventure'],
                'description': 'A four-tiered waterfall located on the Mandovi River.', 'history': 'Legend says a princess poured milk to form a curtain.',
                'why_famous': 'One of India\'s tallest waterfalls.', 'interesting_facts': ['Means "Sea of Milk"'],
                'coordinates': [15.3144, 74.3143], 'address': 'Sonaulim, Goa',
                'ticket': {'adult': 400, 'child': 400, 'foreign': 400, 'student': 400, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '7:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Monsoon', 'visit_duration': '4 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': False, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Dudhsagar Falls',
                'tips': ['Jeep safari is required to reach the falls'], 'nearby': ['Bhagwan Mahaveer Sanctuary'], 'reviews': []
            },
            {
                'id': 'chapora-fort', 'name': 'Chapora Fort', 'category': 'Monument', 'tags': ['history', 'photography'],
                'description': 'An ancient fort overlooking the Chapora river.', 'history': 'Built by Adil Shah of Bijapur.',
                'why_famous': 'Featured in the Bollywood movie Dil Chahta Hai.', 'interesting_facts': ['Offers panoramic views of Vagator beach'],
                'coordinates': [15.6053, 73.7371], 'address': 'Chapora Fort Rd, Chapora, Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '9:30 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Sunset', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'Medium', 'rating': 4.2, 'photo_keyword': 'Chapora Fort',
                'tips': ['Steep climb, wear comfortable shoes'], 'nearby': ['Vagator Beach'], 'reviews': []
            },
            {
                'id': 'vagator-beach', 'name': 'Vagator Beach', 'category': 'Beach', 'tags': ['nature', 'party'],
                'description': 'A stunning beach with red cliffs.', 'history': 'Known for its rave party culture.',
                'why_famous': 'Trance parties and dramatic cliffs.', 'interesting_facts': ['Split into Big Vagator and Little Vagator'],
                'coordinates': [15.6030, 73.7336], 'address': 'Vagator, Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 50, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Vagator Beach',
                'tips': ['Visit the face carved on the rocks at Little Vagator'], 'nearby': ['Chapora Fort'], 'reviews': []
            },
            {
                'id': 'panaji-city', 'name': 'Panaji City', 'category': 'City', 'tags': ['culture', 'architecture'],
                'description': 'The capital of Goa, known for its Portuguese influence.', 'history': 'Replaced Old Goa as the capital in 1843.',
                'why_famous': 'Casinos, churches, and Latin Quarter.', 'interesting_facts': ['Built along the Mandovi River'],
                'coordinates': [15.4909, 73.8278], 'address': 'Panaji, Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '4 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Panaji City',
                'tips': ['Take an evening river cruise'], 'nearby': ['Fontainhas'], 'reviews': []
            },
            {
                'id': 'fontainhas', 'name': 'Fontainhas Latin Quarter', 'category': 'Neighborhood', 'tags': ['culture', 'photography'],
                'description': 'An old Latin Quarter in Panjim.', 'history': 'Established in the late 18th century.',
                'why_famous': 'Colorful Portuguese colonial architecture.', 'interesting_facts': ['UNESCO Heritage Zone'],
                'coordinates': [15.4950, 73.8322], 'address': 'Fontainhas, Panaji, Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'Fontainhas Goa',
                'tips': ['Perfect for a photo walk'], 'nearby': ['Panaji City'], 'reviews': []
            },
            {
                'id': 'mollem-national-park', 'name': 'Mollem National Park', 'category': 'Nature', 'tags': ['nature', 'wildlife'],
                'description': 'A national park and wildlife sanctuary.', 'history': 'Declared a national park in 1978.',
                'why_famous': 'Rich biodiversity and Dudhsagar falls.', 'interesting_facts': ['Home to the black panther'],
                'coordinates': [15.3622, 74.2568], 'address': 'Sanguem, Goa',
                'ticket': {'adult': 50, 'child': 20, 'foreign': 50, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '8:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '4 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Low', 'rating': 4.2, 'photo_keyword': 'Mollem National Park',
                'tips': ['Combine with Dudhsagar visit'], 'nearby': ['Dudhsagar Falls'], 'reviews': []
            },
            {
                'id': 'shri-mangueshi-temple', 'name': 'Shri Mangueshi Temple', 'category': 'Temple', 'tags': ['religion', 'architecture'],
                'description': 'One of the largest and most frequently visited temples in Goa.', 'history': 'Dates back to the 16th century.',
                'why_famous': 'Beautiful architecture and deep stambha.', 'interesting_facts': ['Dedicated to Lord Shiva'],
                'coordinates': [15.4385, 73.9785], 'address': 'Mangeshi village, Mardol, Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '6:00 AM', 'close': '10:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Mangueshi Temple',
                'tips': ['Dress modestly'], 'nearby': ['Spice Plantations'], 'reviews': []
            },
            {
                'id': 'cabo-de-rama-fort', 'name': 'Cabo de Rama Fort', 'category': 'Monument', 'tags': ['history', 'photography'],
                'description': 'An ancient fort in South Goa.', 'history': 'Claimed by the Portuguese in 1763.',
                'why_famous': 'Stunning views of the Arabian sea.', 'interesting_facts': ['Named after Lord Rama'],
                'coordinates': [15.0886, 73.9213], 'address': 'Canacona, South Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '9:00 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': False, 'parking': True},
                'crowd': 'Low', 'rating': 4.3, 'photo_keyword': 'Cabo de Rama Fort',
                'tips': ['Great offbeat location'], 'nearby': ['Agonda Beach'], 'reviews': []
            },
            {
                'id': 'spice-plantations', 'name': 'Spice Plantations', 'category': 'Nature', 'tags': ['nature', 'culture'],
                'description': 'Farms growing exotic spices.', 'history': 'Traditional agricultural practices.',
                'why_famous': 'Guided tours and traditional Goan lunch.', 'interesting_facts': ['Learn how spices are grown and processed'],
                'coordinates': [15.3995, 74.0163], 'address': 'Ponda, Goa',
                'ticket': {'adult': 500, 'child': 300, 'foreign': 500, 'student': 500, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '4:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.4, 'photo_keyword': 'Spice Plantation Goa',
                'tips': ['Enjoy the complementary lunch'], 'nearby': ['Shri Mangueshi Temple'], 'reviews': []
            },
            {
                'id': 'butterfly-beach', 'name': 'Butterfly Beach', 'category': 'Beach', 'tags': ['nature', 'peace'],
                'description': 'A secluded and beautiful beach in South Goa.', 'history': 'Known for its untouched beauty.',
                'why_famous': 'Dolphin sightings and butterflies.', 'interesting_facts': ['Accessible only by boat or a hike'],
                'coordinates': [15.0135, 73.9926], 'address': 'Canacona, South Goa',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': False, 'parking': False},
                'crowd': 'Low', 'rating': 4.8, 'photo_keyword': 'Butterfly Beach Goa',
                'tips': ['Carry your own food and water'], 'nearby': ['Palolem Beach'], 'reviews': []
            }
        ]
    },
    'jaipur': {
        'name': 'Jaipur',
        'state': 'Rajasthan',
        'tagline': 'The Pink City',
        'description': 'Famous for its historic forts, palaces, and vibrant culture.',
        'coordinates': [26.9124, 75.7873],
        'best_season': 'October to March',
        'languages': ['Hindi', 'Rajasthani', 'English'],
        'famous_food': [
            {'name': 'Dal Bati Churma', 'description': 'Lentils served with hard wheat rolls and a sweet cereal.', 'where_to_eat': 'Chokhi Dhani'}
        ],
        'instagram_spots': [
            {'name': 'Patrika Gate', 'tip': 'Symmetrical colorful arches'}
        ],
        'trip_cost': {
            'budget': {'per_day': 900, 'hotel': 400, 'food': 300, 'transport': 200},
            'standard': {'per_day': 2500, 'hotel': 1200, 'food': 800, 'transport': 500},
            'luxury': {'per_day': 8000, 'hotel': 5000, 'food': 2000, 'transport': 1000}
        },
        'attractions': [
            {
                'id': 'amer-fort', 'name': 'Amer Fort', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A majestic fort located high on a hill.', 'history': 'Built by Raja Man Singh in 1592.',
                'why_famous': 'Hindu architectural elements and large ramparts.', 'interesting_facts': ['UNESCO World Heritage Site'],
                'coordinates': [26.9855, 75.8513], 'address': 'Devisinghpura, Amer, Jaipur',
                'ticket': {'adult': 100, 'child': 50, 'foreign': 500, 'student': 100, 'camera': 0, 'parking': 50, 'is_free': False},
                'timings': {'open': '8:00 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.7, 'photo_keyword': 'Amer Fort',
                'tips': ['Elephant rides are available but walking is recommended'], 'nearby': ['Jaigarh Fort'], 'reviews': []
            },
            {
                'id': 'hawa-mahal', 'name': 'Hawa Mahal', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A palace built from red and pink sandstone.', 'history': 'Built in 1799 by Maharaja Sawai Pratap Singh.',
                'why_famous': 'Its unique five-story exterior akin to the honeycomb of a beehive.', 'interesting_facts': ['Has 953 small windows called jharokhas'],
                'coordinates': [26.8852, 75.8267], 'address': 'Hawa Mahal Rd, Badi Choupad, J.D.A. Market, Pink City, Jaipur',
                'ticket': {'adult': 50, 'child': 0, 'foreign': 200, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '4:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Hawa Mahal',
                'tips': ['Best viewed from the cafes opposite the street'], 'nearby': ['City Palace'], 'reviews': []
            },
            {
                'id': 'city-palace-jaipur', 'name': 'City Palace Jaipur', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A complex of courtyards, gardens and buildings.', 'history': 'Built between 1729 and 1732.',
                'why_famous': 'A beautiful blend of Mughal and Rajput architecture.', 'interesting_facts': ['The royal family still lives in part of the palace'],
                'coordinates': [26.9255, 75.8236], 'address': 'Tulsi Marg, Gangori Bazaar, J.D.A. Market, Pink City, Jaipur',
                'ticket': {'adult': 200, 'child': 100, 'foreign': 700, 'student': 200, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:30 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'City Palace Jaipur',
                'tips': ['Take a guided tour'], 'nearby': ['Jantar Mantar'], 'reviews': []
            },
            {
                'id': 'jantar-mantar-jaipur', 'name': 'Jantar Mantar Jaipur', 'category': 'Monument', 'tags': ['history', 'science'],
                'description': 'A collection of 19 architectural astronomical instruments.', 'history': 'Built by the Rajput king Sawai Jai Singh II.',
                'why_famous': 'Features the world\'s largest stone sundial.', 'interesting_facts': ['UNESCO World Heritage Site'],
                'coordinates': [26.9247, 75.8245], 'address': 'Gangori Bazaar, J.D.A. Market, Pink City, Jaipur',
                'ticket': {'adult': 50, 'child': 0, 'foreign': 200, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '4:30 PM', 'weekly_off': 'None', 'best_time': 'Midday', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Jantar Mantar Jaipur',
                'tips': ['Hire a guide to understand the instruments'], 'nearby': ['City Palace'], 'reviews': []
            },
            {
                'id': 'nahargarh-fort', 'name': 'Nahargarh Fort', 'category': 'Monument', 'tags': ['history', 'views'],
                'description': 'Fort stands on the edge of the Aravalli Hills, overlooking the city of Jaipur.', 'history': 'Built in 1734 by Maharaja Sawai Jai Singh.',
                'why_famous': 'Stunning sunset views of the entire city.', 'interesting_facts': ['Connected to Jaigarh Fort through its fortifications'],
                'coordinates': [26.9373, 75.8155], 'address': 'Krishna Nagar, Brahampuri, Jaipur',
                'ticket': {'adult': 50, 'child': 0, 'foreign': 200, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Sunset', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Nahargarh Fort Sunset',
                'tips': ['Visit the Padao restaurant for city views'], 'nearby': ['Jaigarh Fort'], 'reviews': []
            },
            {
                'id': 'jaigarh-fort', 'name': 'Jaigarh Fort', 'category': 'Monument', 'tags': ['history', 'military'],
                'description': 'A rugged fort built to protect the Amer Fort.', 'history': 'Built by Jai Singh II in 1726.',
                'why_famous': 'Houses the Jaivana cannon, the world\'s largest cannon on wheels.', 'interesting_facts': ['Never conquered in battle'],
                'coordinates': [26.9839, 75.8460], 'address': 'Devisinghpura, Amer, Jaipur',
                'ticket': {'adult': 35, 'child': 0, 'foreign': 85, 'student': 35, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '4:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.4, 'photo_keyword': 'Jaigarh Fort Cannon',
                'tips': ['Walk through the underground passages'], 'nearby': ['Amer Fort'], 'reviews': []
            },
            {
                'id': 'albert-hall-museum', 'name': 'Albert Hall Museum', 'category': 'Museum', 'tags': ['history', 'art'],
                'description': 'The oldest museum of the state and functions as the state museum of Rajasthan.', 'history': 'Designed by Sir Samuel Swinton Jacob.',
                'why_famous': 'Indo-Saracenic architecture and Egyptian mummy.', 'interesting_facts': ['Looks spectacular when illuminated at night'],
                'coordinates': [26.9116, 75.8195], 'address': 'Museum Road, Ram Niwas Garden, Kailash Puri, Adarsh Nagar, Jaipur',
                'ticket': {'adult': 40, 'child': 0, 'foreign': 300, 'student': 40, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Anytime', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Albert Hall Museum Jaipur',
                'tips': ['Night tourism is also available here'], 'nearby': ['Jaipur Zoo'], 'reviews': []
            },
            {
                'id': 'jal-mahal', 'name': 'Jal Mahal', 'category': 'Monument', 'tags': ['architecture', 'nature'],
                'description': 'A palace in the middle of the Man Sagar Lake.', 'history': 'Renovated and enlarged in the 18th century by Maharaja Jai Singh II.',
                'why_famous': 'It appears to float on the lake.', 'interesting_facts': ['Four of its five floors are underwater when the lake is full'],
                'coordinates': [26.9530, 75.8465], 'address': 'Amer Road, Jal Mahal, Amer, Jaipur',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Sunset', 'visit_duration': '30 mins'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Jal Mahal Jaipur',
                'tips': ['Entry inside is restricted, view from the banks'], 'nearby': ['Amer Fort'], 'reviews': []
            },
            {
                'id': 'birla-temple-jaipur', 'name': 'Birla Temple Jaipur', 'category': 'Temple', 'tags': ['religion', 'peace'],
                'description': 'A Hindu temple built of white marble.', 'history': 'Built in 1988 by the B.M. Birla Foundation.',
                'why_famous': 'Stunning white marble architecture.', 'interesting_facts': ['Dedicated to Lord Vishnu and Goddess Lakshmi'],
                'coordinates': [26.8924, 75.8153], 'address': 'Jawahar Lal Nehru Marg, Tilak Nagar, Jaipur',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '8:00 AM', 'close': '8:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.6, 'photo_keyword': 'Birla Temple Jaipur',
                'tips': ['Looks beautiful when lit up at night'], 'nearby': ['Albert Hall Museum'], 'reviews': []
            },
            {
                'id': 'galtaji-temple', 'name': 'Galtaji Temple', 'category': 'Temple', 'tags': ['religion', 'nature'],
                'description': 'An ancient Hindu pilgrimage site in the town of Khaniya-Balaji.', 'history': 'Built in the 18th century.',
                'why_famous': 'Natural springs and large monkey population.', 'interesting_facts': ['Often called the Monkey Temple'],
                'coordinates': [26.9150, 75.8622], 'address': 'Galtaji, Jaipur',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 50, 'parking': 0, 'is_free': True},
                'timings': {'open': '5:00 AM', 'close': '9:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': False, 'parking': True},
                'crowd': 'Medium', 'rating': 4.3, 'photo_keyword': 'Galtaji Temple Monkeys',
                'tips': ['Beware of the monkeys'], 'nearby': ['Sisodia Rani Garden'], 'reviews': []
            },
            {
                'id': 'chokhi-dhani', 'name': 'Chokhi Dhani', 'category': 'Culture', 'tags': ['culture', 'food'],
                'description': 'A mock Rajasthani village resort.', 'history': 'Established to preserve Rajasthani culture.',
                'why_famous': 'Authentic Rajasthani food and cultural performances.', 'interesting_facts': ['Offers camel rides and magic shows'],
                'coordinates': [26.7674, 75.8173], 'address': '12 Miles Tonk Road, Via Vatika, Jaipur',
                'ticket': {'adult': 900, 'child': 500, 'foreign': 900, 'student': 900, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '5:00 PM', 'close': '11:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '4 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Chokhi Dhani Dinner',
                'tips': ['Go hungry, the food portions are large'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'johari-bazaar', 'name': 'Johari Bazaar', 'category': 'Market', 'tags': ['shopping', 'jewelry'],
                'description': 'A famous market for traditional Rajasthani jewelry.', 'history': 'One of the oldest markets in Jaipur.',
                'why_famous': 'Precious stones and Kundan jewelry.', 'interesting_facts': ['Name means "Jeweler\'s Market"'],
                'coordinates': [26.9202, 75.8271], 'address': 'Johari Bazar Road, Jaipur',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:00 AM', 'close': '11:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.3, 'photo_keyword': 'Johari Bazaar Jaipur',
                'tips': ['Bargaining is a must'], 'nearby': ['Hawa Mahal'], 'reviews': []
            },
            {
                'id': 'bapu-bazaar', 'name': 'Bapu Bazaar', 'category': 'Market', 'tags': ['shopping', 'textiles'],
                'description': 'A vibrant market known for its textiles and Mojari shoes.', 'history': 'A prominent shopping hub.',
                'why_famous': 'Camel leather shoes and vibrant textiles.', 'interesting_facts': ['Famous for Jaipuri quilts'],
                'coordinates': [26.9174, 75.8236], 'address': 'Bapu Bazaar, Jaipur',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '11:00 AM', 'close': '10:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Bapu Bazaar Shopping',
                'tips': ['Check out the block printed suits'], 'nearby': ['Albert Hall Museum'], 'reviews': []
            },
            {
                'id': 'panna-meena-kund', 'name': 'Panna Meena Kund', 'category': 'Monument', 'tags': ['architecture', 'history'],
                'description': 'An ancient stepwell.', 'history': 'Built in the 16th century.',
                'why_famous': 'Symmetrical staircases.', 'interesting_facts': ['Used as a community gathering space'],
                'coordinates': [26.9922, 75.8520], 'address': 'Amer, Jaipur',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '7:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '30 mins'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': False, 'parking': False},
                'crowd': 'Low', 'rating': 4.5, 'photo_keyword': 'Panna Meena Stepwell',
                'tips': ['Photography on the steps might require special permission'], 'nearby': ['Amer Fort'], 'reviews': []
            },
            {
                'id': 'sisodia-rani-garden', 'name': 'Sisodia Rani Garden', 'category': 'Garden', 'tags': ['nature', 'history'],
                'description': 'A palace garden with tiered levels and fountains.', 'history': 'Built in 1728 by Maharaja Sawai Jai Singh.',
                'why_famous': 'Wall paintings of Radha-Krishna.', 'interesting_facts': ['A symbol of the king\'s love for his queen'],
                'coordinates': [26.9015, 75.8647], 'address': 'Agra Road, Ghat Ki Guni, Jaipur',
                'ticket': {'adult': 50, 'child': 0, 'foreign': 200, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '8:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Low', 'rating': 4.1, 'photo_keyword': 'Sisodia Rani Garden',
                'tips': ['Peaceful getaway from the city'], 'nearby': ['Galtaji Temple'], 'reviews': []
            }
        ]
    },
    'agra': {
        'name': 'Agra',
        'state': 'Uttar Pradesh',
        'tagline': 'City of the Taj',
        'description': 'Home to the iconic Taj Mahal and rich Mughal history.',
        'coordinates': [27.1767, 78.0081],
        'best_season': 'October to March',
        'languages': ['Hindi', 'Urdu', 'English'],
        'famous_food': [
            {'name': 'Petha', 'description': 'Soft translucent candy made from ash gourd.', 'where_to_eat': 'Panchhi Petha Store'}
        ],
        'instagram_spots': [
            {'name': 'Taj Mahal from Mehtab Bagh', 'tip': 'Perfect for a less crowded perspective'}
        ],
        'trip_cost': {
            'budget': {'per_day': 800, 'hotel': 400, 'food': 250, 'transport': 150},
            'standard': {'per_day': 2000, 'hotel': 1000, 'food': 600, 'transport': 400},
            'luxury': {'per_day': 7000, 'hotel': 4500, 'food': 1500, 'transport': 1000}
        },
        'attractions': [
            {
                'id': 'taj-mahal', 'name': 'Taj Mahal', 'category': 'Monument', 'tags': ['history', 'wonder'],
                'description': 'An ivory-white marble mausoleum on the right bank of the river Yamuna.', 'history': 'Commissioned in 1632 by the Mughal emperor Shah Jahan.',
                'why_famous': 'One of the New Seven Wonders of the World.', 'interesting_facts': ['Changes color depending on the light'],
                'coordinates': [27.1751, 78.0421], 'address': 'Dharmapuri, Forest Colony, Tajganj, Agra',
                'ticket': {'adult': 50, 'child': 0, 'foreign': 1100, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': 'Sunrise', 'close': 'Sunset', 'weekly_off': 'Friday', 'best_time': 'Sunrise', 'visit_duration': '2-3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Very High', 'rating': 4.9, 'photo_keyword': 'Taj Mahal',
                'tips': ['Arrive early for sunrise to beat the crowd'], 'nearby': ['Agra Fort'], 'reviews': []
            },
            {
                'id': 'agra-fort', 'name': 'Agra Fort', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A historical fort in the city of Agra.', 'history': 'Main residence of the emperors of the Mughal Dynasty until 1638.',
                'why_famous': 'UNESCO World Heritage Site with beautiful palaces.', 'interesting_facts': ['Shah Jahan was imprisoned here by his son'],
                'coordinates': [27.1795, 78.0211], 'address': 'Agra Fort, Rakabganj, Agra',
                'ticket': {'adult': 50, 'child': 0, 'foreign': 650, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.7, 'photo_keyword': 'Agra Fort',
                'tips': ['Get a great view of the Taj Mahal from the balconies'], 'nearby': ['Taj Mahal'], 'reviews': []
            },
            {
                'id': 'fatehpur-sikri', 'name': 'Fatehpur Sikri', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A town in the Agra District, founded as the capital of Mughal Empire in 1571 by Emperor Akbar.', 'history': 'Abandoned due to lack of water.',
                'why_famous': 'Stunning red sandstone architecture like Buland Darwaza.', 'interesting_facts': ['UNESCO World Heritage Site'],
                'coordinates': [27.0945, 77.6679], 'address': 'Fatehpur Sikri, Uttar Pradesh',
                'ticket': {'adult': 50, 'child': 0, 'foreign': 610, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Fatehpur Sikri',
                'tips': ['Hire an official guide'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'itimad-ud-daulah', 'name': 'Itimad ud Daulah', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A Mughal mausoleum often described as a "jewel box".', 'history': 'Built between 1622 and 1628.',
                'why_famous': 'First Mughal structure made completely of marble.', 'interesting_facts': ['Often called the "Baby Taj"'],
                'coordinates': [27.1929, 78.0310], 'address': 'Moti Bagh, Agra',
                'ticket': {'adult': 30, 'child': 0, 'foreign': 310, 'student': 30, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Low', 'rating': 4.6, 'photo_keyword': 'Baby Taj Agra',
                'tips': ['Very peaceful compared to the Taj Mahal'], 'nearby': ['Mehtab Bagh'], 'reviews': []
            },
            {
                'id': 'mehtab-bagh', 'name': 'Mehtab Bagh', 'category': 'Garden', 'tags': ['nature', 'photography'],
                'description': 'A charbagh complex located north of the Taj Mahal complex.', 'history': 'Built by Emperor Babur.',
                'why_famous': 'Offers a perfect view of the Taj Mahal from across the river.', 'interesting_facts': ['Translates to "Moonlight Garden"'],
                'coordinates': [27.1795, 78.0426], 'address': 'Dharmapuri, Forest Colony, Nagla Devjit, Agra',
                'ticket': {'adult': 25, 'child': 0, 'foreign': 300, 'student': 25, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Sunset', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Mehtab Bagh View',
                'tips': ['Best place for sunset photos of the Taj'], 'nearby': ['Itimad ud Daulah'], 'reviews': []
            },
            {
                'id': 'akbar-tomb-sikandra', 'name': 'Akbar Tomb Sikandra', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'The tomb of the Mughal emperor Akbar.', 'history': 'Built 1605–1613 by his son Jahangir.',
                'why_famous': 'Architectural masterpiece blending different styles.', 'interesting_facts': ['Akbar planned the tomb and selected a suitable site for it'],
                'coordinates': [27.2206, 77.9505], 'address': 'Tomb of Akbar The Great Area, Sikandra, Agra',
                'ticket': {'adult': 30, 'child': 0, 'foreign': 310, 'student': 30, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1.5 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Low', 'rating': 4.6, 'photo_keyword': 'Akbar Tomb',
                'tips': ['Watch out for monkeys'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'jama-masjid-agra', 'name': 'Jama Masjid Agra', 'category': 'Mosque', 'tags': ['religion', 'history'],
                'description': 'A 17th-century congregational mosque.', 'history': 'Built by Shah Jahan in 1648.',
                'why_famous': 'Dedicated to his favorite daughter, Jahanara Begum.', 'interesting_facts': ['Built with red sandstone and zig-zag white marble decorations'],
                'coordinates': [27.1824, 78.0163], 'address': 'Jama Masjid Rd, Subash Bazar, Kinari Bazar, Hing ki Mandi, Mantola, Agra',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '7:00 AM', 'close': '12:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'Medium', 'rating': 4.4, 'photo_keyword': 'Jama Masjid Agra',
                'tips': ['Respect the dress code'], 'nearby': ['Agra Fort'], 'reviews': []
            },
            {
                'id': 'ram-bagh', 'name': 'Ram Bagh', 'category': 'Garden', 'tags': ['nature', 'history'],
                'description': 'The oldest Mughal garden in India.', 'history': 'Built by Emperor Babur in 1528.',
                'why_famous': 'Islamic garden layout.', 'interesting_facts': ['Babur was temporarily buried here'],
                'coordinates': [27.2066, 78.0315], 'address': 'Ram Bagh, Agra',
                'ticket': {'adult': 20, 'child': 0, 'foreign': 250, 'student': 20, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Low', 'rating': 4.1, 'photo_keyword': 'Ram Bagh Agra',
                'tips': ['Quiet place to relax'], 'nearby': ['Itimad ud Daulah'], 'reviews': []
            },
            {
                'id': 'sadar-bazaar-agra', 'name': 'Sadar Bazaar Agra', 'category': 'Market', 'tags': ['shopping', 'food'],
                'description': 'One of the most popular shopping destinations in Agra.', 'history': 'Traditional market area.',
                'why_famous': 'Leather goods, petha, and handicrafts.', 'interesting_facts': ['Located close to the Agra Cantt Railway Station'],
                'coordinates': [27.1593, 78.0062], 'address': 'Sadar Bazaar, Agra',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '11:00 AM', 'close': '11:00 PM', 'weekly_off': 'Tuesday', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.2, 'photo_keyword': 'Sadar Bazaar Agra',
                'tips': ['Try the Chaat Gali for local street food'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'mughal-heritage-walk', 'name': 'Mughal Heritage Walk', 'category': 'Activity', 'tags': ['culture', 'history'],
                'description': 'A walking tour through the historical village of Kachhpura.', 'history': 'Initiative to promote community-based tourism.',
                'why_famous': 'Discovering lesser-known monuments and local life.', 'interesting_facts': ['Offers a view of Taj Mahal from a rustic setting'],
                'coordinates': [27.1770, 78.0425], 'address': 'Kachhpura Village, Agra',
                'ticket': {'adult': 500, 'child': 250, 'foreign': 500, 'student': 500, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': 'Flexible', 'close': 'Flexible', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'Low', 'rating': 4.5, 'photo_keyword': 'Mughal Heritage Walk',
                'tips': ['Book the tour in advance'], 'nearby': ['Mehtab Bagh'], 'reviews': []
            }
        ]
    },
    'varanasi': {
        'name': 'Varanasi',
        'state': 'Uttar Pradesh',
        'tagline': 'The Spiritual Capital of India',
        'description': 'One of the world\'s oldest continually inhabited cities, located on the banks of the Ganges.',
        'coordinates': [25.3176, 82.9739],
        'best_season': 'October to March',
        'languages': ['Hindi', 'Bhojpuri', 'English'],
        'famous_food': [
            {'name': 'Banarasi Paan', 'description': 'Betel leaf filled with various sweet and flavorful ingredients.', 'where_to_eat': 'Keshri Paan Bhandar'}
        ],
        'instagram_spots': [
            {'name': 'Dashashwamedh Ghat at Sunrise', 'tip': 'Hire a boat for the best view'}
        ],
        'trip_cost': {
            'budget': {'per_day': 700, 'hotel': 300, 'food': 250, 'transport': 150},
            'standard': {'per_day': 1800, 'hotel': 900, 'food': 600, 'transport': 300},
            'luxury': {'per_day': 6000, 'hotel': 4000, 'food': 1200, 'transport': 800}
        },
        'attractions': [
            {
                'id': 'kashi-vishwanath-temple', 'name': 'Kashi Vishwanath Temple', 'category': 'Temple', 'tags': ['religion', 'history'],
                'description': 'One of the most famous Hindu temples dedicated to Lord Shiva.', 'history': 'Rebuilt in 1780 by Ahilyabai Holkar.',
                'why_famous': 'One of the twelve Jyotirlingas.', 'interesting_facts': ['The temple dome is plated with gold'],
                'coordinates': [25.3109, 83.0107], 'address': 'Lahori Tola, Varanasi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '3:00 AM', 'close': '11:00 PM', 'weekly_off': 'None', 'best_time': 'Early Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'Very High', 'rating': 4.8, 'photo_keyword': 'Kashi Vishwanath Corridor',
                'tips': ['Phones and cameras are not allowed inside'], 'nearby': ['Dashashwamedh Ghat'], 'reviews': []
            },
            {
                'id': 'ganga-aarti', 'name': 'Ganga Aarti Dashashwamedh Ghat', 'category': 'Culture', 'tags': ['religion', 'culture'],
                'description': 'A daily evening ritual on the banks of the Ganges.', 'history': 'An ancient tradition to worship the river goddess.',
                'why_famous': 'Spectacular fire ritual with chanting.', 'interesting_facts': ['Priests perform synchronized rituals with brass lamps'],
                'coordinates': [25.3065, 83.0076], 'address': 'Dashashwamedh Ghat Rd, Ghats of Varanasi, Varanasi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '6:30 PM', 'close': '7:30 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'Very High', 'rating': 4.9, 'photo_keyword': 'Ganga Aarti Varanasi',
                'tips': ['Hire a boat for the best view'], 'nearby': ['Kashi Vishwanath Temple'], 'reviews': []
            },
            {
                'id': 'manikarnika-ghat', 'name': 'Manikarnika Ghat', 'category': 'Ghat', 'tags': ['religion', 'culture'],
                'description': 'One of the holiest cremation grounds along the Ganges.', 'history': 'According to myth, Lord Shiva and Parvati bathed here.',
                'why_famous': 'The primary cremation ghat in Varanasi.', 'interesting_facts': ['Fires here have been burning constantly for centuries'],
                'coordinates': [25.3115, 83.0135], 'address': 'Ghats of Varanasi, Lahori Tola, Varanasi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Anytime', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': False, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Manikarnika Ghat',
                'tips': ['Be respectful, do not take photos of the cremations'], 'nearby': ['Kashi Vishwanath Temple'], 'reviews': []
            },
            {
                'id': 'sarnath', 'name': 'Sarnath', 'category': 'Monument', 'tags': ['history', 'religion'],
                'description': 'A place where Gautama Buddha first taught the Dharma.', 'history': 'One of the four major Buddhist pilgrimage sites.',
                'why_famous': 'Dhamek Stupa and Ashoka Pillar.', 'interesting_facts': ['The Lion Capital of Ashoka here is India\'s national emblem'],
                'coordinates': [25.3811, 83.0232], 'address': 'Sarnath, Varanasi',
                'ticket': {'adult': 25, 'child': 0, 'foreign': 300, 'student': 25, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '8:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'Dhamek Stupa Sarnath',
                'tips': ['Visit the archaeological museum'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'ramnagar-fort', 'name': 'Ramnagar Fort', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A fortification on the eastern bank of the Ganges.', 'history': 'Built in 1750 by Kashi Naresh Raja Balwant Singh.',
                'why_famous': 'Mughal-style architecture and vintage car collection.', 'interesting_facts': ['The current king of Varanasi still resides here'],
                'coordinates': [25.2694, 83.0278], 'address': 'Ramnagar, Varanasi',
                'ticket': {'adult': 20, 'child': 0, 'foreign': 150, 'student': 20, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Afternoon', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.1, 'photo_keyword': 'Ramnagar Fort Varanasi',
                'tips': ['Try the famous Lassi nearby'], 'nearby': ['Banaras Hindu University'], 'reviews': []
            },
            {
                'id': 'assi-ghat', 'name': 'Assi Ghat', 'category': 'Ghat', 'tags': ['culture', 'peace'],
                'description': 'The southernmost ghat in Varanasi.', 'history': 'A prominent bathing ghat.',
                'why_famous': 'Subah-e-Banaras morning aarti and yoga.', 'interesting_facts': ['Where the river Assi meets the Ganges'],
                'coordinates': [25.2818, 83.0062], 'address': 'Assi Ghat, Varanasi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Early Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.7, 'photo_keyword': 'Assi Ghat Morning',
                'tips': ['Attend the Subah-e-Banaras at sunrise'], 'nearby': ['Tulsi Manas Temple'], 'reviews': []
            },
            {
                'id': 'tulsi-manas-temple', 'name': 'Tulsi Manas Temple', 'category': 'Temple', 'tags': ['religion', 'history'],
                'description': 'A prominent Hindu temple dedicated to Lord Rama.', 'history': 'Constructed in 1964.',
                'why_famous': 'Verses of the Ramcharitmanas are engraved on its marble walls.', 'interesting_facts': ['Believed to be the place where Tulsidas wrote the Ramcharitmanas'],
                'coordinates': [25.2858, 82.9995], 'address': 'Sankat Mochan Rd, Durga Kund, Varanasi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '5:30 AM', 'close': '9:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.6, 'photo_keyword': 'Tulsi Manas Temple',
                'tips': ['Peaceful atmosphere compared to ghats'], 'nearby': ['Durga Temple'], 'reviews': []
            },
            {
                'id': 'durga-temple-varanasi', 'name': 'Durga Temple Varanasi', 'category': 'Temple', 'tags': ['religion', 'architecture'],
                'description': 'One of the most famous temples in the holy city of Varanasi.', 'history': 'Built in the 18th century by a Bengali Maharani.',
                'why_famous': 'Red color and large monkey population.', 'interesting_facts': ['Also known as the Monkey Temple'],
                'coordinates': [25.2866, 82.9998], 'address': 'Durga Kund Rd, Durga Kund, Varanasi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '5:00 AM', 'close': '11:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Durga Temple Varanasi',
                'tips': ['Beware of the monkeys'], 'nearby': ['Tulsi Manas Temple'], 'reviews': []
            },
            {
                'id': 'bhu', 'name': 'Banaras Hindu University', 'category': 'Attraction', 'tags': ['culture', 'education'],
                'description': 'A collegiate, central, and research university.', 'history': 'Established in 1916 by Madan Mohan Malaviya.',
                'why_famous': 'Largest residential university in Asia.', 'interesting_facts': ['Houses the New Vishwanath Temple'],
                'coordinates': [25.2677, 82.9913], 'address': 'Ajigart, Varanasi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '9:00 AM', 'close': '6:00 PM', 'weekly_off': 'Sunday', 'best_time': 'Anytime', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'BHU Campus',
                'tips': ['Visit the Bharat Kala Bhavan museum on campus'], 'nearby': ['Ramnagar Fort'], 'reviews': []
            },
            {
                'id': 'benares-ghats', 'name': 'Benares Ghats', 'category': 'Ghat', 'tags': ['culture', 'history'],
                'description': 'Riverfront steps leading to the banks of the River Ganges.', 'history': 'Built and rebuilt over centuries by various rulers.',
                'why_famous': 'The spiritual heart of Varanasi.', 'interesting_facts': ['There are 88 ghats in total'],
                'coordinates': [25.3090, 83.0090], 'address': 'River Ganges, Varanasi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Early Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.8, 'photo_keyword': 'Varanasi Ghats Boat',
                'tips': ['Take a sunrise boat ride spanning all ghats'], 'nearby': [], 'reviews': []
            }
        ]
    },
    'manali': {
        'name': 'Manali',
        'state': 'Himachal Pradesh',
        'tagline': 'Valley of the Gods',
        'description': 'A high-altitude Himalayan resort town known for backpacking and honeymooning.',
        'coordinates': [32.2396, 77.1887],
        'best_season': 'October to June',
        'languages': ['Hindi', 'English'],
        'famous_food': [
            {'name': 'Siddu', 'description': 'Local steamed bread stuffed with nuts or paste.', 'where_to_eat': 'Local stalls'}
        ],
        'instagram_spots': [
            {'name': 'Solang Valley Snow', 'tip': 'Winter months are best'}
        ],
        'trip_cost': {
            'budget': {'per_day': 1200, 'hotel': 600, 'food': 400, 'transport': 200},
            'standard': {'per_day': 3000, 'hotel': 1500, 'food': 800, 'transport': 700},
            'luxury': {'per_day': 8000, 'hotel': 5000, 'food': 1500, 'transport': 1500}
        },
        'attractions': [
            {
                'id': 'rohtang-pass', 'name': 'Rohtang Pass', 'category': 'Nature', 'tags': ['adventure', 'snow'],
                'description': 'A high mountain pass on the eastern end of the Pir Panjal Range.', 'history': 'An ancient trade route.',
                'why_famous': 'Snow activities and breathtaking landscapes.', 'interesting_facts': ['Connecting the Kullu Valley with the Lahaul and Spiti Valleys'],
                'coordinates': [32.3716, 77.2466], 'address': 'Leh Manali Highway, Himachal Pradesh',
                'ticket': {'adult': 550, 'child': 550, 'foreign': 550, 'student': 550, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '5:00 PM', 'weekly_off': 'Tuesday', 'best_time': 'Morning', 'visit_duration': '4 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Rohtang Pass Snow',
                'tips': ['Permit is required, book in advance online'], 'nearby': ['Solang Valley'], 'reviews': []
            },
            {
                'id': 'solang-valley', 'name': 'Solang Valley', 'category': 'Nature', 'tags': ['adventure', 'sports'],
                'description': 'A side valley at the top of the Kullu Valley.', 'history': 'Known for its summer and winter sport conditions.',
                'why_famous': 'Skiing, paragliding, and zorbing.', 'interesting_facts': ['Hosts winter skiing festivals'],
                'coordinates': [32.3168, 77.1578], 'address': 'Solang Valley, Manali',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 50, 'is_free': True},
                'timings': {'open': '9:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '4 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Solang Valley Paragliding',
                'tips': ['Bargain for adventure sports'], 'nearby': ['Rohtang Pass'], 'reviews': []
            },
            {
                'id': 'hadimba-devi-temple', 'name': 'Hadimba Devi Temple', 'category': 'Temple', 'tags': ['religion', 'history'],
                'description': 'An ancient cave temple dedicated to Hidimbi Devi.', 'history': 'Built in 1553.',
                'why_famous': 'Unique cedar wood architecture.', 'interesting_facts': ['Surrounded by a cedar forest called Dhungiri Van Vihar'],
                'coordinates': [32.2472, 77.1818], 'address': 'Hadimba Temple Rd, Old Manali, Manali',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '8:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Hadimba Temple',
                'tips': ['Take a photo with the yaks outside'], 'nearby': ['Old Manali'], 'reviews': []
            },
            {
                'id': 'old-manali', 'name': 'Old Manali', 'category': 'Neighborhood', 'tags': ['culture', 'food'],
                'description': 'A quaint neighborhood with traditional houses, cafes, and shops.', 'history': 'The original settlement before the modern town developed.',
                'why_famous': 'Hippie vibe, live music, and cafes.', 'interesting_facts': ['Famous for its apple orchards'],
                'coordinates': [32.2536, 77.1783], 'address': 'Old Manali, Manali',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:00 AM', 'close': '11:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Old Manali Cafes',
                'tips': ['Cafe hopping is a must'], 'nearby': ['Hadimba Devi Temple'], 'reviews': []
            },
            {
                'id': 'beas-river', 'name': 'Beas River', 'category': 'Nature', 'tags': ['nature', 'adventure'],
                'description': 'A river in north India that rises in the Himalayas.', 'history': 'Marks the eastern-most border of Alexander the Great\'s conquests.',
                'why_famous': 'River rafting and scenic beauty.', 'interesting_facts': ['Provides drinking water to millions'],
                'coordinates': [32.2415, 77.1895], 'address': 'Manali, Himachal Pradesh',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'Medium', 'rating': 4.6, 'photo_keyword': 'Beas River Manali',
                'tips': ['Enjoy riverside camping'], 'nearby': ['Vashisht Hot Springs'], 'reviews': []
            },
            {
                'id': 'jogini-falls', 'name': 'Jogini Falls', 'category': 'Nature', 'tags': ['nature', 'trekking'],
                'description': 'A beautiful waterfall situated near Vashisht Village.', 'history': 'Considered sacred by the locals.',
                'why_famous': 'Scenic trek and pristine waterfall.', 'interesting_facts': ['Trek takes about 1.5 hours from Vashisht'],
                'coordinates': [32.2741, 77.1897], 'address': 'Vashisht Village, Manali',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '6:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': False, 'parking': False},
                'crowd': 'Low', 'rating': 4.7, 'photo_keyword': 'Jogini Waterfall Trek',
                'tips': ['Wear good trekking shoes'], 'nearby': ['Vashisht Hot Springs'], 'reviews': []
            },
            {
                'id': 'naggar-castle', 'name': 'Naggar Castle', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A medieval castle built of wood and stone.', 'history': 'Built in 1460 A.D.',
                'why_famous': 'Architecture and art gallery.', 'interesting_facts': ['Used as a shooting location for the movie Jab We Met'],
                'coordinates': [32.1158, 77.1724], 'address': 'Naggar, Himachal Pradesh',
                'ticket': {'adult': 30, 'child': 0, 'foreign': 30, 'student': 30, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '7:00 AM', 'close': '10:00 PM', 'weekly_off': 'None', 'best_time': 'Afternoon', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.4, 'photo_keyword': 'Naggar Castle',
                'tips': ['Try the local food at the restaurant inside'], 'nearby': ['Roerich Art Gallery'], 'reviews': []
            },
            {
                'id': 'great-himalayan-national-park', 'name': 'Great Himalayan National Park', 'category': 'Nature', 'tags': ['nature', 'wildlife'],
                'description': 'A national park in the Kullu region.', 'history': 'Established in 1984.',
                'why_famous': 'Rich biodiversity and trekking routes.', 'interesting_facts': ['UNESCO World Heritage Site'],
                'coordinates': [31.6384, 77.3439], 'address': 'Kullu, Himachal Pradesh',
                'ticket': {'adult': 100, 'child': 50, 'foreign': 400, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Anytime', 'visit_duration': 'Full Day'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': False, 'parking': True},
                'crowd': 'Low', 'rating': 4.6, 'photo_keyword': 'Great Himalayan National Park',
                'tips': ['Requires permits for trekking'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'kullu-valley', 'name': 'Kullu Valley', 'category': 'Nature', 'tags': ['nature', 'culture'],
                'description': 'A broad open valley formed by the Beas River.', 'history': 'Known as the "Valley of the Gods".',
                'why_famous': 'Temples, beauty, and its majestic hills covered with pine and deodar forest.', 'interesting_facts': ['Famous for its Kullu shawls'],
                'coordinates': [31.9579, 77.1095], 'address': 'Kullu, Himachal Pradesh',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Daytime', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.6, 'photo_keyword': 'Kullu Valley',
                'tips': ['Buy authentic Kullu shawls here'], 'nearby': ['Naggar Castle'], 'reviews': []
            },
            {
                'id': 'vashisht-hot-springs', 'name': 'Vashisht Hot Springs', 'category': 'Nature', 'tags': ['religion', 'nature'],
                'description': 'Natural hot springs located inside the Vashisht Temple.', 'history': 'Temple dedicated to Sage Vashisht.',
                'why_famous': 'Medicinal properties of the water.', 'interesting_facts': ['Separate bathing areas for men and women'],
                'coordinates': [32.2599, 77.1895], 'address': 'Vashisht Village, Manali',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '7:00 AM', 'close': '9:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'High', 'rating': 4.2, 'photo_keyword': 'Vashisht Hot Springs',
                'tips': ['Take a dip, but be prepared for a crowd'], 'nearby': ['Jogini Falls'], 'reviews': []
            }
        ]
    },
    'kochi': {
        'name': 'Kochi',
        'state': 'Kerala',
        'tagline': 'Queen of the Arabian Sea',
        'description': 'A major port city on the south-west coast of India with a mix of colonial architecture.',
        'coordinates': [9.9312, 76.2673],
        'best_season': 'October to March',
        'languages': ['Malayalam', 'English'],
        'famous_food': [
            {'name': 'Kerala Fish Curry', 'description': 'Spicy fish curry made with coconut milk and tamarind.', 'where_to_eat': 'Fort House Restaurant'}
        ],
        'instagram_spots': [
            {'name': 'Chinese Fishing Nets', 'tip': 'Best at sunset for silhouettes'}
        ],
        'trip_cost': {
            'budget': {'per_day': 1000, 'hotel': 500, 'food': 300, 'transport': 200},
            'standard': {'per_day': 2500, 'hotel': 1200, 'food': 800, 'transport': 500},
            'luxury': {'per_day': 8000, 'hotel': 5000, 'food': 2000, 'transport': 1000}
        },
        'attractions': [
            {
                'id': 'fort-kochi', 'name': 'Fort Kochi', 'category': 'Neighborhood', 'tags': ['history', 'culture'],
                'description': 'A region in the city of Kochi known for its colonial architecture.', 'history': 'First European township in India.',
                'why_famous': 'Historical streets, art cafes, and the Kochi-Muziris Biennale.', 'interesting_facts': ['Water-bound region toward the south-west of the mainland'],
                'coordinates': [9.9658, 76.2421], 'address': 'Fort Kochi, Kochi, Kerala',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '4 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.6, 'photo_keyword': 'Fort Kochi Streets',
                'tips': ['Rent a bicycle to explore'], 'nearby': ['Chinese Fishing Nets'], 'reviews': []
            },
            {
                'id': 'chinese-fishing-nets', 'name': 'Chinese Fishing Nets', 'category': 'Culture', 'tags': ['photography', 'history'],
                'description': 'Stationary lift nets used for fishing.', 'history': 'Introduced by Chinese explorers in the 14th century.',
                'why_famous': 'Iconic symbol of Kochi.', 'interesting_facts': ['Operated by a team of up to 6 fishermen'],
                'coordinates': [9.9678, 76.2415], 'address': 'Fort Kochi Beach, Kochi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Sunset', 'visit_duration': '30 mins'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Chinese Fishing Nets Sunset',
                'tips': ['Buy fresh fish nearby and have it cooked at a shack'], 'nearby': ['St Francis Church'], 'reviews': []
            },
            {
                'id': 'mattancherry-palace', 'name': 'Mattancherry Palace', 'category': 'Museum', 'tags': ['history', 'architecture'],
                'description': 'A Portuguese palace featuring Kerala murals.', 'history': 'Built around 1555 and presented to the Raja of Kochi.',
                'why_famous': 'Also known as the Dutch Palace.', 'interesting_facts': ['Features detailed Hindu temple art murals'],
                'coordinates': [9.9583, 76.2594], 'address': 'Palace Rd, Mattancherry, Kochi',
                'ticket': {'adult': 5, 'child': 0, 'foreign': 5, 'student': 5, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:45 AM', 'close': '1:00 PM', 'weekly_off': 'Friday', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.3, 'photo_keyword': 'Mattancherry Palace',
                'tips': ['Photography inside is strictly prohibited'], 'nearby': ['Jewish Synagogue'], 'reviews': []
            },
            {
                'id': 'jewish-synagogue-mattancherry', 'name': 'Jewish Synagogue Mattancherry', 'category': 'Monument', 'tags': ['history', 'religion'],
                'description': 'The oldest active synagogue in the Commonwealth of Nations.', 'history': 'Constructed in 1568.',
                'why_famous': 'Antiques, Belgian glass chandeliers, and hand-painted floor tiles.', 'interesting_facts': ['Located in Jew Town'],
                'coordinates': [9.9575, 76.2599], 'address': 'Synagogue Ln, Jew Town, Kappalandimukku, Mattancherry, Kochi',
                'ticket': {'adult': 5, 'child': 0, 'foreign': 5, 'student': 5, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '5:00 PM', 'weekly_off': 'Friday, Saturday', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': False, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'Medium', 'rating': 4.4, 'photo_keyword': 'Jewish Synagogue Kochi',
                'tips': ['Dress code applies (shoulders and knees covered)'], 'nearby': ['Mattancherry Palace'], 'reviews': []
            },
            {
                'id': 'st-francis-church-kochi', 'name': 'St Francis Church Kochi', 'category': 'Monument', 'tags': ['history', 'religion'],
                'description': 'One of the oldest European churches in India.', 'history': 'Originally built in 1503.',
                'why_famous': 'Original burial site of explorer Vasco da Gama.', 'interesting_facts': ['His remains were moved to Lisbon 14 years later'],
                'coordinates': [9.9655, 76.2407], 'address': 'Head Post Office, Saint Francis Church Road Opp, Fort Kochi, Kochi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '7:00 AM', 'close': '6:30 PM', 'weekly_off': 'Sunday Morning', 'best_time': 'Morning', 'visit_duration': '30 mins'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'Low', 'rating': 4.2, 'photo_keyword': 'St Francis Church Kochi',
                'tips': ['Keep silent inside'], 'nearby': ['Fort Kochi Beach'], 'reviews': []
            },
            {
                'id': 'cherai-beach', 'name': 'Cherai Beach', 'category': 'Beach', 'tags': ['nature', 'family'],
                'description': 'A picturesque beach on the northern end of Vypin Island.', 'history': 'A popular swimming beach.',
                'why_famous': 'Where the sea and the backwaters meet.', 'interesting_facts': ['Dolphins are occasionally seen here'],
                'coordinates': [10.1416, 76.1783], 'address': 'Cherai, Kochi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Cherai Beach',
                'tips': ['Great for swimming'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'kerala-backwaters', 'name': 'Kerala Backwaters', 'category': 'Nature', 'tags': ['nature', 'peace'],
                'description': 'A network of brackish lagoons and lakes lying parallel to the Arabian Sea coast.', 'history': 'Used for local transport and fishing.',
                'why_famous': 'Houseboat cruises.', 'interesting_facts': ['Includes five large lakes linked by canals'],
                'coordinates': [9.9312, 76.2673], 'address': 'Various locations, Kochi',
                'ticket': {'adult': 1000, 'child': 500, 'foreign': 1000, 'student': 1000, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': 'Daylight hours', 'close': 'Evening', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2-4 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'Kerala Houseboat',
                'tips': ['Take a half-day cruise for the best experience'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'marine-drive-kochi', 'name': 'Marine Drive Kochi', 'category': 'Promenade', 'tags': ['nature', 'views'],
                'description': 'A picturesque promenade in Kochi facing the backwaters.', 'history': 'Built on land reclaimed from the sea.',
                'why_famous': 'Evening walks and sunset views.', 'interesting_facts': ['Vehicles are not allowed on the walkway'],
                'coordinates': [9.9816, 76.2750], 'address': 'Marine Drive, Kochi',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1.5 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Marine Drive Kochi Sunset',
                'tips': ['Take a quick boat ride from the jetty'], 'nearby': [], 'reviews': []
            }
        ]
    },
    'kolkata': {
        'name': 'Kolkata',
        'state': 'West Bengal',
        'tagline': 'The City of Joy',
        'description': 'Known for its grand colonial architecture, art galleries and cultural festivals.',
        'coordinates': [22.5726, 88.3639],
        'best_season': 'October to March',
        'languages': ['Bengali', 'Hindi', 'English'],
        'famous_food': [
            {'name': 'Rosogolla', 'description': 'Spongy ball-shaped dumplings of chhena and semolina dough.', 'where_to_eat': 'K.C. Das'}
        ],
        'instagram_spots': [
            {'name': 'Victoria Memorial', 'tip': 'Best photographed in the evening lights'}
        ],
        'trip_cost': {
            'budget': {'per_day': 800, 'hotel': 400, 'food': 300, 'transport': 100},
            'standard': {'per_day': 2200, 'hotel': 1200, 'food': 700, 'transport': 300},
            'luxury': {'per_day': 7000, 'hotel': 4500, 'food': 1800, 'transport': 700}
        },
        'attractions': [
            {
                'id': 'victoria-memorial', 'name': 'Victoria Memorial', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A large marble building dedicated to the memory of Queen Victoria.', 'history': 'Built between 1906 and 1921.',
                'why_famous': 'Iconic monument and museum.', 'interesting_facts': ['Built of the same Makrana marble as the Taj Mahal'],
                'coordinates': [22.5448, 88.3426], 'address': 'Victoria Memorial Hall, 1, Queens Way, Maidan, Kolkata',
                'ticket': {'adult': 30, 'child': 10, 'foreign': 200, 'student': 10, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '5:00 PM', 'weekly_off': 'Monday', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.7, 'photo_keyword': 'Victoria Memorial',
                'tips': ['Enjoy the light and sound show in the evening'], 'nearby': ['Maidan'], 'reviews': []
            },
            {
                'id': 'howrah-bridge', 'name': 'Howrah Bridge', 'category': 'Architecture', 'tags': ['architecture', 'photography'],
                'description': 'A balanced cantilever bridge over the Hooghly River.', 'history': 'Commissioned in 1943.',
                'why_famous': 'Busiest cantilever bridge in the world.', 'interesting_facts': ['Built without a single nut or bolt'],
                'coordinates': [22.5851, 88.3468], 'address': 'Howrah Bridge, Kolkata',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Night', 'visit_duration': '30 mins'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'Very High', 'rating': 4.6, 'photo_keyword': 'Howrah Bridge Night',
                'tips': ['Take a ferry for the best views of the bridge'], 'nearby': ['Mullick Ghat Flower Market'], 'reviews': []
            },
            {
                'id': 'dakshineswar-kali-temple', 'name': 'Dakshineswar Kali Temple', 'category': 'Temple', 'tags': ['religion', 'history'],
                'description': 'A Hindu navaratna temple situated on the eastern bank of the Hooghly River.', 'history': 'Built in 1855 by Rani Rashmoni.',
                'why_famous': 'Association with Ramakrishna Paramahamsa.', 'interesting_facts': ['Features 12 shrines to Shiva'],
                'coordinates': [22.6534, 88.3576], 'address': 'Dakshineswar, Kolkata',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '6:00 AM', 'close': '8:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.8, 'photo_keyword': 'Dakshineswar Kali Temple',
                'tips': ['Combine with a visit to Belur Math by boat'], 'nearby': ['Belur Math'], 'reviews': []
            },
            {
                'id': 'park-street', 'name': 'Park Street', 'category': 'Neighborhood', 'tags': ['food', 'nightlife'],
                'description': 'A famous thoroughfare known as the "Food Street" of Kolkata.', 'history': 'Known for its nightlife since the 1940s.',
                'why_famous': 'Iconic restaurants like Peter Cat and Flurys.', 'interesting_facts': ['Renamed to Mother Teresa Sarani'],
                'coordinates': [22.5516, 88.3524], 'address': 'Park Street, Kolkata',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:00 AM', 'close': '11:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Park Street Kolkata',
                'tips': ['Try the Chelo Kebab at Peter Cat'], 'nearby': ['Indian Museum'], 'reviews': []
            },
            {
                'id': 'college-street', 'name': 'College Street', 'category': 'Market', 'tags': ['books', 'culture'],
                'description': 'A street famous for its small and big book stores.', 'history': 'Historically the center of Kolkata\'s literary crowd.',
                'why_famous': 'Largest second-hand book market in the world.', 'interesting_facts': ['Home to the famous Indian Coffee House'],
                'coordinates': [22.5756, 88.3631], 'address': 'College Street, Kolkata',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:00 AM', 'close': '8:00 PM', 'weekly_off': 'Sunday', 'best_time': 'Afternoon', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'College Street Books',
                'tips': ['Bargaining is possible'], 'nearby': ['Presidency University'], 'reviews': []
            },
            {
                'id': 'indian-museum-kolkata', 'name': 'Indian Museum Kolkata', 'category': 'Museum', 'tags': ['history', 'art'],
                'description': 'The largest and oldest museum in India.', 'history': 'Founded in 1814.',
                'why_famous': 'Rare collections of antiques, armor, and mummies.', 'interesting_facts': ['It is the ninth oldest regular museum of the world'],
                'coordinates': [22.5579, 88.3514], 'address': '27, Jawaharlal Nehru Rd, Fire Brigade Head Quarter, New Market Area, Dharmatala, Kolkata',
                'ticket': {'adult': 50, 'child': 20, 'foreign': 500, 'student': 50, 'camera': 50, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '5:00 PM', 'weekly_off': 'Monday', 'best_time': 'Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.4, 'photo_keyword': 'Indian Museum Kolkata',
                'tips': ['Don\'t miss the Egyptian mummy'], 'nearby': ['Park Street'], 'reviews': []
            },
            {
                'id': 'kalighat-temple', 'name': 'Kalighat Temple', 'category': 'Temple', 'tags': ['religion'],
                'description': 'A Hindu temple dedicated to the goddess Kali.', 'history': 'The current structure is about 200 years old.',
                'why_famous': 'One of the 51 Shakti Peethas.', 'interesting_facts': ['The name Calcutta is said to have been derived from Kalighat'],
                'coordinates': [22.5204, 88.3416], 'address': 'Kalighat, Kolkata',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '5:00 AM', 'close': '10:30 PM', 'weekly_off': 'None', 'best_time': 'Early Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'Very High', 'rating': 4.5, 'photo_keyword': 'Kalighat Temple',
                'tips': ['Beware of aggressive touts'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'eden-gardens', 'name': 'Eden Gardens', 'category': 'Sports', 'tags': ['sports', 'history'],
                'description': 'A cricket ground in Kolkata.', 'history': 'Established in 1864.',
                'why_famous': 'Oldest and second-largest cricket stadium in India.', 'interesting_facts': ['Often referred to as the "Mecca of Indian cricket"'],
                'coordinates': [22.5646, 88.3433], 'address': 'B.B.D. Bagh, Kolkata',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '9:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Anytime', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.6, 'photo_keyword': 'Eden Gardens Stadium',
                'tips': ['Entry might be restricted when there are no matches'], 'nearby': ['Maidan'], 'reviews': []
            },
            {
                'id': 'science-city-kolkata', 'name': 'Science City Kolkata', 'category': 'Museum', 'tags': ['science', 'family'],
                'description': 'The largest science centre in the Indian subcontinent.', 'history': 'Opened in 1997.',
                'why_famous': 'Interactive exhibits, Space Odyssey, and Evolution Park.', 'interesting_facts': ['Managed by the National Council of Science Museums'],
                'coordinates': [22.5385, 88.3956], 'address': 'J.B.S Haldane Avenue, Kolkata',
                'ticket': {'adult': 60, 'child': 60, 'foreign': 60, 'student': 60, 'camera': 0, 'parking': 50, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '8:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '4 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Science City Kolkata',
                'tips': ['Great for kids and families'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'kumartuli', 'name': 'Kumartuli', 'category': 'Neighborhood', 'tags': ['art', 'culture'],
                'description': 'A traditional potters\' quarter in northern Kolkata.', 'history': 'Renowned for its sculpting prowess since the settlement began.',
                'why_famous': 'Idol making for festivals like Durga Puja.', 'interesting_facts': ['Idols are exported all over the world'],
                'coordinates': [22.5999, 88.3619], 'address': 'Kumartuli, Kolkata',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Before Durga Puja (Sept/Oct)', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Kumartuli Idols',
                'tips': ['Photographers might be charged a small fee by artisans'], 'nearby': [], 'reviews': []
            }
        ]
    },
    'hyderabad': {
        'name': 'Hyderabad',
        'state': 'Telangana',
        'tagline': 'City of Pearls',
        'description': 'Famous for its historic sites, pearls, and the delectable Hyderabadi Biryani.',
        'coordinates': [17.3850, 78.4867],
        'best_season': 'October to March',
        'languages': ['Telugu', 'Urdu', 'English'],
        'famous_food': [
            {'name': 'Hyderabadi Biryani', 'description': 'Flavorful rice dish cooked with meat and spices.', 'where_to_eat': 'Paradise Biryani'}
        ],
        'instagram_spots': [
            {'name': 'Charminar', 'tip': 'Best at night when illuminated'}
        ],
        'trip_cost': {
            'budget': {'per_day': 900, 'hotel': 500, 'food': 300, 'transport': 100},
            'standard': {'per_day': 2500, 'hotel': 1300, 'food': 800, 'transport': 400},
            'luxury': {'per_day': 8000, 'hotel': 5000, 'food': 2000, 'transport': 1000}
        },
        'attractions': [
            {
                'id': 'charminar', 'name': 'Charminar', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A monument and mosque located in Hyderabad.', 'history': 'Constructed in 1591 by Muhammad Quli Qutb Shah.',
                'why_famous': 'Global icon of Hyderabad.', 'interesting_facts': ['Built to celebrate the end of a deadly plague'],
                'coordinates': [17.3616, 78.4747], 'address': 'Charminar Rd, Char Kaman, Ghansi Bazaar, Hyderabad',
                'ticket': {'adult': 25, 'child': 0, 'foreign': 300, 'student': 25, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:30 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'Very High', 'rating': 4.6, 'photo_keyword': 'Charminar',
                'tips': ['Shop at Laad Bazaar nearby'], 'nearby': ['Laad Bazaar', 'Mecca Masjid'], 'reviews': []
            },
            {
                'id': 'golconda-fort', 'name': 'Golconda Fort', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A fortified citadel and an early capital city of the Qutb Shahi dynasty.', 'history': 'Originally built by Kakatiya ruler in the 11th century.',
                'why_famous': 'Acoustic effects and massive structure.', 'interesting_facts': ['The famous Hope diamond was found in its mines'],
                'coordinates': [17.3833, 78.4011], 'address': 'Khair Complex, Ibrahim Bagh, Hyderabad',
                'ticket': {'adult': 25, 'child': 0, 'foreign': 200, 'student': 25, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.7, 'photo_keyword': 'Golconda Fort',
                'tips': ['Clap at the entrance to hear the echo at the top'], 'nearby': ['Qutb Shahi Tombs'], 'reviews': []
            },
            {
                'id': 'ramoji-film-city', 'name': 'Ramoji Film City', 'category': 'Entertainment', 'tags': ['family', 'cinema'],
                'description': 'An integrated film studio facility.', 'history': 'Set up by Ramoji Group in 1996.',
                'why_famous': 'Largest studio complex in the world.', 'interesting_facts': ['Holds Guinness World Record for the largest film studio complex'],
                'coordinates': [17.2543, 78.6808], 'address': 'Ramoji Film City Main Road, Hyderabad',
                'ticket': {'adult': 1250, 'child': 1050, 'foreign': 1250, 'student': 1250, 'camera': 0, 'parking': 50, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Full Day', 'visit_duration': '8 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Ramoji Film City',
                'tips': ['Takes a full day to explore'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'hussain-sagar', 'name': 'Hussain Sagar Lake', 'category': 'Nature', 'tags': ['nature', 'boating'],
                'description': 'A heart-shaped lake in Hyderabad built by Ibrahim Quli Qutb Shah.', 'history': 'Excavated in 1562.',
                'why_famous': 'Large monolithic statue of Gautama Buddha in the middle.', 'interesting_facts': ['Connects Hyderabad and Secunderabad'],
                'coordinates': [17.4239, 78.4738], 'address': 'Hussain Sagar, Hyderabad',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '8:00 AM', 'close': '10:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Hussain Sagar Buddha',
                'tips': ['Take a boat ride to the Buddha statue'], 'nearby': ['Lumbini Park'], 'reviews': []
            },
            {
                'id': 'salar-jung-museum', 'name': 'Salar Jung Museum', 'category': 'Museum', 'tags': ['history', 'art'],
                'description': 'An art museum located at Dar-ul-Shifa.', 'history': 'Established in 1951.',
                'why_famous': 'One of the largest collections of antiques by a single person.', 'interesting_facts': ['Features the famous Veiled Rebecca statue'],
                'coordinates': [17.3714, 78.4804], 'address': 'Salar Jung Rd, Darulshifa, Hyderabad',
                'ticket': {'adult': 50, 'child': 20, 'foreign': 500, 'student': 50, 'camera': 50, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '5:00 PM', 'weekly_off': 'Friday', 'best_time': 'Anytime', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Salar Jung Museum',
                'tips': ['Look out for the musical clock'], 'nearby': ['Charminar'], 'reviews': []
            },
            {
                'id': 'qutb-shahi-tombs', 'name': 'Qutb Shahi Tombs', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'Tombs of the seven Qutb Shahi rulers.', 'history': 'Built during the 16th and 17th centuries.',
                'why_famous': 'Blend of Persian, Pashtun and Hindu architectural styles.', 'interesting_facts': ['Only place in the world where an entire dynasty is buried at one place'],
                'coordinates': [17.3949, 78.3968], 'address': 'Fort Rd, Toli Chowki, Hyderabad',
                'ticket': {'adult': 10, 'child': 5, 'foreign': 100, 'student': 10, 'camera': 20, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:30 AM', 'close': '4:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1.5 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Low', 'rating': 4.4, 'photo_keyword': 'Qutb Shahi Tombs',
                'tips': ['Peaceful spot away from the city noise'], 'nearby': ['Golconda Fort'], 'reviews': []
            },
            {
                'id': 'laad-bazaar', 'name': 'Laad Bazaar', 'category': 'Market', 'tags': ['shopping', 'culture'],
                'description': 'A very old market popular for bangles.', 'history': 'Operating since the time of the Qutb Shahis.',
                'why_famous': 'Lacquer bangles studded with artificial diamonds.', 'interesting_facts': ['Located adjacent to the Charminar'],
                'coordinates': [17.3616, 78.4740], 'address': 'Charminar, Hyderabad',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '11:00 AM', 'close': '11:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'Very High', 'rating': 4.3, 'photo_keyword': 'Laad Bazaar Bangles',
                'tips': ['Bargaining is essential'], 'nearby': ['Charminar'], 'reviews': []
            },
            {
                'id': 'birla-mandir-hyderabad', 'name': 'Birla Mandir Hyderabad', 'category': 'Temple', 'tags': ['religion', 'architecture'],
                'description': 'A Hindu temple built on a 280 feet high hillock.', 'history': 'Constructed in 1976 by the Birla Foundation.',
                'why_famous': 'Made entirely of white marble.', 'interesting_facts': ['Does not have traditional bells to maintain peace'],
                'coordinates': [17.4062, 78.4691], 'address': 'Hill Fort Rd, Ambedkar Colony, Khairtabad, Hyderabad',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '7:00 AM', 'close': '9:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': False, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.7, 'photo_keyword': 'Birla Mandir Hyderabad',
                'tips': ['Offers great panoramic views of the city'], 'nearby': ['Hussain Sagar Lake'], 'reviews': []
            }
        ]
    },
    'chennai': {
        'name': 'Chennai',
        'state': 'Tamil Nadu',
        'tagline': 'The Detroit of India',
        'description': 'A major cultural and economic center in South India, known for its temples and beaches.',
        'coordinates': [13.0827, 80.2707],
        'best_season': 'November to February',
        'languages': ['Tamil', 'English'],
        'famous_food': [
            {'name': 'Idli and Sambar', 'description': 'Steamed rice cakes served with lentil stew.', 'where_to_eat': 'Murugan Idli Shop'}
        ],
        'instagram_spots': [
            {'name': 'Kapaleeshwarar Temple', 'tip': 'Capture the vibrant gopuram'}
        ],
        'trip_cost': {
            'budget': {'per_day': 900, 'hotel': 500, 'food': 300, 'transport': 100},
            'standard': {'per_day': 2500, 'hotel': 1300, 'food': 800, 'transport': 400},
            'luxury': {'per_day': 8000, 'hotel': 5000, 'food': 2000, 'transport': 1000}
        },
        'attractions': [
            {
                'id': 'marina-beach', 'name': 'Marina Beach', 'category': 'Beach', 'tags': ['nature', 'family'],
                'description': 'A natural urban beach along the Bay of Bengal.', 'history': 'One of the longest urban beaches in the world.',
                'why_famous': 'Its long stretch of sand and statues.', 'interesting_facts': ['Bathing and swimming are illegal due to strong undercurrents'],
                'coordinates': [13.0500, 80.2824], 'address': 'Marina Beach, Chennai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Sunrise', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Marina Beach Chennai',
                'tips': ['Try the local beach snacks'], 'nearby': ['San Thome Basilica'], 'reviews': []
            },
            {
                'id': 'kapaleeshwarar-temple', 'name': 'Kapaleeshwarar Temple', 'category': 'Temple', 'tags': ['religion', 'architecture'],
                'description': 'A Hindu temple dedicated to Shiva located in Mylapore.', 'history': 'Built around the 7th century CE in Dravidian architecture.',
                'why_famous': 'Stunning colorful gopuram (gateway tower).', 'interesting_facts': ['Parvati worshipped Shiva in the form of a peacock here'],
                'coordinates': [13.0335, 80.2687], 'address': 'Kapaleesvarar Sannadhi St, Vinayaka Nagar Colony, Mylapore, Chennai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '5:00 AM', 'close': '9:00 PM', 'weekly_off': 'None', 'best_time': 'Early Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'High', 'rating': 4.8, 'photo_keyword': 'Kapaleeshwarar Temple',
                'tips': ['Dress traditionally'], 'nearby': ['Mylapore Market'], 'reviews': []
            },
            {
                'id': 'fort-st-george', 'name': 'Fort St George', 'category': 'Monument', 'tags': ['history'],
                'description': 'The first English fortress in India.', 'history': 'Founded in 1644 at the coastal city of Madras.',
                'why_famous': 'Currently houses the Tamil Nadu legislative assembly.', 'interesting_facts': ['The museum has a large collection of British era artifacts'],
                'coordinates': [13.0805, 80.2776], 'address': 'Rajaji Rd, Fort St George, Chennai',
                'ticket': {'adult': 15, 'child': 0, 'foreign': 200, 'student': 15, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '5:00 PM', 'weekly_off': 'Friday', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.3, 'photo_keyword': 'Fort St George Chennai',
                'tips': ['Carry a valid ID proof'], 'nearby': ['High Court'], 'reviews': []
            },
            {
                'id': 'government-museum-chennai', 'name': 'Government Museum Chennai', 'category': 'Museum', 'tags': ['history', 'art'],
                'description': 'A museum of human history and culture.', 'history': 'Started in 1851, it is the second oldest museum in India.',
                'why_famous': 'Greatest collection of bronze idols in the world.', 'interesting_facts': ['Built in Indo-Saracenic style'],
                'coordinates': [13.0732, 80.2572], 'address': 'Pantheon Rd, Egmore, Chennai',
                'ticket': {'adult': 15, 'child': 10, 'foreign': 250, 'student': 10, 'camera': 200, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:30 AM', 'close': '5:00 PM', 'weekly_off': 'Friday', 'best_time': 'Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.4, 'photo_keyword': 'Government Museum Chennai',
                'tips': ['The bronze gallery is a must-visit'], 'nearby': ['Connemara Public Library'], 'reviews': []
            },
            {
                'id': 'valluvar-kottam', 'name': 'Valluvar Kottam', 'category': 'Monument', 'tags': ['culture', 'architecture'],
                'description': 'A monument dedicated to the classical Tamil poet-philosopher Valluvar.', 'history': 'Completed in 1976.',
                'why_famous': 'Looks like a temple chariot.', 'interesting_facts': ['All 1,330 couplets of Tirukkural are inscribed here'],
                'coordinates': [13.0538, 80.2404], 'address': 'Valluvar Kottam High Rd, Nungambakkam, Chennai',
                'ticket': {'adult': 10, 'child': 5, 'foreign': 10, 'student': 5, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '8:30 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.2, 'photo_keyword': 'Valluvar Kottam',
                'tips': ['Often hosts handloom exhibitions'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'birla-planetarium-chennai', 'name': 'Birla Planetarium Chennai', 'category': 'Science', 'tags': ['science', 'family'],
                'description': 'A large planetarium providing virtual tours of the night sky.', 'history': 'Built in 1983.',
                'why_famous': 'Shows on astronomy.', 'interesting_facts': ['Located at Periyar Science and Technology Centre'],
                'coordinates': [13.0076, 80.2372], 'address': 'Gandhi Mandapam Rd, Kotturpuram, Chennai',
                'ticket': {'adult': 30, 'child': 15, 'foreign': 30, 'student': 15, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '5:45 PM', 'weekly_off': 'None', 'best_time': 'Anytime', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.1, 'photo_keyword': 'Birla Planetarium Chennai',
                'tips': ['Check show timings before visiting'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'elliots-beach', 'name': 'Elliot Beach', 'category': 'Beach', 'tags': ['nature', 'food'],
                'description': 'A popular beach in Besant Nagar.', 'history': 'Named after Edward Elliot, Governor of Madras.',
                'why_famous': 'Cleaner and less crowded than Marina beach.', 'interesting_facts': ['Contains the Karl Schmidt Memorial'],
                'coordinates': [13.0003, 80.2733], 'address': 'Besant Nagar, Chennai',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Elliot Beach',
                'tips': ['Great cafes and restaurants nearby'], 'nearby': ['Ashtalakshmi Temple'], 'reviews': []
            }
        ]
    },
    'bangalore': {
        'name': 'Bangalore',
        'state': 'Karnataka',
        'tagline': 'Silicon Valley of India',
        'description': 'India\'s tech hub, known for its pleasant weather and parks.',
        'coordinates': [12.9716, 77.5946],
        'best_season': 'September to February',
        'languages': ['Kannada', 'English', 'Hindi'],
        'famous_food': [
            {'name': 'Bisi Bele Bath', 'description': 'Spicy rice based dish with lentils and vegetables.', 'where_to_eat': 'MTR'}
        ],
        'instagram_spots': [
            {'name': 'Bangalore Palace', 'tip': 'The grand wooden interiors'}
        ],
        'trip_cost': {
            'budget': {'per_day': 1000, 'hotel': 500, 'food': 300, 'transport': 200},
            'standard': {'per_day': 3000, 'hotel': 1500, 'food': 900, 'transport': 600},
            'luxury': {'per_day': 9000, 'hotel': 5500, 'food': 2500, 'transport': 1000}
        },
        'attractions': [
            {
                'id': 'lalbagh-botanical-garden', 'name': 'Lalbagh Botanical Garden', 'category': 'Nature', 'tags': ['nature', 'peace'],
                'description': 'An old botanical garden in Bengaluru.', 'history': 'Commissioned by Hyder Ali in 1760.',
                'why_famous': 'Glass House inspired by London\'s Crystal Palace.', 'interesting_facts': ['Has India\'s largest collection of tropical plants'],
                'coordinates': [12.9507, 77.5848], 'address': 'Mavalli, Bangalore',
                'ticket': {'adult': 25, 'child': 0, 'foreign': 25, 'student': 25, 'camera': 50, 'parking': 0, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '7:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Lalbagh Glass House',
                'tips': ['Flower shows during Republic Day and Independence Day'], 'nearby': ['Cubbon Park'], 'reviews': []
            },
            {
                'id': 'cubbon-park', 'name': 'Cubbon Park', 'category': 'Nature', 'tags': ['nature', 'parks'],
                'description': 'A landmark lung space of the Bengaluru city.', 'history': 'Created in 1870.',
                'why_famous': 'Abundant flora and historical buildings.', 'interesting_facts': ['Spread over 300 acres'],
                'coordinates': [12.9779, 77.5952], 'address': 'Kasturba Road, Sampangi Rama Nagara, Bangalore',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '6:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Cubbon Park',
                'tips': ['Vehicles are banned on Sundays'], 'nearby': ['Vidhana Soudha'], 'reviews': []
            },
            {
                'id': 'iskcon-temple-bangalore', 'name': 'ISKCON Temple Bangalore', 'category': 'Temple', 'tags': ['religion', 'peace'],
                'description': 'A huge cultural complex accommodating a temple dedicated to Krishna.', 'history': 'Inaugurated in 1997.',
                'why_famous': 'One of the largest ISKCON temples in the world.', 'interesting_facts': ['Has a gold-plated flag post'],
                'coordinates': [13.0098, 77.5511], 'address': 'Hare Krishna Hill, Chord Rd, Rajajinagar, Bangalore',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '4:15 AM', 'close': '8:30 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.7, 'photo_keyword': 'ISKCON Temple Bangalore',
                'tips': ['Try the free prasadam'], 'nearby': ['Orion Mall'], 'reviews': []
            },
            {
                'id': 'vidhana-soudha', 'name': 'Vidhana Soudha', 'category': 'Architecture', 'tags': ['architecture', 'government'],
                'description': 'The seat of the state legislature of Karnataka.', 'history': 'Completed in 1956.',
                'why_famous': 'Imposing Neo-Dravidian architecture.', 'interesting_facts': ['Largest legislative building in India'],
                'coordinates': [12.9796, 77.5906], 'address': 'Ambedkar Veedhi, Sampangi Rama Nagara, Bangalore',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '9:00 AM', 'close': '5:00 PM', 'weekly_off': 'Sunday', 'best_time': 'Evening', 'visit_duration': '30 mins'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': False, 'parking': False},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Vidhana Soudha',
                'tips': ['Illuminated on Sunday evenings'], 'nearby': ['Cubbon Park'], 'reviews': []
            },
            {
                'id': 'tipu-sultan-summer-palace', 'name': 'Tipu Sultan Summer Palace', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'An example of Indo-Islamic architecture.', 'history': 'Completed in 1791.',
                'why_famous': 'Built entirely of teak wood.', 'interesting_facts': ['Served as the summer residence of the ruler'],
                'coordinates': [12.9621, 77.5738], 'address': 'Albert Victor Road, Chamrajpet, Bangalore',
                'ticket': {'adult': 15, 'child': 0, 'foreign': 200, 'student': 15, 'camera': 25, 'parking': 0, 'is_free': False},
                'timings': {'open': '8:30 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'Medium', 'rating': 4.1, 'photo_keyword': 'Tipu Sultan Palace',
                'tips': ['A small museum details Tipu Sultan\'s life'], 'nearby': ['K.R. Market'], 'reviews': []
            },
            {
                'id': 'bangalore-palace', 'name': 'Bangalore Palace', 'category': 'Monument', 'tags': ['architecture', 'history'],
                'description': 'A royal palace in Tudor Revival style architecture.', 'history': 'Construction began in 1874.',
                'why_famous': 'Looks like Windsor Castle in England.', 'interesting_facts': ['Hosts many rock concerts and events'],
                'coordinates': [12.9988, 77.5921], 'address': 'Vasanth Nagar, Bangalore',
                'ticket': {'adult': 230, 'child': 0, 'foreign': 460, 'student': 230, 'camera': 685, 'parking': 0, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.3, 'photo_keyword': 'Bangalore Palace',
                'tips': ['Audio guide is highly recommended'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'commercial-street', 'name': 'Commercial Street', 'category': 'Market', 'tags': ['shopping', 'food'],
                'description': 'One of the oldest and busiest shopping areas of the city.', 'history': 'A prominent commercial hub.',
                'why_famous': 'Clothes, jewelry, and electronics.', 'interesting_facts': ['A maze of small lanes branching off the main street'],
                'coordinates': [12.9822, 77.6083], 'address': 'Tasker Town, Shivaji Nagar, Bangalore',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '10:30 AM', 'close': '9:30 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'Very High', 'rating': 4.4, 'photo_keyword': 'Commercial Street Bangalore',
                'tips': ['Parking is difficult, use public transport'], 'nearby': ['MG Road'], 'reviews': []
            }
        ]
    },
    'rishikesh': {
        'name': 'Rishikesh',
        'state': 'Uttarakhand',
        'tagline': 'Yoga Capital of the World',
        'description': 'A city in the Himalayan foothills beside the Ganges River.',
        'coordinates': [30.0869, 78.2676],
        'best_season': 'September to November, February to May',
        'languages': ['Hindi', 'English'],
        'famous_food': [
            {'name': 'Aloo Puri', 'description': 'Deep fried bread served with potato curry.', 'where_to_eat': 'Chotiwala'}
        ],
        'instagram_spots': [
            {'name': 'Laxman Jhula', 'tip': 'View from the middle of the bridge'}
        ],
        'trip_cost': {
            'budget': {'per_day': 800, 'hotel': 400, 'food': 300, 'transport': 100},
            'standard': {'per_day': 2200, 'hotel': 1200, 'food': 600, 'transport': 400},
            'luxury': {'per_day': 6000, 'hotel': 4000, 'food': 1200, 'transport': 800}
        },
        'attractions': [
            {
                'id': 'laxman-jhula', 'name': 'Laxman Jhula', 'category': 'Architecture', 'tags': ['views', 'history'],
                'description': 'An iron suspension bridge across the river Ganges.', 'history': 'Built in 1929.',
                'why_famous': 'According to mythology, Lakshmana crossed the Ganges on jute ropes where the bridge is built.', 'interesting_facts': ['It is a pedestrian and motor-bike bridge'],
                'coordinates': [30.1221, 78.3283], 'address': 'Tapovan, Rishikesh',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Laxman Jhula',
                'tips': ['Currently restricted for two-wheelers and large crowds for safety'], 'nearby': ['Tera Manzil Temple'], 'reviews': []
            },
            {
                'id': 'ram-jhula', 'name': 'Ram Jhula', 'category': 'Architecture', 'tags': ['views', 'peace'],
                'description': 'An iron suspension bridge across the river Ganges.', 'history': 'Built in 1986.',
                'why_famous': 'Connects Sivananda Ashram and Swargashram.', 'interesting_facts': ['Bigger than Laxman Jhula'],
                'coordinates': [30.1082, 78.3150], 'address': 'Swarg Ashram, Rishikesh',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': False},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Ram Jhula',
                'tips': ['Visit the ashrams on either side'], 'nearby': ['Beatles Ashram'], 'reviews': []
            },
            {
                'id': 'triveni-ghat', 'name': 'Triveni Ghat', 'category': 'Ghat', 'tags': ['religion', 'culture'],
                'description': 'The biggest and most famous ghat in Rishikesh.', 'history': 'Believed to be the confluence of three holy rivers.',
                'why_famous': 'Maha Aarti performed every evening.', 'interesting_facts': ['A dip here is believed to wash away all sins'],
                'coordinates': [30.1030, 78.2982], 'address': 'Mayakund, Rishikesh',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '24 Hours', 'close': '24 Hours', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.7, 'photo_keyword': 'Triveni Ghat Aarti',
                'tips': ['Must attend the evening Ganga Aarti'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'beatles-ashram', 'name': 'Beatles Ashram', 'category': 'Monument', 'tags': ['history', 'art'],
                'description': 'The ashram where the Beatles stayed in 1968.', 'history': 'Originally the ashram of Maharishi Mahesh Yogi.',
                'why_famous': 'Beatles wrote many songs of the White Album here.', 'interesting_facts': ['Now famous for graffiti art on its walls'],
                'coordinates': [30.1042, 78.3188], 'address': 'Swarg Ashram, Rishikesh',
                'ticket': {'adult': 150, 'child': 0, 'foreign': 600, 'student': 150, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:00 AM', 'close': '4:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': False},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Beatles Ashram Graffiti',
                'tips': ['Great for photography and meditation'], 'nearby': ['Ram Jhula'], 'reviews': []
            },
            {
                'id': 'rajaji-national-park', 'name': 'Rajaji National Park', 'category': 'Nature', 'tags': ['nature', 'wildlife'],
                'description': 'An Indian national park and tiger reserve.', 'history': 'Created in 1983.',
                'why_famous': 'Elephants and tigers.', 'interesting_facts': ['Named after C. Rajagopalachari'],
                'coordinates': [29.9701, 78.1724], 'address': 'Ansari Road, Mohand Range, Uttarakhand',
                'ticket': {'adult': 150, 'child': 150, 'foreign': 600, 'student': 150, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '6:00 AM', 'close': '5:00 PM', 'weekly_off': 'Monsoon (July-Nov)', 'best_time': 'Morning', 'visit_duration': '4 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Low', 'rating': 4.2, 'photo_keyword': 'Rajaji National Park',
                'tips': ['Take a jeep safari'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'neelkanth-mahadev-temple', 'name': 'Neelkanth Mahadev Temple', 'category': 'Temple', 'tags': ['religion', 'nature'],
                'description': 'A Hindu temple dedicated to Nilkanth, an aspect of Shiva.', 'history': 'A prominent pilgrimage site.',
                'why_famous': 'According to myth, this is the place where Shiva consumed the poison from Samudra Manthan.', 'interesting_facts': ['Located amidst dense forests'],
                'coordinates': [30.0818, 78.3615], 'address': 'Kotdwar - Pauri Rd, Kotdwara, Uttarakhand',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '5:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Neelkanth Mahadev',
                'tips': ['Trek from Rishikesh is an option for adventure seekers'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'bungee-jumping-rishikesh', 'name': 'Bungee Jumping Rishikesh', 'category': 'Adventure', 'tags': ['adventure', 'sports'],
                'description': 'India\'s highest bungee jumping platform.', 'history': 'Set up by Jumpin Heights.',
                'why_famous': '83 meters high jump.', 'interesting_facts': ['Designed by experts from New Zealand'],
                'coordinates': [30.1270, 78.3496], 'address': 'Mohanchatti, Rishikesh',
                'ticket': {'adult': 3550, 'child': 3550, 'foreign': 3550, 'student': 3550, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '9:30 AM', 'close': '3:30 PM', 'weekly_off': 'Tuesday', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.7, 'photo_keyword': 'Bungee Jumping Rishikesh',
                'tips': ['Book in advance online'], 'nearby': [], 'reviews': []
            }
        ]
    },
    'darjeeling': {
        'name': 'Darjeeling',
        'state': 'West Bengal',
        'tagline': 'Queen of the Hills',
        'description': 'Famous for its tea industry and scenic views of the Kanchenjunga.',
        'coordinates': [27.0360, 88.2627],
        'best_season': 'March to May, October to November',
        'languages': ['Nepali', 'Bengali', 'English'],
        'famous_food': [
            {'name': 'Momos', 'description': 'Steamed dumplings filled with meat or vegetables.', 'where_to_eat': 'Kunga Restaurant'}
        ],
        'instagram_spots': [
            {'name': 'Tiger Hill', 'tip': 'Catch the first ray of sun hitting Kanchenjunga'}
        ],
        'trip_cost': {
            'budget': {'per_day': 1200, 'hotel': 700, 'food': 300, 'transport': 200},
            'standard': {'per_day': 3000, 'hotel': 1800, 'food': 700, 'transport': 500},
            'luxury': {'per_day': 8000, 'hotel': 5000, 'food': 1500, 'transport': 1500}
        },
        'attractions': [
            {
                'id': 'tiger-hill', 'name': 'Tiger Hill Sunrise', 'category': 'Nature', 'tags': ['views', 'nature'],
                'description': 'The summit of Ghoom, the highest railway station in the Darjeeling Himalayan Railway.', 'history': 'A famous sunrise viewpoint.',
                'why_famous': 'Panoramic views of Mount Everest and Kanchenjunga.', 'interesting_facts': ['Must wake up at 3 AM to catch the sunrise'],
                'coordinates': [26.9959, 88.2801], 'address': 'Senchal Forest, Darjeeling',
                'ticket': {'adult': 50, 'child': 0, 'foreign': 50, 'student': 50, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '4:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Early Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'Very High', 'rating': 4.6, 'photo_keyword': 'Tiger Hill Sunrise',
                'tips': ['Dress warmly as it gets very cold'], 'nearby': ['Batasia Loop'], 'reviews': []
            },
            {
                'id': 'darjeeling-himalayan-railway', 'name': 'Darjeeling Himalayan Railway', 'category': 'Attraction', 'tags': ['history', 'views'],
                'description': 'A 2 ft gauge railway that runs between New Jalpaiguri and Darjeeling.', 'history': 'Built between 1879 and 1881.',
                'why_famous': 'The "Toy Train".', 'interesting_facts': ['UNESCO World Heritage Site'],
                'coordinates': [27.0345, 88.2618], 'address': 'Darjeeling Railway Station, Darjeeling',
                'ticket': {'adult': 1500, 'child': 1500, 'foreign': 1500, 'student': 1500, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '8:00 AM', 'close': '5:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Toy Train Darjeeling',
                'tips': ['Take the Joy Ride from Darjeeling to Ghoom'], 'nearby': ['Batasia Loop'], 'reviews': []
            },
            {
                'id': 'batasia-loop', 'name': 'Batasia Loop', 'category': 'Attraction', 'tags': ['nature', 'history'],
                'description': 'A spiral railway created to lower the gradient of ascent of the Darjeeling Himalayan Railway.', 'history': 'Commissioned in 1919.',
                'why_famous': 'War memorial and panoramic views.', 'interesting_facts': ['Offers a 360-degree view of Darjeeling'],
                'coordinates': [27.0163, 88.2492], 'address': 'West Point, Darjeeling',
                'ticket': {'adult': 15, 'child': 0, 'foreign': 15, 'student': 15, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '5:00 AM', 'close': '8:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': False},
                'crowd': 'High', 'rating': 4.4, 'photo_keyword': 'Batasia Loop',
                'tips': ['Best visited while on the Toy Train'], 'nearby': ['Tiger Hill'], 'reviews': []
            },
            {
                'id': 'happy-valley-tea-estate', 'name': 'Happy Valley Tea Estate', 'category': 'Nature', 'tags': ['nature', 'culture'],
                'description': 'The second oldest tea estate in Darjeeling.', 'history': 'Established in 1854.',
                'why_famous': 'Tea factory tours and tasting.', 'interesting_facts': ['One of the highest tea estates in the world'],
                'coordinates': [27.0475, 88.2612], 'address': 'Pamposh Enclave, Darjeeling',
                'ticket': {'adult': 100, 'child': 50, 'foreign': 100, 'student': 100, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '8:00 AM', 'close': '4:00 PM', 'weekly_off': 'Monday', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.3, 'photo_keyword': 'Darjeeling Tea Garden',
                'tips': ['Buy tea directly from the estate'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'peace-pagoda-darjeeling', 'name': 'Peace Pagoda Darjeeling', 'category': 'Monument', 'tags': ['peace', 'religion'],
                'description': 'A Buddhist stupa designed to provide a focus for people of all races and creeds.', 'history': 'Built under the guidance of Nichidatsu Fujii.',
                'why_famous': 'Provides a panoramic view of Darjeeling and the Kanchenjunga range.', 'interesting_facts': ['Houses four avatars of Buddha'],
                'coordinates': [27.0315, 88.2570], 'address': 'West Point, Darjeeling',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '4:30 AM', 'close': '7:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': False, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'Peace Pagoda Darjeeling',
                'tips': ['Listen to the traditional drumming during prayer times'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'padmaja-naidu-zoo', 'name': 'Padmaja Naidu Himalayan Zoological Park', 'category': 'Nature', 'tags': ['wildlife', 'family'],
                'description': 'A 67.56-acre zoo in Darjeeling.', 'history': 'Opened in 1958.',
                'why_famous': 'Conservation breeding of red panda and snow leopard.', 'interesting_facts': ['Highest altitude zoo in India'],
                'coordinates': [27.0504, 88.2541], 'address': 'Jawahar Parbat, Darjeeling',
                'ticket': {'adult': 60, 'child': 30, 'foreign': 150, 'student': 60, 'camera': 10, 'parking': 0, 'is_free': False},
                'timings': {'open': '8:30 AM', 'close': '4:30 PM', 'weekly_off': 'Thursday', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.6, 'photo_keyword': 'Red Panda Darjeeling',
                'tips': ['Tickets include entry to the Himalayan Mountaineering Institute'], 'nearby': ['Himalayan Mountaineering Institute'], 'reviews': []
            }
        ]
    },
    'mysore': {
        'name': 'Mysore',
        'state': 'Karnataka',
        'tagline': 'The City of Palaces',
        'description': 'Known for its heritage structures and palaces, including the famous Mysore Palace.',
        'coordinates': [12.2958, 76.6394],
        'best_season': 'October to March',
        'languages': ['Kannada', 'English'],
        'famous_food': [
            {'name': 'Mysore Pak', 'description': 'Rich sweet dish made of ghee, sugar, gram flour.', 'where_to_eat': 'Guru Sweet Mart'}
        ],
        'instagram_spots': [
            {'name': 'Mysore Palace Illumination', 'tip': 'Sundays and public holidays from 7 PM to 7:45 PM'}
        ],
        'trip_cost': {
            'budget': {'per_day': 900, 'hotel': 500, 'food': 300, 'transport': 100},
            'standard': {'per_day': 2200, 'hotel': 1200, 'food': 700, 'transport': 300},
            'luxury': {'per_day': 7000, 'hotel': 4000, 'food': 2000, 'transport': 1000}
        },
        'attractions': [
            {
                'id': 'mysore-palace', 'name': 'Mysore Palace', 'category': 'Monument', 'tags': ['history', 'architecture'],
                'description': 'A historical palace and a royal residence.', 'history': 'The current structure was constructed between 1897 and 1912.',
                'why_famous': 'Indo-Saracenic architecture and stunning illumination.', 'interesting_facts': ['One of the most visited monuments in India'],
                'coordinates': [12.3051, 76.6551], 'address': 'Sayyaji Rao Rd, Agrahara, Chamrajpura, Mysuru',
                'ticket': {'adult': 100, 'child': 50, 'foreign': 100, 'student': 50, 'camera': 0, 'parking': 50, 'is_free': False},
                'timings': {'open': '10:00 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2-3 hours'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Very High', 'rating': 4.8, 'photo_keyword': 'Mysore Palace Illuminated',
                'tips': ['Visit on Sunday evening for the illumination'], 'nearby': ['Jaganmohan Palace'], 'reviews': []
            },
            {
                'id': 'chamundeshwari-temple', 'name': 'Chamundeshwari Temple', 'category': 'Temple', 'tags': ['religion', 'views'],
                'description': 'A Hindu temple located on the top of Chamundi Hills.', 'history': 'Originally built in the 12th century by Hoysala rulers.',
                'why_famous': 'Dedicated to Goddess Chamundeshwari.', 'interesting_facts': ['Has a massive statue of Nandi the bull on the way up'],
                'coordinates': [12.2743, 76.6713], 'address': 'Chamundi Hill Rd, Mysuru',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '7:30 AM', 'close': '9:00 PM', 'weekly_off': 'None', 'best_time': 'Early Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': False, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.7, 'photo_keyword': 'Chamundeshwari Temple',
                'tips': ['You can hike up the 1000 steps or take a vehicle'], 'nearby': ['Mysore Zoo'], 'reviews': []
            },
            {
                'id': 'brindavan-gardens', 'name': 'Brindavan Gardens', 'category': 'Garden', 'tags': ['nature', 'family'],
                'description': 'A garden laid out adjoining the Krishnarajasagara Dam.', 'history': 'Work started in 1927 and was completed in 1932.',
                'why_famous': 'Musical fountain show.', 'interesting_facts': ['Modeled on the Shalimar Gardens of Kashmir'],
                'coordinates': [12.4228, 76.5739], 'address': 'KRS Dam Road, Mandya, Karnataka',
                'ticket': {'adult': 50, 'child': 10, 'foreign': 50, 'student': 50, 'camera': 50, 'parking': 50, 'is_free': False},
                'timings': {'open': '6:30 AM', 'close': '9:00 PM', 'weekly_off': 'None', 'best_time': 'Evening', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.2, 'photo_keyword': 'Brindavan Gardens Fountain',
                'tips': ['Musical fountain show happens in the evening'], 'nearby': [], 'reviews': []
            },
            {
                'id': 'st-philomena-church', 'name': 'St Philomena Church', 'category': 'Monument', 'tags': ['religion', 'architecture'],
                'description': 'A Catholic church that is the cathedral of the Diocese of Mysore.', 'history': 'Constructed in 1936.',
                'why_famous': 'Neo Gothic style architecture.', 'interesting_facts': ['Inspired by the Cologne Cathedral in Germany'],
                'coordinates': [12.3204, 76.6582], 'address': 'Lourdnagar, Ashoka Rd, Lashkar Mohalla, Mysuru',
                'ticket': {'adult': 0, 'child': 0, 'foreign': 0, 'student': 0, 'camera': 0, 'parking': 0, 'is_free': True},
                'timings': {'open': '5:00 AM', 'close': '6:00 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '1 hour'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': False, 'parking': True},
                'crowd': 'Medium', 'rating': 4.5, 'photo_keyword': 'St Philomena Church',
                'tips': ['Contains relics of St. Philomena'], 'nearby': ['Mysore Palace'], 'reviews': []
            },
            {
                'id': 'mysore-zoo', 'name': 'Mysore Zoo', 'category': 'Nature', 'tags': ['wildlife', 'family'],
                'description': 'One of the oldest and most popular zoos in India.', 'history': 'Created in 1892.',
                'why_famous': 'Well-maintained and houses a wide variety of animals.', 'interesting_facts': ['Currently houses over 1450 specimen'],
                'coordinates': [12.3023, 76.6644], 'address': 'Zoo Main Road, Indira Nagar, Ittige Gudu, Mysuru',
                'ticket': {'adult': 100, 'child': 50, 'foreign': 100, 'student': 100, 'camera': 0, 'parking': 50, 'is_free': False},
                'timings': {'open': '8:30 AM', 'close': '5:30 PM', 'weekly_off': 'Tuesday', 'best_time': 'Morning', 'visit_duration': '3 hours'},
                'facilities': {'wheelchair': True, 'photography': True, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'High', 'rating': 4.5, 'photo_keyword': 'Mysore Zoo',
                'tips': ['Very large, expect a lot of walking'], 'nearby': ['Mysore Palace'], 'reviews': []
            },
            {
                'id': 'jaganmohan-palace', 'name': 'Jaganmohan Palace', 'category': 'Museum', 'tags': ['history', 'art'],
                'description': 'A palace which now serves as an art gallery and a function hall.', 'history': 'Completed in 1861.',
                'why_famous': 'Houses the Jayachamarajendra Art Gallery.', 'interesting_facts': ['Contains original paintings by Raja Ravi Varma'],
                'coordinates': [12.3057, 76.6508], 'address': 'Jagan Mohan Palace Area, Chamrajpura, Mysuru',
                'ticket': {'adult': 40, 'child': 20, 'foreign': 40, 'student': 40, 'camera': 0, 'parking': 0, 'is_free': False},
                'timings': {'open': '8:30 AM', 'close': '5:30 PM', 'weekly_off': 'None', 'best_time': 'Morning', 'visit_duration': '2 hours'},
                'facilities': {'wheelchair': True, 'photography': False, 'food_nearby': True, 'washroom': True, 'parking': True},
                'crowd': 'Medium', 'rating': 4.4, 'photo_keyword': 'Jaganmohan Palace Art',
                'tips': ['A must-visit for art lovers'], 'nearby': ['Mysore Palace'], 'reviews': []
            }
        ]
    }
}

CITY_ALIASES = {
    'new delhi': 'delhi',
    'bombay': 'mumbai',
    'calcutta': 'kolkata',
    'madras': 'chennai',
    'bengaluru': 'bangalore',
    'benares': 'varanasi',
    'benaras': 'varanasi',
    'kashi': 'varanasi',
    'mysuru': 'mysore',
    'cochin': 'kochi',
    'ernakulam': 'kochi',
}
