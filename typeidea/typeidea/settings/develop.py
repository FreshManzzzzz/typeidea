from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# INSTALLED_APPS += [
#     'debug_toolbar',
#     # 'pympler',
#     # 'debug_toolbar_line_profiler',
#     # 'silk',
# ]

# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
#     # 'silk.middleware.SilkyMiddleware',
# ]

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
