# flake8: noqa

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import gun
from .base import *

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True


# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

sentry_sdk.init(
    dsn=config("SENTRY_DSN", default=""),
    environment=gun_ENVIRONMENT,
  #  release="gun@%s" % gun.__version__,
    release="gun@1.0.0",
    integrations=[DjangoIntegration()],
)
# ==============================================================================
# DATABASE SETTINGS
# ==============================================================================

import dj_database_url
import os

# Database from environment variable
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# Static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATIC_ROOT = BASE_DIR / 'staticfiles'

import os

# Add this near the end of the file
PORT = int(os.environ.get('PORT', 8000))

# Make sure ALLOWED_HOSTS includes your Railway domain
ALLOWED_HOSTS = [
    'gun-production.up.railway.app',
    '.railway.app',
    'localhost',
    '127.0.0.1',
]


