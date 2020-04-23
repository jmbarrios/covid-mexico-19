REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'covid_api.pagination.CustomPaginator',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'covid_api.renderers.CSVRenderer',
    ],
    'PAGE_SIZE': 100,
}

COVID_API_APPS = [
    'covid_api.apps.CovidApiConfig',
    'drf_yasg',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'crispy_forms',
]

ORDERING_PARAM = 'ordenar'
