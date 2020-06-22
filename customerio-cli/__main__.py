import csv
import sys

from . import CustomerIOWrapper
from optparse import OptionParser

def main(argv):
    parser = OptionParser()
    parser.add_option('--id', dest='site_id', default='', help='Site ID')
    parser.add_option('--key', dest='api_key', default='', help='API Key')
    parser.add_option('--delete', dest='delete', default=None, help='Delete customers in a CSV file that contains id column.')
    opts, args = parser.parse_args()

    app = CustomerIOWrapper(opts.site_id, opts.api_key)

    if not opts.site_id:
        opts.site_id = input('Customer.io Site ID: ').strip()
    
    if not opts.api_key:
        opts.api_key = input('Customer.io API Key: ').strip()

    if opts.delete:
        app.remove_bulk(opts.delete)
    


if __name__ == '__main__':
    main(sys.argv)
