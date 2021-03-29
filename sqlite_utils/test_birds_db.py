
from sqlite_utils import Database

db = Database("bird_database.db")

# This creates a "birds" table if one does not already exist:
db["birds"].insert_all([
    {"id": 1, "age": 4, "name": "Buzzy"},
    {"id": 2, "age": 2, "name": "Chirpy"}
], pk="id")

