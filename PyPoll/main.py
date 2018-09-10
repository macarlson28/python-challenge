import os
import csv


csvpath = os.path.join("..", "ElectionResources", "election_data.csv")
output = "myoutput.txt"

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader) 
    
    votes = 0
    candidates = []
    candidate_votes = {}
    total_candidates = 0
   

    for row in csvreader:
        
        votes = votes + 1
        total_candidates
        
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1

    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:", str(votes))
    print("-----------------------------------")
    

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes) * 100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes) *100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")

    winner = max(candidates,key=candidates.count)

    print("-----------------------------------")
    print("Winner: " + str(winner))
    print("-----------------------------------")


with open(output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    
