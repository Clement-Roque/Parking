import datetime
import pytest
from model.parking import Parking
from services.parking_services import ParkingServices
import ressources.meta_data as meta_data


@pytest.fixture
def parking_services_test() -> ParkingServices:
    return ParkingServices()

def test_get(parking_services_test: ParkingServices):

    parking_to_test = parking_services_test.get("Antigone")

    assert parking_to_test
    assert isinstance(parking_to_test, Parking)
    assert parking_to_test is not None

    assert parking_to_test.last_update is not None
    assert isinstance(parking_to_test.last_update, datetime.datetime)
    assert parking_to_test.free is not None
    assert isinstance(parking_to_test.free, int)
    assert parking_to_test.name is not None
    assert isinstance(parking_to_test.name, str)
    assert parking_to_test.status is not None
    assert isinstance(parking_to_test.status, str)
    assert parking_to_test.total is not None
    assert isinstance(parking_to_test.total, int)

    assert parking_to_test.free <= parking_to_test.free
    assert parking_to_test.status in ['Open', 'Closed']

def test_get_all(parking_services_test: ParkingServices):

    parkings = parking_services_test.get_all()

    assert len(parkings) == len(meta_data.labels_to_filenames)

    for parking_to_test in parkings:

        assert parking_to_test
        assert isinstance(parking_to_test, Parking)
        assert parking_to_test is not None

        assert parking_to_test.last_update is not None
        assert isinstance(parking_to_test.last_update, datetime.datetime)
        assert parking_to_test.free is not None
        assert isinstance(parking_to_test.free, int)
        assert parking_to_test.name is not None
        assert isinstance(parking_to_test.name, str)
        assert parking_to_test.status is not None
        assert isinstance(parking_to_test.status, str)
        assert parking_to_test.total is not None
        assert isinstance(parking_to_test.total, int)
        assert parking_to_test.label is not None
        assert isinstance(parking_to_test.label, str)

        assert parking_to_test.free <= parking_to_test.free
        assert parking_to_test.status in ['Open', 'Closed']
        assert parking_to_test.label in meta_data.labels_to_filenames.keys()
