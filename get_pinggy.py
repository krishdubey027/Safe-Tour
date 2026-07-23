import subprocess
import time
import os
import re

print("Starting Pinggy SSH Tunnel...")
cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-p", "443", "-R", "80:localhost:5000", "free.pinggy.io"]

# Start subprocess
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Wait 5 seconds for connection handshake
time.sleep(5)

# Read whatever is in the pipe buffer (non-blocking read)
try:
    fd = process.stdout.fileno()
    data = os.read(fd, 8192)
    output = data.decode('utf-8', errors='ignore')
    
    # Strip ANSI escape codes
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    clean_output = ansi_escape.sub('', output)
    
    # Write full clean log
    with open("pinggy_debug.txt", "w", encoding="utf-8") as f:
        f.write(clean_output)
        
    # Search for URL (looks like http://xxxx.pinggy.link or https://xxxx.pinggy.link)
    urls = re.findall(r'https?://[a-zA-Z0-9.-]+\.pinggy\.[a-zA-Z0-9.-]+', clean_output)
    
    if urls:
        # Save the unique URLs to pinggy_url.txt
        unique_urls = list(set(urls))
        with open("pinggy_url.txt", "w", encoding="utf-8") as f:
            for url in unique_urls:
                f.write(url + "\n")
        print(f"URLs found: {unique_urls}")
    else:
        print("No URLs found in the first 5 seconds. Check pinggy_debug.txt")
except Exception as e:
    print(f"Error reading stdout: {e}")

# Keep the SSH process running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping tunnel...")
    process.terminate()
