myfile = "workouts.txt"

def sortbydates(myfile):
    file = open(myfile, "r")
    newfile = open("workouts_by_date.txt", "w")
    lines = file.readlines()
    lines.sort() # sort ascending
    newfile.writelines(lines)

# print split workouts from 'workouts.txt'
# there should be at least one because user just entered it
def print_workouts(split):    
    file = open(myfile, "r")
    wo_lines = file.readlines()
    wo_lines.sort()
    print("All", split, "workouts saved in file 'workouts.txt':")
    for wo in wo_lines:
        wo = wo.replace("\n", "") # remove extra line breaks 
        if wo.find(split) > -1:   # split found
            print(wo)
    file.close()

# save workouts from 'wo_list' to file 'workouts.txt'
def save_workout(wo_list, how): 
    if how == "a":
        file = open(myfile, "a")
        total = len(wo_list)
        i = 0
    
        while i < total:        
            file.write(str(wo_list[i]) + "\n")
            i += 1
        file.close()

        sortbydates(myfile)
        