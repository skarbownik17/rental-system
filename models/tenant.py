class Tenant:
    def __init__(self, name, surname, room):
        self.name = name
        self.surname = surname
        self.room = room

    def __str__(self):
        return f"{self.name} {self.surname} - {self.room}"
