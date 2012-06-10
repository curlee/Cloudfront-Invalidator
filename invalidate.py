import sys
import datetime
from boto.cloudfront import CloudFrontConnection
import settings

class Invalidate():
    def do_invalidation(self):
        files = sys.argv[1:]
        if len(files) > 0:
            print 'Sending invalidation request for the following files:'
            for f in files:
                print f
                conn = CloudFrontConnection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_ACCESS_KEY)
                req = conn.create_invalidation_request(settings.AWS_CF_DISTRIBUTION_ID, files)
                print req.status
        else:
            self.help()
        sys.exit()
    
    def help(self):
        print 'Usage: invalidate.py [file 1] [file 2] [file 3] [...]'

i = Invalidate()
i.do_invalidation()