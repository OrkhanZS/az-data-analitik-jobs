
# Azerbaijan Data Analyst Job Bot 🤖

This is a Python-based Telegram bot that sends daily job postings for **Data Analyst** roles in Azerbaijan.

## Setup

1. Clone or download the repo
2. Install requirements:  
```bash
pip install -r requirements.txt
```
3. Set your Telegram bot `TOKEN` and `CHAT_ID` in `data_analyst_bot.py`.

## Run manually:
```bash
python data_analyst_bot.py
```

## Automate with cron (Linux):
```bash
0 9 * * * /usr/bin/python3 /tam/yol/data_analyst_bot.py
```
