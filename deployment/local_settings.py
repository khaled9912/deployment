# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = False

# Make these unique, and don't share it with anybody.
SECRET_KEY = "9i-0s1rr8#sp&(j$0n3t8s*-t23g0!i9&rs)1=!h(cirx3b$x3"
NEVERCACHE_KEY = "#_j9)qpfw_ems2(qt^8pjviw*cdg5@fr)^r1of!6zg=-(7bg*9"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "alexgreen",
        # Not used with sqlite3.
        "USER": "khaledmourad",
        # Not used with sqlite3.
        "PASSWORD": "passwordpostgres",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "database-1.cqutv8fmtcxv.us-east-2.rds.amazonaws.com",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "5432",
    }
}

# Allowed development hosts
ALLOWED_HOSTS = ["alexgreen-eg.herokuapp.com","alexgreen-eg.zeet.app", "127.0.0.1"]


###################
# DEPLOY SETTINGS #
###################

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "DEPLOY_TOOL": "git",  # Deploy with "git", "hg", or "rsync"
#     "REPO_URL":"https://github.com/khaled9912/alexgreen.git",
#     "SSH_USER": "alexgreen",  # VPS SSH username
#     "HOSTS": [""],  # The IP address of your VPS
#     "DOMAINS": [""],  # Will be used as ALLOWED_HOSTS in production
#     "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
#     "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
#     "DB_PASS": "",  # Live database password
#     "ADMIN_PASS": "",  # Live admin user password
#     "SECRET_KEY": "9i-0s1rr8#sp&(j$0n3t8s*-t23g0!i9&rs)1=!h(cirx3b$x3",
#     "NEVERCACHE_KEY": "#_j9)qpfw_ems2(qt^8pjviw*cdg5@fr)^r1of!6zg=-(7bg*9",
# }
#34.221.96.152 (the public IP of your Postgres project)
