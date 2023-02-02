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
from swagger_client.api.sparql_api import SparqlApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSparqlApi(unittest.TestCase):
    """SparqlApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.sparql_api.SparqlApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_execute_get_select_query(self):
        """Test case for execute_get_select_query

        Send queries on a specific repository with ID. This resource represents a SPARQL query endpoint  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Performs updates on the data in the repository  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
