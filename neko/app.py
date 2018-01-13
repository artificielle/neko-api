from . import create_app

app = create_app()

# pylint: disable = wrong-import-position
from .models.db_init import db_init
db_init(app)
