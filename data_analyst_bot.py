
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import datetime

TOKEN = 'SENIN_BOT_TOKENIN'
CHAT_ID = 'SENIN_CHAT_IDIN'
bot = Bot(token=TOKEN)

def scrape_bossaz():
    url = "https://boss.az/vacancies?search%5Btext%5D=data+analitik"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    jobs = []
    for item in soup.select("div.results-i"):
        title = item.select_one("a.results-title").text.strip()
        link = "https://boss.az" + item.select_one("a.results-title")["href"]
        jobs.append(f"📌 {title}\n🔗 {link}")
    return jobs

def scrape_jobsearch():
    url = "https://jobsearch.az/search?q=data+analyst"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    jobs = []
    for item in soup.select("div.col-md-9 div.card"):
        title = item.select_one("a").text.strip()
        link = "https://jobsearch.az" + item.select_one("a")["href"]
        jobs.append(f"📌 {title}\n🔗 {link}")
    return jobs

def send_daily_report():
    date = datetime.datetime.now().strftime("%d %B %Y")
    msg = f"📊 *{date} üçün Data Analyst vakansiyaları:*\n\n"
    boss_jobs = scrape_bossaz()
    jobsearch_jobs = scrape_jobsearch()
    all_jobs = boss_jobs + jobsearch_jobs
    if not all_jobs:
        msg += "Bu gün üçün heç bir vakansiya tapılmadı."
    else:
        msg += "\n\n".join(all_jobs)
    bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="Markdown")

if __name__ == "__main__":
    send_daily_report()
