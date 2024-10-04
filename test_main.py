import unittest
import json
from main import app


class AlphabetCheckTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    """Test case where the input string contains all alphabets"""
    def test_contains_all_alphabet(self):
        payload = {"input_string": "The quick brown fox jumps over the lazy dog234 &8*"}
        response = self.app.post('/check_alphabet',
                                 data=json.dumps(payload),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['contains_all_alphabet'], True)

    """Test case where the input string does not contain all alphabets"""
    def test_does_not_contain_all_alphabet(self):
        payload = {"input_string": "Hello World"}
        response = self.app.post('/check_alphabet',
                                 data=json.dumps(payload),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['contains_all_alphabet'], False)

    """Test case where the input_string is missing in the request"""
    def test_missing_input_string(self):
        payload = {}
        response = self.app.post('/check_alphabet',
                                 data=json.dumps(payload),
                                 content_type='application/json')

        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'input string not provided')

# To execute all tests at once in our app
if __name__ == '__main__':
    unittest.main()

# Using above unittest we can run our application and test our application for various scenarios
# Command to run above test cases python3 test_main.py