# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_event_list import V1EventList


class TestV1EventList(unittest.TestCase):
    """ V1EventList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1EventList(self):
        """
        Test V1EventList
        """
        model = kubernetes.client.models.v1_event_list.V1EventList()


if __name__ == '__main__':
    unittest.main()
