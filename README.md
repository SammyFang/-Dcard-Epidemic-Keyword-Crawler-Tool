# -Dcard-Epidemic-Keyword-Crawler-Tool
Dcard Epidemic Keyword Crawler Tool Built a Python crawler to track COVID-19 posts on Dcard, extracting key discussions and sending real-time alerts via LINE API. Optimized performance, bypassed anti-crawling measures, and used SQL for data management. Future upgrades include a GUI for custom keywords and enhanced automation with a LINE bot.

# Dcard Epidemic Keyword Crawler Tool

A Python-based web crawler that tracks COVID-19-related discussions on Dcard’s Dong Hwa University section. It extracts posts with relevant keywords and delivers real-time notifications to users via LINE Notify, ensuring timely access to critical epidemic updates.

## Features
- **Automated Tracking**: Fetches posts containing epidemic-related keywords such as "rapid test," "confirmed case," "remote learning," etc.
- **Real-time Notifications**: Sends alerts via LINE Notify when new relevant posts are detected.
- **Optimized Crawling**: Bypasses anti-crawling mechanisms for efficient data retrieval.
- **SQLite Integration**: Stores retrieved posts to prevent duplicate notifications.
- **User-Friendly Execution**: Requires minimal setup; just input your LINE Notify token and run the program.

## Installation

### **Prerequisites**
- **Python 3.9+**  
- **Dependencies** (Install via `requirements.txt`):  
  ```sh
  pip install -r requirements.txt
## Usage Instructions

### Step 1: Obtain a LINE Notify Token
1. Visit [LINE Notify](https://notify-bot.line.me/) and log in with your LINE account.
2. Click **Issue Token**.
3. Enter a token name (e.g., "Dcard Epidemic Alerts") and select **1-on-1 LINE Notify Notification**.
4. Copy and securely store the generated token (it will not be displayed again).

### Step 2: Run the Program
1. Open the program and paste your LINE Notify token when prompted.
2. Press **Enter** to start receiving notifications.
3. To stop, simply close the program window.

### Expected Output
Once running, the program fetches the latest posts matching the predefined keywords and sends notifications to your LINE account. Example output:

<div align="center"><img width="360" height="720" src="https://i.imgur.com/lqt9xBm.jpg"/></div>

---

## Troubleshooting & FAQs
- **Notifications are delayed** → Network speed or API response time may cause delays.
- **Program closes unexpectedly** → Ensure you entered the correct LINE Notify token.
- **Not receiving new posts** → Restart the program to refresh the data.
- **Database file (`Dcard.db`) missing** → This file is used to track sent posts; deleting it will reset the notification history.

---

## Keywords Monitored
The crawler tracks posts containing:
```plaintext
["rapid test", "online teaching", "remote learning", "epidemic", "footprints", "immunity", "transmission chain", "vaccine", "mass testing", "confirmed case"]
