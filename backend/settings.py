# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'new_database_name',    # Replace with your database name
        'USER': 'postchess',      # Replace with your PostgreSQL username
        'PASSWORD': 'lichess',  # Replace with your PostgreSQL password
        'HOST': 'localhost',             # Or the IP address of your PostgreSQL server
        'PORT': '5432',                  # Default PostgreSQL port, change if needed
    }
}
