#!/usr/bin/env python

# source:
# http://santini.dsi.unimi.it/extras/ph/quick-and-dirty-backup-of-your-facebook-statuses.html

from json import loads
from urllib2 import urlopen
from sys import argv

next = 'https://graph.facebook.com/me/statuses?access_token=' + argv[ 1 ]
while next:
        url = urlopen( next )
        data = loads( url.read() )
        for msg in data[ 'data' ]:
                print msg[ 'updated_time' ], msg[ 'message' ].encode('utf-8')
        try:
                next = data[ 'paging' ][ 'next' ]
        except KeyError:
                next = None

