"""mbta test cases"""
# pylint: disable=no-self-use
import unittest.mock as mock

from django.http import HttpRequest, JsonResponse
from django.test import TestCase

import mbta.ajax

# Create your tests here.
class MBTAAjaxTest(TestCase):
    """test ajax"""

    def setUp(self):
        pass

    @mock.patch('mbta.ajax.MBTAStop')
    def test_stops_by_route(self, stop):
        """test index"""
        stop().get().json.return_value = {'data': []}

        resp = mbta.ajax.stops_by_route(HttpRequest())
        assert resp.status_code == 200
        assert resp.content == JsonResponse({'stops': []}).content

    def test_departure_prediction_403(self):
        """test departure prediction failure - missing param"""
        post = HttpRequest()

        resp = mbta.ajax.departure_prediction(post)
        assert resp.status_code == 403
        assert resp.content == b'Please select a Route'
        assert str(resp.content, 'utf-8') == 'Please select a Route'

        post.POST.update({'route_id': 'TEST'})
        resp = mbta.ajax.departure_prediction(post)
        assert resp.status_code == 403
        assert resp.content == b'Please select a Direction'
        assert str(resp.content, 'utf-8') == 'Please select a Direction'

        post.POST.update({'direction_id': 'TEST'})
        resp = mbta.ajax.departure_prediction(post)
        assert resp.status_code == 403
        assert resp.content == b'Please select a Stop'
        assert str(resp.content, 'utf-8') == 'Please select a Stop'

    @mock.patch('mbta.ajax.MBTAPrediction')
    def test_departure_prediction_404(self, _):
        """test departure prediction failure - unable to find departure"""
        post = HttpRequest()
        post.POST = {'route_id': 'test', 'direction_id': 'test', 'stop_id': 'test'}

        resp = mbta.ajax.departure_prediction(post)
        assert resp.status_code == 404
        assert resp.content == b'Unable to predicte Departure'
        assert str(resp.content, 'utf-8') == 'Unable to predicte Departure'


    @mock.patch('mbta.ajax.MBTAPrediction')
    def test_departure_prediction_200(self, prediction):
        """test departure prediction failure - unable to find departure"""
        post = HttpRequest()
        post.POST = {'route_id': 'test', 'direction_id': 'test', 'stop_id': 'test'}

        prediction().get().json.return_value = {'data': [{'attributes': {'departure_time': 'TEST DATETIME'}}]}

        resp = mbta.ajax.departure_prediction(post)
        assert resp.status_code == 200
        assert resp.content == b'TEST DATETIME'
        assert str(resp.content, 'utf-8') == 'TEST DATETIME'
