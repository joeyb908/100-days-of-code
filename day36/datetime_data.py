import datetime as dt


class Date:

    def __init__(self):
        # sets the date as yesterday's date
        self.time = dt.datetime
        self.today = self.time.today()
        self.yesterday = str((self.today - dt.timedelta(days=1)).date())
