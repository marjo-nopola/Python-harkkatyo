"""
    TTC2030 Ohjelmoinnin perusteet
    Marjo Nopola
    AA9074

    26.2.2021
    Harjoitustyö
    
"""
try:
    import datetime
    from workout import Workout
    from files import *

    today = datetime.datetime.now()
    print("Hello! Add your gym workouts.")
    print("Today is", today.strftime("%a %d.%m.%Y.")) # Tue 23.02.2021
    print("Press 't' to add workout for today. Press 'a' to add workout for another day.")
    
    # ask workout day (today == 't' or another day == 'a')
    ans = -1
    while ans < 0:
        day = input("Enter t/a: ")
        day = day.lower()
        if day == "a":
            #date = input("Give workout date (dd.mm.yyyy): ")
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            date = datetime.date(year, month, day)
            date = date.strftime("%Y.%m.%d")
            ans += 1
        elif day == "t":
            #date = today.strftime("%d.%m.%Y") # 23.02.2021
            date = today.strftime("%Y.%m.%d")
            ans += 1
        else:
            print("Wrong input.")

    # ask split name and convert to upper characters
    split = input("Give workout split (push/pull/legs/random): ")
    split = split.upper()

    name = "xxx"    
    kg = 0.00
    reps = 0
    wo_list = []

    # ask workout name, kg and reps and add Workout objects to list
    while name != "":
        name = input("Give workout name (Empty to end this workout session): ")
        if name != "":            
            kg = input("Give weight (kg): ")
            reps = input("Give workout reps: ")
            wo = Workout(date, split, name, kg, reps)
            wo_list.append(wo)
   
    # workout list is saved in function save_workout
    save_workout(wo_list, "a")

    # print added workouts
    print("Added workouts: ")         
    for wo in wo_list:
        print(wo)
    
    print("--------------------------------------------------------------------------")
    # all split workouts are printed in function print_workouts
    print_workouts(split)

except:
    print("Oh no...something went wrong")


