from datetime import datetime


class DateProvider:
    @staticmethod
    def now():
        return datetime.now()

	# Added by Liwen Guo
	def today():
		return datetime.today()

	# Added by Liwen Guo	
	def oneday():
		return datetime.timedelta(days=1)
