from flask import Blueprint
from flask import jsonify
from src.functionality.identity import upsert_contact
from src.helper import parse_request_data
from src.resources.serializer import serialize_contact_data


identify = Blueprint("identity", __name__)


@identify.route("/identify", methods=["POST"])
def upsert_contact_api():
    request_data = parse_request_data()
    response, status_code = upsert_contact(request_data)
    if status_code == 200: 
       return jsonify(serialize_contact_data(response)), status_code
    return jsonify(response), status_code