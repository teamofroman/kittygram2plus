import datetime

from rest_framework import throttling


class WorkingHoursRateThrottle(throttling.BaseThrottle):

    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if now >= 12 and now <= 13:
            return False
        return True
