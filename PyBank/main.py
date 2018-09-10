import os
import csv


csvpath = os.path.join("..", "Resources", "budget_data.csv")

output = "myoutput.txt"

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader) 
    revenue = []
    date = []
    rev_change = []

    for row in csvreader:

        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total: ", "$", sum(revenue))


    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_change = sum(rev_change)/len(rev_change)

        max_change = max(rev_change)

        min_change = min(rev_change)

        max_change_date = str(date[rev_change.index(max(rev_change))])
        min_change_date = str(date[rev_change.index(min(rev_change))])


    print("Average Change: ", "$", round(avg_change))
    print("Greatest Increase in Profits:", max_change_date,"$", max_change)
    print("Greatest Decrease in Profits:", min_change_date,"$", min_change)

    with open(output, "w") as txt_file:
        txt_file.write("Total Months: " + str(len(date)))
        txt_file.write("\n")
        txt_file.write("Total: " + "$" + str(sum(revenue)))
        txt_file.write("\n")
        txt_file.write("Average Change: " + "$" + str(round(avg_change)))
        txt_file.write("\n")
        txt_file.write("Greatest Increase in Profits: " + str(max_change_date) + " $" + str(max_change))
        txt_file.write("\n")
        txt_file.write("Greatest Decrease in Profits: " + str(min_change_date) + " $" + str(min_change))
