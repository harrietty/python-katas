import re
from datetime import datetime, time
import pytz

class Mongo(object):
    def is_valid(id):
        if not isinstance(id, str):
            return False
        return True if re.match(r'^[0-9a-f]{24}$', id) else False
    
    def get_timestamp(id):
        if Mongo.is_valid(id):
            return datetime.fromtimestamp(int(id[0:8], 16))
        else:
            return False