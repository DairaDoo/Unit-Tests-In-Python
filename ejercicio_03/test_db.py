import pytest
from db import Database

@pytest.fixture
def db():
    "Create a fresh instance of the Database class and cleans after the test"
    database = Database()
    yield database
    database.data.clear() # used in real databases to clean up (not needed for in-memory)
def test_add_user(db):
    db.add_user("1", "Maria")
    assert db.get_user("1") == "Maria"

def test_add_duplicate_user(db):
    db.add_user("1", "Maria")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user("1", "Javier")

def test_delete_user(db):
    db.add_user("2", "Jose")
    db.delete_user("2")
    assert db.get_user("2") is None