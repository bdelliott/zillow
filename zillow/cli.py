import argparse
import ConfigParser
import os
import xml.dom.minidom

import requests


class Zillow(object):

    def __init__(self):
        parser = ConfigParser.RawConfigParser()
        parser.read([os.path.expanduser("~/.zillow.ini")])
        self.zwsid = parser.get('DEFAULT', 'zwsid')
        
    def search(self, address, citystatezip):
        url = 'http://www.zillow.com/webservice/GetSearchResults.htm'
        params = {
            'zws-id': self.zwsid,
            'address': address,
            'citystatezip': citystatezip
        }
        r = requests.get(url, params=params)
        print r.url
        print "-" * 80
        print "Status code: %d" % r.status_code
        print "-" * 80
        doc = xml.dom.minidom.parseString(r.text)
        print doc.toprettyxml()


def main():
    parser = argparse.ArgumentParser(description='Interact with Zillow API.')
    parser.add_argument('action', choices=['search'], help='Action to take')
    parser.add_argument('--address', help='Address to search')
    parser.add_argument('--citystatezip', help='City state zip to search')

    args = parser.parse_args()

    zillow = Zillow()

    # do a property search
    if args.action == 'search':
        if not args.address:
            raise Exception("Need address to search")
        if not args.citystatezip:
            raise Exception("Need citystatezip to search")

        zillow.search(args.address, args.citystatezip)

