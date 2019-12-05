import csv

from customerio import CustomerIO


class CustomerIOWrapper(object):
    def __init__(self, site_id, api_key):
        self.cio = CustomerIO(site_id, api_key)
    
    def remove_bulk(self, filename):
        with open(filename) as f:
            reader = csv.DictReader(f, delimiter=',')
            items = list(reader)
            item_count = len(items)
            
            if not items:
                print(f'No rows to delete: {filename}')
                return False

            if 'id' not in items[0]:
                print(f'id column not exists in the file {filename}')
                return False

            for idx, item in enumerate(items):
                if 'id' not in item:
                    continue
                
                try:
                    cio.delete(customer_id=item['id'])
                    item_label = item['email'] if 'email' in item else item['id']
                    item_percent = round((idx / item_count) * 100, 2)
                    print(f'{idx_percent}% DELETE ({idx} of {item_count}): {item_label}')
                except Exception as e:
                    print(f'Exception: {e}')
            
            return True
