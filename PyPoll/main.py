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
        total
        
        if row[3] not in candidates:
            candidates.append(row[3])
            candidate_votes[row[3]] = 1
        else:
            candidate_votes[row[3]] = candidate_votes[row[3]] + 1

    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:", len(votes))
    print("-----------------------------------")
    

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes) * 100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes) *100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")

    winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

    print("-----------------------------------")
    print("Winner: " + str(winner[0]))
    print("-----------------------------------")

with open(output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))
