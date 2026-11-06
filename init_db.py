
import sys

from app import app
from models import db

with app.app_context():
    if '--reset' in sys.argv:
        db.drop_all()
        db.create_all()
        print('Database recreated (all previous posts deleted).')
    else:
        db.create_all()
        print('Database ready (existing data kept). Use --reset to wipe it.')