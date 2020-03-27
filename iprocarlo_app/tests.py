import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Search


class SearchModelTests(TestCase):
    def test_was_searched_recently_with_future_search(self):
        """
        was_searched_recently() returns False for searches whose search_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_search = Search(search_date=time)
        self.assertIs(future_search.was_searched_recently(), False)

    def test_was_search_recently_with_old_search(self):
        """
        was_searched_recently() returns False for searchs whose search_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_search = Search(search_date=time)
        self.assertIs(old_search.was_searched_recently(), False)

    def test_was_search_recently_with_recent_search(self):
        """
        was_searched_recently() returns True for searchs whose search_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_search = Search(search_date=time)
        self.assertIs(recent_search.was_searched_recently(), True)
