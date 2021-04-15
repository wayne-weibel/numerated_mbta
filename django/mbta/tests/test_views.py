"""mbta test cases"""
# pylint: disable=no-self-use
import unittest.mock as mock

from django.test import TestCase

import mbta.views

# Create your tests here.
class MBTAViewsTest(TestCase):
    """test views"""

    def setUp(self):
        pass

    @mock.patch('mbta.views.render')
    @mock.patch('mbta.views.MBTAStop')
    @mock.patch('mbta.views.MBTARoute')
    def test_index(self, routes, stops, render):
        """test index"""
        mbta.views.index(mock.ANY)
        routes.assert_called_once()
        stops.assert_called_once()
        render.assert_called_with(mock.ANY, 'mbta/index.html', {'routes': mock.ANY, 'stops': mock.ANY})
