REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'covid_api.pagination.CustomPaginator',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'PAGE_SIZE': 100,
}

COVID_API_APPS = [
    'covid_api.apps.CovidApiConfig',
    'drf_yasg',
    'rest_framework',
    'django_filters',
    'crispy_forms',
]
