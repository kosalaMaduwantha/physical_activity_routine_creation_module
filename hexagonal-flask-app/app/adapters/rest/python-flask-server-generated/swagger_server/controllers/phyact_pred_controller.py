import connexion
import six

from swagger_server.models.predict_physical_act import PredictPhysicalAct  # noqa: E501
from swagger_server.models.predict_physical_act_response_body201 import PredictPhysicalActResponseBody201  # noqa: E501
from swagger_server.models.predict_physical_act_response_body400 import PredictPhysicalActResponseBody400  # noqa: E501
from swagger_server.models.predict_physical_act_response_body500 import PredictPhysicalActResponseBody500  # noqa: E501
from swagger_server import util


def api_v1_physical_act_prediction_post(body):  # noqa: E501
    """predict the physical activities

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: PredictPhysicalActResponseBody201
    """
    if connexion.request.is_json:
        body = PredictPhysicalAct.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
