REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
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
