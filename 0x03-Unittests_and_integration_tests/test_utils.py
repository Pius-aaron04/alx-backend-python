#!/usr/bin/env python3
"""Tests for utils functions"""

import unittest
from utils import access_nested_map, memoize
from unittest.mock import patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """tests access_nested_map utils fn"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests access map with expected outputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """tests access_nested_map func with invalid data"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})])
    def test_get_json(self, url, test_payload):
        """test get_json function"""
        with patch('utils.requests') as mock_requests:
            mock_requests.get.return_value = test_payload
            mock_requests.get('url')
            mock_requests.get.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test case for memoized function"""
    def test_memoize(self):
        """test memoize decorator"""
        class TestClass:
            """test class for memoize"""
            def a_method(self):
                """a method that return 42"""
                return 42

            @memoize
            def a_property(self):
                """memoized function"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as a_method:
            test = TestClass()
            test.a_property
            test.a_property
            a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
