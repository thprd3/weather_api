# Konfigurasjon for vaer-api
import os
DEBUG = True

# Hemmeligheter hentes na fra miljovariabler
API_KEY = os.environ.get("API_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
