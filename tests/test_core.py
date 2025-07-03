from models.tenant import Tenant
from models.room import Room
from utils.filters import filter_by_rent

def test_filter():
    tenants = [
        Tenant("Jan", "Kowalski", Room("1A", 1500)),
        Tenant("Anna", "Nowak", Room("2B", 1000))
    ]
    filtered = filter_by_rent(tenants, 1200)
    assert len(filtered) == 1
    assert filtered[0].surname == "Nowak"
