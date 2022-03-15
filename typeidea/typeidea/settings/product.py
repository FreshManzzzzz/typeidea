from .base import *  # NOQA

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'CONN_MAX_AGE': 60,
        'OPTIONS': {'charset': 'utf8mb4'}
    },
}

ADMINS = MANAGERS = {
    ('shj', '1027118385@qq.com'),
}

# 配置邮件服务
# EMAIL_HOST = ''
# EMAIL_HOST_USER = 'the5fire'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_SUBJECT_PREFIX = ''
# DEFAULT_FROM_EMAIL = ''
# SERVER_EMAIL = ''

# 配置django-redis
REDIS_URL = 'redis://127.0.0.1:6379/1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            # 'PASSWORD': '<对应密码>',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}

# 配置线上环境 DEBUG=False时的静态文件获取路径
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_files/')
STATIC_ROOT = '../static_files'
# 配置日志

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        # 'file': {
        #     'level': 'INFO',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': 'tmp/logs/typeidea.log',
        #     'formatter': 'default',
        #     'maxBytes': 1024 * 1024,  # 1M
        #     'backupCount': 5,
        # },

    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

# INSTALLED_APPS += [
#     'debug_toolbar',
#     # 'pympler',
#     # 'debug_toolbar_line_profiler',
#     # 'silk',
# ]
#
# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
#     # 'silk.middleware.SilkyMiddleware',
# ]
#
# INTERNAL_IPS = ['127.0.0.1']
# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js',
#     'SHOW_COLLAPSED': True,
#     'SHOW_TOOLBAR_CALLBACK': lambda x: True,
# }


# DEBUG_TOOLBAR_PANELS = [
#     # 'djdt_flamegraph.FlamegraphPanel',
#     # 'pympler.panels.MemoryPanel',
#     # 'debug_toolbar_line_profiler.panel.ProfilingPanel',
# ]
