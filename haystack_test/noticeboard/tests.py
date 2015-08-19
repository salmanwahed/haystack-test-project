from django.test import TestCase
from noticeboard.models import Notice
from django.utils import timezone

# Create your tests here.

class NoticeTestCase(TestCase):
    def setUp(self):
        Notice.objects.create(title="Test notice 1", body="Some body of notice 1", pubdate=timezone.now(),
                              organization='KIN')

    def test_entry(self):
        objects = Notice.objects.all()
        self.assertEqual(len(objects), 1)
