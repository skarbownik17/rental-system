import json
from models.tenant import Tenant
from models.room import Room

def load_data(filename='data/tenants.json'):
    try:
        with open(filename, 'r') as f:
            raw = json.load(f)
            return [Tenant(r['name'], r['surname'], Room(r['room']['number'], r['room']['rent'])) for r in raw]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(tenants, filename='data/tenants.json'):
    data = [
        {
            "name": t.name,
            "surname": t.surname,
            "room": {"number": t.room.number, "rent": t.room.rent}
        }
        for t in tenants
    ]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
