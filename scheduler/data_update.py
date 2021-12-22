from apscheduler.schedulers.background import BackgroundScheduler
from search.views import getdata


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(getdata, "interval", minutes=1,
                      id="search_001", replace_existing=True)
    scheduler.start()
