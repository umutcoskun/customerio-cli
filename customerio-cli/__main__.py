import csv
import sys

from . import CustomerIOWrapper
from optparse import OptionParser

def main(argv):
    """ ZAFAF
    site_id = 'c70ba869be43f6fef670'
    api_key = 'cc942b3501591786c8b4'
    """

    """ DUGUN
    site_id = '78a2837e7f049f9a9b65'
    api_key = 'e4c8050a93437883d219'
    """

    parser = OptionParser()
    parser.add_option('-id', dest='site_id', default='78a2837e7f049f9a9b65', help='Site ID')
    parser.add_option('-key', dest='api_key', default='e4c8050a93437883d219', help='API Key')
    parser.add_option('-delete', dest='delete', default=None, help='Delete customers in a CSV file that contains id column.')
    opts, args = parser.parse_args()

    app = CustomerIOWrapper(parser.site_id, parser.api_key)

    if parser.delete:
        app.remove_bulk(parser.delete)


if __name__ == '__main__':
    main(sys.argv)