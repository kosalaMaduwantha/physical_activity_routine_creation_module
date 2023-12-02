# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.get_physical_act_response_body201 import GetPhysicalActResponseBody201  # noqa: E501
from swagger_server.models.physical_act_response_body400 import PhysicalActResponseBody400  # noqa: E501
from swagger_server.models.physical_act_response_body500 import PhysicalActResponseBody500  # noqa: E501
from swagger_server.models.predict_physical_act import PredictPhysicalAct  # noqa: E501
from swagger_server.models.predict_physical_act_response_body201 import PredictPhysicalActResponseBody201  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPhyactPredController(BaseTestCase):
    """PhyactPredController integration test stubs"""

    def test_api_v1_physical_act_prediction_get(self):
        """Test case for api_v1_physical_act_prediction_get

        get the predicted physical activities
        """
        query_string = [('user_id', 789)]
        response = self.client.open(
            '//api/v1/physical_act/prediction',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_physical_act_prediction_post(self):
        """Test case for api_v1_physical_act_prediction_post

        predict the physical activities
        """
        body = PredictPhysicalAct()
        response = self.client.open(
            '//api/v1/physical_act/prediction',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
