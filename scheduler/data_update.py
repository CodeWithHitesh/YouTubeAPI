from apscheduler.schedulers.background import BackgroundScheduler
from search.views import getdata

# This adds a scheduler to update the data after an interval of 10 seconds.


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(getdata, "interval", seconds=10,
                      id="search_001", replace_existing=True)
    scheduler.start()
