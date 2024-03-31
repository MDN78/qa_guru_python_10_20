import json
import logging
import allure
import requests
from curlify import to_curl
from allure_commons._allure import step


def post_request_logger(url, **kwargs):
    with step(f"API-POST: request {url}"):
        response = requests.post(url=url, **kwargs)
        curl = to_curl(response.request)
        logging.info(to_curl(response.request))
        logging.debug(to_curl(response.request))
        logging.info(f'status code: {response.status_code}')
        allure.attach(body=curl, name="curl", attachment_type=allure.attachment_type.TEXT, extension='txt')
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                      name="response",
                      attachment_type=allure.attachment_type.JSON,
                      extension='json')
        return response
