class Room:
    def __init__(self, number, rent):
        self.number = number
        self.rent = rent

    def __str__(self):
        return f"Pokój {self.number}, Czynsz: {self.rent} zł"
