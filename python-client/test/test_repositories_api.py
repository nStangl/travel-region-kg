# coding: utf-8

"""
    RDF4J API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.repositories_api import RepositoriesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRepositoriesApi(unittest.TestCase):
    """RepositoriesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.repositories_api.RepositoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_repository(self):
        """Test case for delete_repository

        Repository removal  # noqa: E501
        """
        pass

    def test_delete_statements(self):
        """Test case for delete_statements

        Deletes statements from the repository.  # noqa: E501
        """
        pass

    def test_get_all_repositories(self):
        """Test case for get_all_repositories

        An overview of the repositories that are available on a server.  # noqa: E501
        """
        pass

    def test_get_all_statements(self):
        """Test case for get_all_statements

        Fetches statements from the repository.  # noqa: E501
        """
        pass

    def test_get_repository_size(self):
        """Test case for get_repository_size

        The repository size (defined as the number of statements it contains)  # noqa: E501
        """
        pass

    def test_put_statements(self):
        """Test case for put_statements

        Updates data in the repository, replacing any existing data with the supplied data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
