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
from swagger_client.api.graph_store_api import GraphStoreApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGraphStoreApi(unittest.TestCase):
    """GraphStoreApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.graph_store_api.GraphStoreApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_statements_to_indirect_namedgraph(self):
        """Test case for add_statements_to_indirect_namedgraph

        Add statements to an INDIRECTLY referenced named graph  # noqa: E501
        """
        pass

    def test_add_statements_to_namedgraph(self):
        """Test case for add_statements_to_namedgraph

        Add statements to a DIRECTLY referenced named graph  # noqa: E501
        """
        pass

    def test_delete_statements_from_indirect_namedgraph(self):
        """Test case for delete_statements_from_indirect_namedgraph

        Clear an INDIRECTLY referenced named graph  # noqa: E501
        """
        pass

    def test_delete_statements_from_namedgraph(self):
        """Test case for delete_statements_from_namedgraph

        Clear a DIRECTLY referenced named graph  # noqa: E501
        """
        pass

    def test_get_all_statements_from_indirect_namedgraph(self):
        """Test case for get_all_statements_from_indirect_namedgraph

        Fetch all statements from an INDIRECTLY referenced named graph  # noqa: E501
        """
        pass

    def test_get_all_statements_from_namedgraph(self):
        """Test case for get_all_statements_from_namedgraph

        Fetch all statements from a DIRECTLY referenced named graph  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()