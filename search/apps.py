from django.apps import AppConfig


class SearchConfig(AppConfig):
    name = 'search'

    # Making instance of scheduler
    def ready(self):
        print("Starting Scheduler ...")
        from scheduler import data_update
        data_update.start()
