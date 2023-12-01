from flask import jsonify

class ResponseAdapter:
    @staticmethod
    def to_http_response(data, status_code=200):
        """
        Converts the application's response into an HTTP response.
        """
        return jsonify(data), status_code