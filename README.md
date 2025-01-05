# ID Check Bot  

**A Telegram bot to check the ID of forwarded messages, identify users, and apply rate limits to prevent abuse.**  

---

## Features  
- Identify the group or user ID of forwarded messages.  
- Rate limit requests to prevent spamming (default: 1 request per 5 seconds).  
- Automatically ban users exceeding the rate limit for 24 hours.  
- Provide a concise usage guide after `/start`.  

---

## Installation  

### Requirements  
- Python 3.11+  
- Telegram bot token (obtainable via [BotFather](https://core.telegram.org/bots#botfather))  

### Setup  
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/ryu878/id-check-bot.git  
   cd id-check-bot  
    ```
2. **Install Dependencies:**  
    ```bash
    pip install -r requirements.txt
    ```
