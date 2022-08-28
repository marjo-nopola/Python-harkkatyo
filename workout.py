# declare a workout class to hold information about workout data
class Workout:
    def __init__(self, date = "", split = "", name = "", weight = 0.00, reps = 0):
        self.date = date
        self.split = split
        self.name = name
        self.weight = weight
        self.reps = reps

    # override conversion from Workout to string with __str__
    def __str__(self):
        return self.date + " " + self.split + ": " + self.name + " " + str(self.weight) + " kg " + str(self.reps) + " reps"

    date = ""
    split = ""
    name = ""
    weight = 0.00
    reps = 0

    

    