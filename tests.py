import unittest
from unittest.mock import patch
from flask import Flask, request, jsonify
from text_classifier import app, classify_text, CATEGORIES  # assuming your code is in app.py
import json


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_classify_valid_input(self):
        with patch('httpx.post') as mock_post:
            mock_post.return_value.json.return_value = {
                'choices': [{'message': {'content': 'sports'}}]
            }
            response = self.app.post('/classify',
                                     data=json.dumps({'text': 'Football is a popular game.', 'classes': CATEGORIES}),
                                     content_type='application/json')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(data['category'], 'sports')

    def test_classify_missing_text(self):
        response = self.app.post('/classify',
                                 data=json.dumps({'classes': CATEGORIES}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], 'No text provided')

    def test_classify_missing_classes(self):
        response = self.app.post('/classify',
                                 data=json.dumps({'text': 'Football is a popular game.'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], 'No classes provided')


if __name__ == '__main__':
    unittest.main()
