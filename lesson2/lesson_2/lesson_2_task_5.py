def month_to_season():
    month_input = input("Enter the number of the month (1-12): ")
    try:
        month = int(month_input)
        if month in (12, 1, 2):
            print("Winter")
        elif month in (3, 4, 5):
            print("Spring")
        elif month in (6, 7, 8):
            print("Summer")
        elif month in (9, 10, 11):
            print("Autumn")  # Исправлено с "Outom" на "Autumn"
        else:
            print("Invalid month number. Please enter a number between 1 and 12.")
    except ValueError:
        print("Please enter a valid integer.")

# Вызов функции
month_to_season()