# 🖥️ Monitrix - Server Monitoring Dashboard

![Monitrix Screenshot](dashboard/assets/screenshot_dark.png)
![Monitrix Screenshot](dashboard/assets/screenshot_light.png)

**Monitrix** is a real-time server monitoring dashboard built with FastAPI, WebSockets, and Chart.js. It features live metrics for CPU, memory, and disk usage with interactive charts, dark/light theme toggle, and responsive UI.

---

## 🔧 Features

- ✅ Real-time monitoring via WebSocket
- ✅ Light/Dark mode switch
- ✅ Animated loading spinner & hover effects
- ✅ Clean Bootstrap layout
- ✅ Live CPU, Memory, Disk charts with Chart.js

---

## 🚀 Run the Project

### 1. Clone the Repo

```bash
git clone https://github.com/silverstar33/monitrix.git
cd monitrix

2. Install Dependencies
pip install -r requirements.txt

Or manually if no requirements.txt:
pip install fastapi uvicorn psutil websockets

3. Start the Monitoring Agent
This script gathers real-time system metrics and sends them to the dashboard backend.

python monitor_agent.py
Make sure this is running on the machine you want to monitor.

4. Start the FastAPI Backend in another Terminal
uvicorn main:app --reload

Then open in browser:
📍 http://localhost:8000

🗂️ Folder Structure
monitrix/
├── main.py                 # FastAPI backend
├── monitor_agent.py        # Sends real-time metrics
├── dashboard/
│   ├── dashboard.html      # Main UI
│   └── assets/             # Logos, favicon, screenshots
│       ├── logo_black.png
│       ├── logo_green.png
│       ├── favicon2.ico
│       ├── screenshot_light.png
│       └── screenshot_dark.png
├── requirements.txt
├── README.md
└── run.sh                  # Use Git Bash or WSL (Windows Subsystem for Linux) to run run.sh directly
```
### 💡 Why Use Monitrix?

Monitrix solves real-world problems faced by developers, sysadmins, and home server enthusiasts:

- ✅ Most tools like Prometheus or Grafana are overkill for personal projects or small teams. 
- Monitrix gives you a lightweight, self-hosted dashboard that shows live CPU, memory, and disk usage — all without complex setup or a steep learning curve.


## 🧑‍💻 For Developers & Self-Hosters
- 🔧 Self-host in minutes with FastAPI + Python

- 📈 Real-time metrics via WebSockets (CPU, Memory, Disk)

- 🎨 Responsive UI with dark/light mode toggle

- 🚀 Zero bloat, only essentials – Easy to run, hack, and extend

- 🖥️ Run anywhere – Raspberry Pi, VPS, cloud, or home server

## 🌐 For Non-Technical Users / SaaS Vision
- 🛡️ Peace of Mind – Know your servers are running smoothly 24/7

- 🧩 No Setup Headache – Just run one script and start monitoring

- 📊 Instant Insights – Visualize performance without logging in to terminals

- ☁️ Use it as a Service – Let us host and handle everything (coming soon)

- ⚙️ Zero Dev Skills Needed – Clean UI with real-time feedback


### 📦 Future Enhancements
- Package dashboard & agent as a .exe (single-click)

- Add Slack/Email alerting system

- Add Docker support for easy deployment

- More Features will be added according to Requirements and needs
---

## 🧡 Made with love in India



