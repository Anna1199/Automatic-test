month_to_season=input("num ")
month=int(month_to_season)
if month in (12, 1, 2):
        print("Winter")
elif month in (3, 4, 5):
        print("Spring")
elif month in (6, 7, 8):
        print("Summer")
elif month in (9, 10, 11):
        print("Outom")
else:
        print("What is it?")