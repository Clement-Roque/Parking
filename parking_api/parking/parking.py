import flask
from .utils.services.parking_services import ParkingServices
from .utils.ressources import meta_data

parking_bp = flask.Blueprint('parking', __name__)


@parking_bp.route('/parking/<parking_label>')
def parking_by_label(parking_label: str):

    if (parking_label in meta_data.labels_to_filenames.keys()):
        parking_service = ParkingServices()

        return flask.jsonify(parking_service.get_by_parking_label(parking_label).to_json())
    else:
        flask.abort(404)