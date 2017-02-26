
# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_DBNAME =  'admin'
DOMAIN = {
    'user': {
        'schema': {
            'firstname': {
                'type': 'string'
            },
            'lastname': {
                'type': 'string'
            },
            'username': {
                'type': 'string',
                 'unique': True
            },
            'password': {
                'type': 'string'
            },
            'phone': {
                'type': 'string',
                'unique':True
            },
            'additional_lookup': {
                'url': 'regex("[\w]+")',
                'field': 'username',
            }
        }
    },
    'item': {
        'schema': {
            'name': {
                'type': 'string'
            },
            'username': {
                'type': 'string'
            }
        }
    }

}

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE', 'PATCH']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

