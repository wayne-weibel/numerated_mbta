"""mbta test cases"""
# pylint: disable=no-self-use
import unittest.mock as mock

from django.test import TestCase

import mbta.models

# Create your tests here.
class MBTAModelsTest(TestCase):
    """test views"""

    def setUp(self):
        pass

    @mock.patch('mbta.models.requests')
    def test_get_route(self, requests):
        """test get route"""
        uri = "{}/{}".format(mbta.models.MBTAAPIv3.api_base, 'routes/route_id')
        headers  = mbta.models.MBTAAPIv3.api_headers
        params = {'filter[type]': '0'}

        mbta.models.MBTARoute().get('route_id', filters={'type':[mbta.models.MBTARoute.Type.LIGHT_RAIL]})
        requests.get.assert_called_with(uri, params=params, headers=headers)

    @mock.patch('mbta.models.requests')
    def test_get_stop(self, requests):
        """test get stop"""
        uri = "{}/{}".format(mbta.models.MBTAAPIv3.api_base, 'stops/stop_id')
        headers  = mbta.models.MBTAAPIv3.api_headers
        params = {'include': 'route'}

        mbta.models.MBTAStop().get('stop_id')
        requests.get.assert_called_with(uri, params=params, headers=headers)

    @mock.patch('mbta.models.requests')
    def test_get_prediction(self, requests):
        """test get prediction"""
        uri = "{}/{}".format(mbta.models.MBTAAPIv3.api_base, 'predictions')
        headers  = mbta.models.MBTAAPIv3.api_headers
        params = {'sort': 'departure_time',
                  'filter[route]': 'route_id', 'filter[direction_id]': '0', 'filter[stop]': 'stop_id'}

        mbta.models.MBTAPrediction().get('route_id', 0, 'stop_id')
        requests.get.assert_called_with(uri, params=params, headers=headers)
