from flask import jsonify

INVALID_FIELD_NAME_SENT_422 = {
    "http_code": 422,
    "code": "invalidField",
    "message": "Invalid fields found"
}
INVALID_INPUT_422 = {
    "http_code": 422,
    "code": "invalidInput",
    "message": "Invalid input"
}
MISSING_PARAMETERS_422 = {
    "http_code": 422,
    "code": "missingParameter",
    "message": "Missing parameters."
}
BAD_REQUEST_400 = {
    "http_code": 400,
    "code": "badRequest",
    "message": "Bad request"
}
UNAUTHORIZED_401 = {
    "http_code": 401,
    "code": "unauthorized",
    "message": "Token expired"
}
SERVER_ERROR_500 = {
    "http_code": 500,
    "code": "serverError",
    "message": "Server error"
}
SERVER_ERROR_404 = {
    "http_code": 404,
    "code": "notFound",
    "message": "Resource not found"
}
UNAUTHORIZED_403 = {
    "http_code": 403,
    "code": "notAuthorized",
    "message": "You are not authorised to execute this."
}
CONFLICT_409 = {
    "http_code": 409,
    "code": "resourceConflict",
    "message": "Conflict with the current state of the resource"
}
SUCCESS_200 = {
    'http_code': 200,
    'code': 'success'
}
SUCCESS_201 = {
    'http_code': 201,
    'code': 'success'
}
SUCCESS_204 = {
    'http_code': 204,
    'code': 'success'
}


def response_with(status, value=None, message=None):
    data = {}

    # if value != None and not isinstance(value, dict):
    #     raise Exception(f"dict wasnt provided. Value: {type(value)}")
    if value != None:
        data['data'] = value

    data['status'] = status['code']

    if message != None and isinstance(message, str):
        data['message'] = message
    elif status.get("message"):
        data['message'] = status['message']

    return jsonify(data), status["http_code"]