GRAB_SPIDER_CONFIG = {
    'global': {
        'spider_modules': [
            'spider.wingsdata',
        ],
        #'cache': {
        #    'backend': 'mongodb',
        #    'database': 'wingsdata_cache',
        #},
        #'proxy_list': {
        #    'source': '/web/proxy.txt',
        #    'source_type': 'text_file',
        #},

    },
}

MONGODB = {
    'connection': {},
    'dbname': 'wingsdata',
}

try:
    from project.settings_local import *
except ImportError:
    pass
