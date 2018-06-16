import json as JSON
import requests

class JSONRequest(object):

    """
    Get request from url and decoded the content.
    """
    def request_from_url(url):
        request = requests.get(url)
        content = request.content
        decoded_content = content.decode("utf8")
        return decoded_content

    """
    Loads Json request content's.
    """
    def parse_json_request(url):
        content = JSONRequest.request_from_url(url)
        content_in_json = JSON.loads(content)
        return content_in_json

    """
    Generalization of a request.
    """
    def fetch(url):
        return JSONRequest.parse_json_request(url)
