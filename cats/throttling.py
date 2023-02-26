import datetime

from rest_framework import throttling


class WorkingHoursRateThrottle(throttling.BaseThrottle):
    """Ограничение запросов в период с 12 до 13 часов."""
    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if now >= 12 and now <= 13:
            return False
        return True
