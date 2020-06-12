from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class Future:

    @staticmethod
    def oil(oil):
        oil = datetime.strptime(oil, "%Y-%m-%d %H:%M:%S")
        oil += relativedelta(months=+1)
        return oil.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def filtr(filtr):
        filtr = datetime.strptime(filtr, "%Y-%m-%d %H:%M:%S")
        filtr += relativedelta(months=+1)
        return filtr.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def insurance(insurance):
        insurance = datetime.strptime(insurance, "%Y-%m-%d %H:%M:%S")
        insurance += relativedelta(years=+1)
        return insurance.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def tech_check(tech_check):
        tech_check = datetime.strptime(tech_check, "%Y-%m-%d %H:%M:%S")
        tech_check += relativedelta(months=+1)
        return tech_check.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def air_tires(air_tires):
        air_tires = datetime.strptime(air_tires, "%Y-%m-%d %H:%M:%S")
        air_tires += relativedelta(months=+1)
        return air_tires.strftime("%Y-%m-%d %H:%M:%S")