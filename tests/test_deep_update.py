__author__ = 'andi'
from templating import deep_update
from unittest import TestCase



class TestDeepUpdate(TestCase):
    def test_simple(self):
        input = {
            'a': 1,
            'b': 2,
        }
        update = {
            'c': 3,
            'd': 4
        }
        expected = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4
        }

        result = deep_update(input, update)
        self.assertEqual(result, expected)

    def test_multi_layer(self):
        input = {
            'a': 1,
            'b': {
                'c': 3
            }
        }

        update = {
            'b': {
                'd': 2
            }
        }

        expected = {
            'a': 1,
            'b': {
                'c': 3,
                'd': 2
            }
        }

        result = deep_update(input, update)
        self.assertEqual(result, expected)

    def test_override(self):
        input = {
            'a': 1,
            'b': [1, 2, 3, 4, 5, 6]
        }
        update = {
            'b': []
        }

        expected = { 'a': 1, 'b': [] }

        result = deep_update(input, update)
        self.assertEqual(result, expected)
