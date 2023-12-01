import connexion
import six
import sys
sys.path.append('/home/kosala/git-rep/physical_activity_routine_creation_module/hexagonal-flask-app/')
from app.domain.api.dtos.models import phyActData
from app.adapters.db.mysql_adapter import MySQLAdapter
from app.domain.services.physical_act_impl import PhysicalActImpl
from swagger_server.models.predict_physical_act import PredictPhysicalAct  # noqa: E501
from swagger_server.models.predict_physical_act_response_body201 import PredictPhysicalActResponseBody201  # noqa: E501
from swagger_server.models.predict_physical_act_response_body400 import PredictPhysicalActResponseBody400  # noqa: E501
from swagger_server.models.predict_physical_act_response_body500 import PredictPhysicalActResponseBody500  # noqa: E501
from swagger_server import util

db_sp = MySQLAdapter()
phyActService = PhysicalActImpl(db_sp)

def api_v1_physical_act_prediction_post(body):  # noqa: E501
    """predict the physical activities

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: PredictPhysicalActResponseBody201
    """
    if connexion.request.is_json:
        data = phyActData(**connexion.request.get_json())
    
    phyActService.predict_physical_activities(data)
    
    return 'do some magic!'
