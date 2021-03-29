from sqlite_utils import Database

db = Database("cat_database.db")

# This line creates a "cats" table if one does not already exist:
db["cats"].insert_all([
    {"id": 1, "age": 4, "name": "Mittens"},
    {"id": 2, "age": 2, "name": "Fluffy"}
], pk="id")