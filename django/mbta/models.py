"""
MBTA Models
"""
# pylint: disable=too-few-public-methods
import requests

from mbta.apps import MBTAConfig


class MBTAAPIv3:
    """base api class"""
    api_base = "https://api-v3.mbta.com"
    api_headers = {
        'x-api-key': MBTAConfig.api_key,
        'accept': 'application/vnd.api+json',
    }

    def __make_params(self, **kwargs):
        """helper to assemble request params"""
        params = {}

        for key, value in kwargs.items():
            if isinstance(value, list):
                params[key] = ','.join(map(str, value))
            elif isinstance(value, dict):
                _params = self.__make_params(**value)
                for _key, _value in _params.items():
                    params['{}[{}]'.format(key, _key)] = _value
            elif value is not None: # may need to pass 'False' or 0
                params[key] = str(value)

        return params

    def _get(self, uri, headers=None, **kwargs):
        """
        GET call to API
        :param uri string: api path
        :param headers dict: additional headers to include in the request
        :param **kwargs dict: additional params to append to the path
        :return: @see requests.get
        """
        url = "{}/{}".format(self.api_base, uri)

        params = self.__make_params(**kwargs)

        headers = headers or {}
        headers.update(self.api_headers)

        return requests.get(url, params=params, headers=headers)


class MBTARoute(MBTAAPIv3):
    """Route"""
    class Type:
        """route types"""
        LIGHT_RAIL = 0
        HEAVY_RAIL = 1
        COMMUTER_RAIL = 2
        BUS = 3
        FERRY = 4

    def get(self, route_id=None, limit=None, filters=None, headers=None):
        """get all routes, or route by id"""
        uri = 'routes'
        if route_id:
            uri = '{}/{}'.format(uri, route_id)

        return self._get(uri, headers=headers, limit=limit, filter=filters)


class MBTAStop(MBTAAPIv3):
    """Stop"""

    def get(self, stop_id=None, limit=None, filters=None, headers=None):
        """get all stops, or stop by id"""
        uri = 'stops'
        if stop_id:
            uri = '{}/{}'.format(uri, stop_id)

        return self._get(uri, headers=headers, limit=limit, filter=filters, include=['route'])


class MBTAPrediction(MBTAAPIv3):
    """Prediction"""

    def get(self, route_id, direction_id, stop_id):
        """get predicted time for the stop on route, heading direction"""
        uri = 'predictions'

        filters = {
            'route': route_id,
            'direction_id': direction_id,
            'stop': stop_id,
        }

        return self._get(uri, filter=filters, sort=['departure_time'])
