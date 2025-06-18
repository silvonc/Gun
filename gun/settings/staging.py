# flake8: noqa

import gun
from .base import *

# ==============================================================================
# SECURITY SETTINGS - Less strict for staging
# ==============================================================================

CSRF_COOKIE_SECURE = False  # Allow HTTP for staging
CSRF_COOKIE_HTTPONLY = True

SECURE_HSTS_SECONDS = 0  # Disable HSTS for staging
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_SSL_REDIRECT = False  # Allow HTTP for staging
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = False  # Allow HTTP sessions for staging

# ==============================================================================
# DEBUG SETTINGS
# ==============================================================================

DEBUG = True  # Keep True for staging to see detailed errors

# ==============================================================================
# DATABASE SETTINGS
# ==============================================================================

import dj_database_url
import os

# Database from environment variable (can be same as prod or separate)
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# Static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Port configuration
PORT = int(os.environ.get('PORT', 8000))

# Staging allowed hosts - update this URL after creating staging environment
ALLOWED_HOSTS = [
    'gun-staging.up.railway.app',  # Update with actual staging URL
    '.railway.app',
    'localhost',
    '127.0.0.1',
]

# Email backend - print emails to console in staging
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'