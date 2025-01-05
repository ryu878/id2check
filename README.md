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
   git clone https://github.com/ryu878/id2check.git  
   cd id2check 
    ```
2. **Install Dependencies:**  
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the Bot:**  
    ```bash
    python id2checkbot.py
    ```

### Usage

1. **Start the Bot:**
    Send /start to the bot. The bot will reply with instructions.

    Forward Messages:
        Forward a message to the bot to identify the ID of the sender or group.
        If the message originates from a user, the bot will provide the user ID.
        If it originates from a group/channel, it will display the group/channel ID.

    Rate Limiting:
    Users can send requests at most once every 5 seconds. Spamming requests results in a 24-hour ban.


