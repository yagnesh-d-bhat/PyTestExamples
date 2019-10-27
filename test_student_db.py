from student_db import StudentDB
import pytest


# Can also use test_setup and test_teardown instead of a fixture used below, though fixture is leaner
@pytest.fixture(scope='module')
def db():
    print("--------setup----------")
    db = StudentDB()
    db.connect('data.json')
    yield db
    print("--------teardown----------")
    db.close()


def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark_data(db):
    scott_data = db.get_data('Mark')
    assert scott_data['id'] == 2
    assert scott_data['name'] == 'Mark'
    assert scott_data['result'] == 'fail'
