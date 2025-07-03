from models.tenant import Tenant
from models.room import Room
from utils.file_manager import load_data, save_data
from utils.filters import filter_by_rent
from utils.validators import validate_float

tenants = load_data()

def menu():
    while True:
        print("\n--- SYSTEM ZARZĄDZANIA WYNAJMEM ---")
        print("1. Dodaj najemcę")
        print("2. Wyświetl najemców")
        print("3. Zmień czynsz najemcy")
        print("4. Filtruj wg czynszu")
        print("5. Zapisz dane")
        print("6. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == '1':
            name = input("Imię: ")
            surname = input("Nazwisko: ")
            rent = validate_float("Czynsz (zł): ")
            room_no = input("Nr pokoju: ")
            tenant = Tenant(name, surname, Room(room_no, rent))
            tenants.append(tenant)
        elif choice == '2':
            for t in tenants:
                print(t)
        elif choice == '3':
            surname = input("Podaj nazwisko najemcy do zmiany: ")
            for t in tenants:
                if t.surname == surname:
                    t.room.rent = validate_float("Nowy czynsz: ")
        elif choice == '4':
            threshold = validate_float("Maksymalny czynsz: ")
            filtered = filter_by_rent(tenants, threshold)
            for t in filtered:
                print(t)
        elif choice == '5':
            save_data(tenants)
        elif choice == '6':
            break
        else:
            print("Nieprawidłowa opcja.")

if __name__ == "__main__":
    menu()
