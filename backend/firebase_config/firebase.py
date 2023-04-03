import os

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate(os.environ.get("FIREBASE_CREDENTIALS_PATH"))
firebase_app = firebase_admin.initialize_app(cred)
