import connexion
import six
import sys
import logging
sys.path.append('/home/kosala/git-rep/physical_activity_routine_creation_module/hexagonal-flask-app/')
from app.domain.api.dtos.models import phyActData
from app.adapters.db.mysql_adapter import MySQLAdapter
from app.domain.services.physical_act_impl import PhysicalActImpl
from swagger_server.models.get_physical_act_response_body201 import GetPhysicalActResponseBody201  # noqa: E501
from swagger_server.models.physical_act_response_body400 import PhysicalActResponseBody400  # noqa: E501
from swagger_server.models.physical_act_response_body500 import PhysicalActResponseBody500  # noqa: E501
from swagger_server.models.predict_physical_act import PredictPhysicalAct  # noqa: E501
from swagger_server.models.predict_physical_act_response_body201 import PredictPhysicalActResponseBody201  # noqa: E501
from swagger_server import util
USER_ID = "user_0001"

logger = logging.getLogger(__name__)

db_sp = MySQLAdapter()
phyActService = PhysicalActImpl(db_sp)


def api_v1_physical_act_prediction_get(user_id):  # noqa: E501
    """get the predicted physical activities

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param user_id: user id of the user
    :type user_id: int

    :rtype: GetPhysicalActResponseBody201
    """
    try:
        activity_list = phyActService.get_physical_activities(user_id)
        output = {
            "prediction": activity_list,
            "status": "prediction success"
        }
        STATUS_CODE = 200
    except Exception as e:
        logger.error(e)
        output = {
            "prediction": None,
            "status": "get failed"
        }
        STATUS_CODE = 500
        
    return output, STATUS_CODE


def api_v1_physical_act_prediction_post(body):  # noqa: E501
    """predict the physical activities

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: PredictPhysicalActResponseBody201
    """
    try:
        if connexion.request.is_json:
            data = phyActData(**connexion.request.get_json())
                
        if USER_ID is not None:
            data.uid = USER_ID
        
        activity_list = phyActService.predict_physical_activities(data)
        
        output = {
            "prediction": activity_list,
            "status": "prediction success"
        }
        STATUS_CODE = 201
    except Exception as e:
        logger.error(e)
        output = {
            "prediction": None,
            "status": "prediction failed"
        }
        STATUS_CODE = 500
    
    return output, STATUS_CODE
