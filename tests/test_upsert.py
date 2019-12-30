def test_upsert(fresh_db):
    table = fresh_db["table"]
    table.insert({"id": 1, "name": "Cleo"}, pk="id")
    table.upsert({"id": 1, "age": 5}, pk="id", alter=True)
    assert [{"id": 1, "name": "Cleo", "age": 5}] == list(table.rows)


def test_upsert_all(fresh_db):
    table = fresh_db["table"]
    table.upsert_all([{"id": 1, "name": "Cleo"}, {"id": 2, "name": "Nixie"}], pk="id")
    table.upsert_all([{"id": 1, "age": 5}, {"id": 2, "age": 5}], pk="id", alter=True)
    assert [
        {"id": 1, "name": "Cleo", "age": 5},
        {"id": 2, "name": "Nixie", "age": 5},
    ] == list(table.rows)
    assert 2 == table.last_pk
