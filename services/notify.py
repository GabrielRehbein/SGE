import requests


class Notify:

    def __init__(self):
        self.__base_url = 'http://localhost:8001/'

    def send_sale_event(self, data):
        url = f'{self.__base_url}api/v1/webhooks/sale/'
        requests.post(
            url=url,
            json=data,
        )
