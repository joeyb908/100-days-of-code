import datetime as dt

class Date():

    def __init__(self):
        self.data = dt.datetime
        self.today = self.data.today()
        self.yesterday = str((self.today - dt.timedelta(days=1)).date())
