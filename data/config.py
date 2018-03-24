# SQL-Alchemy Settings
SQLALCHEMY_DATABASE_URI = "sqlite:////data/dudel.db" # DO NOT USE RELATIVE PATHS IF USING MIGRATION!!!
SQLALCHEMY_ECHO = False

# Home button in menu bar
BRAND_TEXT = "Dudel"
HOME_URL = "http://example.org"
HOME_TEXT = "Dudel"
FOOTER_LINKS = [
    ('Imprint', 'http://example.org')
]

# Debug mode, set to False in productive environment
DEBUG = False

# Secret key, required for cookies etc.
SECRET_KEY = "48723z48s2hns82zs4hz29sh4283472yjnjy8346n"

# Select which authentication method to use.
LOGIN_PROVIDERS = ["password"]

# Used only if "password" in LOGIN_PROVIDERS
REGISTRATIONS_ENABLED = True

# Enable group features (create/edit)
GROUPS_ENABLED = True

# Used only if "ldap" in LOGIN_PROVIDERS
LDAP = dict(
    HOST = 'ldap://localhost',
    BASE_DN = 'dc=example,dc=com',
    GLOBAL = dict(
        BIND_DN = 'cn=dudel,dc=example,dc=com',
        PASSWORD = '123456'
    ),
    GROUP = dict(
        ATTRIBUTES = dict(
            IDENTIFIER = 'id',
            NAME = 'cn',
            MEMBERS = 'members'
        ),
        DN = 'ou=groups,dc=example,dc=com',
        FILTER = '(objectClass=posixGroup)'
    ),
    USER = dict(
        BIND_DN = 'uid={username},ou=people,dc=example,dc=com',
        DN = 'uid={username},ou=people,dc=example,dc=com'
    ),
    REGISTER_URL = "https://example.com/register"
)

# Sentry settings
# The Sentry DSN, if it is not set or False Sentry is disabled
# SENTRY_DSN = "https://user:password@sentry.host.tld/X"

MAIL_SERVER = "mail.example.org"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_DEBUG = False
MAIL_USERNAME = "mail@example.org"
MAIL_PASSWORD = "exampleorg"
MAIL_DEFAULT_SENDER = "Dudel <%s>" % MAIL_USERNAME
TESTING = False

# How user's display name is created
# May contain fields: firstname, lastname, username, email
NAME_FORMAT = "%(firstname)s (%(username)s)"

# Allow customization of slugs
ALLOW_CUSTOM_SLUGS = True

# Generate random slugs by default
RANDOM_SLUGS = False

# Usernames of administrators
# e.g. ["13musterm", "14musterf"]
ADMINS = ["example"]

# Timezone
DEFAULT_TIMEZONE = "Europe/Berlin"

# Locale
BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_TIMEZONE = DEFAULT_TIMEZONE

# recaptcha
RECAPTCHA_USE_SSL = True
RECAPTCHA_PUBLIC_KEY = ""
RECAPTCHA_PRIVATE_KEY = ""
RECAPTCHA_OPTIONS = {"theme_name": "white"}

# CSRF protection: Should the CSRF token be consumed when checked? This prevents
# sensible actions that are protected against CSRF in multiple tabs.
CSRF_CONSUME = False
