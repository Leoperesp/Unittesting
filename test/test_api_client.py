import unittest, requests
from src.api_client import get_location
from unittest.mock import patch


class ApiClientTest(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "United States of America",
            "regionName" : "California",
            "cityName": "Mountain View",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(
            result.get('country'), 
            'United States of America',
        )

    @patch('src.api_client.requests.get')
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavaliable"),
            unittest.mock.Mock(
                status_code = 200,
                json = lambda:{
                    "countryName": "United States of America",
                    "regionName" : "California",
                    "cityName": "Mountain View",                   
                }
            )
        ]
 
        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get('country'),'United States of America',)
        self.assertEqual(result.get('region'),'California',)
        self.assertEqual(result.get('city'),'Mountain View',)

