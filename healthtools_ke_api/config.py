import os

MEMCACHED_URL = os.getenv('MEMCACHED_URL', '127.0.0.1:11211')
GA_TRACKING_ID = os.environ.get('GA_TRACKING_ID', 'UA-44795600-33')