#!/usr/bin/env python3
"""Unit test for client class"""
import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import utils


class TestGithubOrgClient(unittest.TestCase):
    """test class for github client class"""

    @parameterized.expand([
            ('google', {'org': 'google'}),
            ('abc', {'org': 'abc'})])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock):
        """Test github org"""
        mock.return_value = expected
        client = GithubOrgClient(org_name)
        assert client.org == expected
        mock.assert_called_once()

    def test_public_repos_url(self):
        """Tests clients public repos url"""
        payload = TEST_PAYLOAD[0][0]
        with patch.object(GithubOrgClient, 'org') as org:
            # manages return value based on behaviour wrt memoize decorator
            org.__getitem__.return_value = payload['repos_url']
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url, payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """test github public_repos method."""

        payload = TEST_PAYLOAD[0][1]
        get_json_mock.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url') as mock_url:

            mock_url.return_value = 'http://github.com/org/google/repos'
            client = GithubOrgClient('google')
            self.assertIsInstance(client.public_repos(), list)
            get_json_mock.assert_called_once()

    @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, repo, license_key, expected):
        """test has license method"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Setup class for test"""

        cls.get_patcher = patch('requests.get', side_effect=utils.get_json)
        cls.get_patcher.start()
        cls.get_patcher.return_value.json.return_value = cls.org_payload
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """Tear down class for test"""

        cls.get_patcher.stop()
