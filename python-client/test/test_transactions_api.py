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
from swagger_client.api.transactions_api import TransactionsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.transactions_api.TransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_execute_transaction_action(self):
        """Test case for execute_transaction_action

        Execute a transaction action  # noqa: E501
        """
        pass

    def test_rollback_transaction(self):
        """Test case for rollback_transaction

        Abort a transaction  # noqa: E501
        """
        pass

    def test_start_new_transaction(self):
        """Test case for start_new_transaction

        Start a new transaction  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
