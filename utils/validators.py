def validate_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Wprowadź poprawną liczbę.")
