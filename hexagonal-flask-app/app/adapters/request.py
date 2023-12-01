from flask import request

def http_request_to_app_request(http_request):
    """
    This function converts an HTTP request to an application request.
    """
    app_request = {}
    app_request['method'] = http_request.method
    app_request['args'] = http_request.args
    app_request['form'] = http_request.form
    app_request['data'] = http_request.data
    app_request['cookies'] = http_request.cookies
    app_request['headers'] = http_request.headers
    return app_request