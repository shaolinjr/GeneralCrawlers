
# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_DBNAME =  'admin'
DOMAIN = {
    'attractions':{
        'schema': {
            'attraction_name': {
                'type': 'string',
            },
            'park_name': {
                'type':'string'
            },
            'attraction_type':{
                'type': 'string'
            }
            #attraction_image
        },
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'park_name'
        }
    },
    'dinings':{
        'schema':{
            'dining_name':{
                'type':'string'
            },
            'park_name':{
                'type': 'string'
            },
            'dining_image':{
                'type':'media'
            }
        },

        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'park_name'
        }

    }

}

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
# ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# PAGINATION = False
# PAGINATION_LIMIT = 199
# PAGINATION_DEFAULT = 199