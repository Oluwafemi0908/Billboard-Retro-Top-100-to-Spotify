import datetime as dt
import calendar
import re


class DateConverter:
    def __init__(self):
        self.request_date = None
        self.billboard_month = str(dt.datetime.now().month).zfill(2)
        self.billboard_year = str(dt.datetime.now().year)
        self.billboard_day = None
        self.months = list(calendar.month_name)[1:]
        self.months_abbr = list(calendar.month_abbr)[1:]
        self.years = list(range(1958, dt.datetime.now().year + 1))
        self.days = list(range(0, 32))
        self.all = self.months + self.days + self.years + self.months_abbr
        self.all_string = [str(x).lower() for x in self.all]
        self.wrong_data = False
        self.converted = False

    def convert_date(self, input_date):
        if input_date < self.billboard_year:
            return input_date
        else:
            try:
                date_split = re.split(r'[\s,;._-]+',
                                      input_date.lower())  # Splitting by spaces, commas, semicolons, dots,
                # underscores, and dashes
            except:
                date_split = [input_date]

            while not self.wrong_data or not self.converted:
                for data in date_split:
                    if data.lower() not in self.all_string:
                        self.wrong_data = data
                    else:
                        for year in self.years:
                            if str(year) in date_split:
                                self.billboard_year = str(year)
                        for m in self.months:
                            if m.lower() in date_split:
                                self.billboard_month = str(dt.datetime.strptime(m, "%B").month).zfill(2)
                        for m in self.months_abbr:
                            if m.lower() in date_split:
                                self.billboard_month = str(dt.datetime.strptime(m, "%b").month).zfill(2)
                        for day in self.days:
                            if str(day) in date_split:
                                self.billboard_day = str(day).zfill(2)
                            elif not self.billboard_day:
                                if self.billboard_year == str(dt.datetime.now().year):
                                    if self.billboard_month == str(dt.datetime.now().month).zfill(2):
                                        self.billboard_day = str(dt.datetime.now().day).zfill(2)
                                    else:
                                        self.billboard_day = "28"

                                else:
                                    self.billboard_day = "28"

                        if (self.billboard_month > str(dt.datetime.now().month).zfill(2) and self.billboard_year >=
                                str(dt.datetime.now().year)):
                            self.billboard_year = str(int(dt.datetime.now().year) - 1)

                        self.request_date = "-".join(
                            filter(None, [self.billboard_year, self.billboard_month, self.billboard_day]))
                        return self.request_date
                self.converted = True

            if self.wrong_data:
                print(f"Wrong Data spotted, check '{self.wrong_data}'")

    # def check_year_or_date(self, input_date):
    #     if input_date < self.billboard_year:
    #         return input_date
    #     else:
    #         return self.request_date


x = DateConverter()
x.convert_date('march 2025')
