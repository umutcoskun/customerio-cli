import csv
import json

import requests
from customerio import CustomerIO


class CustomerIOWrapper(object):
    BASE_URL = 'https://beta-api.customer.io/v1/api'

    def __init__(self, site_id, api_key):
        self.site_id = site_id
        self.api_key = api_key
        self.cio = CustomerIO(site_id, api_key)

    def fetch(self, uri, payload):
        response = requests.get(
            self.BASE_URL + uri,
            data=payload,
            auth=(self.site_id, self.api_key),
        )
        return response

    def get_messages(self, message_type=None):
        payload = {
            'type': message_type,
        }
        response = self.fetch('/messages', payload)
        data = json.loads(response.content)
        return data.get('messages')

    def remove_bulk(self, filename):
        with open(filename) as f:
            reader = csv.DictReader(f, delimiter=',')
            items = list(reader)
            item_count = len(items)

            if not items:
                print(f'Error: no rows to in the file: {filename}')
                return False

            if 'id' not in items[0]:
                print(f'Error: id column not exists in the file: {filename}')
                return False

            for idx, item in enumerate(items):
                if 'id' not in item:
                    continue

                try:
                    self.cio.delete(customer_id=item['id'])
                    item_label = item['email'] if 'email' in item else item['id']
                    item_percent = round((idx / item_count) * 100, 2)
                    print(f'{item_percent}% DELETE ({idx} of {item_count}): {item_label}')
                except Exception as e:
                    print(f'Exception: {e}')

            return True
