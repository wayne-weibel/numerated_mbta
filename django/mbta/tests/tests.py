"""mbta test cases"""
from django.test import TestCase

from mbta.apps import MBTAConfig

# Create your tests here.
class MBTAConfigTest(TestCase):

    def setUp(self):
        pass

    def test_api_key_present(self):
        assert MBTAConfig.api_key
