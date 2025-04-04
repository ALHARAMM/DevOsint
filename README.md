# DevOsint

**DevOsint** is a simple OSINT tool designed to collect device information and approximate location from a target, simply by getting them to click on a crafted URL. Once they click the link, their data is captured and sent to your Discord webhook for easy viewing.

---

## 🚀 Features
- Collects device information (browser, OS, screen size, etc.)
- Captures approximate geolocation (based on browser permissions)
- Sends collected data directly to your Discord webhook
- Auto-redirects the victim to any URL you specify (for realism)

---

## ⚙️ Usage

1. **Navigate to the `src` directory.**
2. **Open `osint.html` and edit the file:**
   - Replace all placeholders for the Discord webhook with your own webhook URL.
   - Set the redirect URL (where the target will be automatically redirected after the data is sent).

> Example: You might redirect the user to a YouTube video, fake login page, or any site to make the scenario more realistic.

---

## ⚠️ Disclaimer

This tool is intended **for educational and authorized security testing purposes only**.  
Any misuse of this tool is strictly discouraged and the developer is **not responsible** for any damages or illegal activities.

---

Feel free to contribute or suggest improvements!
