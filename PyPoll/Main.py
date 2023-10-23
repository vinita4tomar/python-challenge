import os
import csv

'Initialize variables'
total_votes = 0
candidates = {}
winner_vote = 0


election_csv = os.path.join("Resources", "election_data.csv")

'Open file to read and analyze data'
with open(election_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates.update({candidate_name : 1})
        else: 
            candidates[candidate_name] += 1


'Write results to terminal and text file'
output_path = os.path.join("Analysis", "pollResults.txt")

with open(output_path, "w", newline = '\n') as txt_file:

    str_output = "Election Results" + '\n'
    txt_file.write(str_output + '\n')
    print(str_output)

    str_output_break = "------------------------------------" + '\n'
    txt_file.write(str_output_break + '\n')
    print(str_output_break)

    str_output = "Total Votes: " + str(total_votes) + '\n'
    txt_file.write(str_output + '\n')
    txt_file.write(str_output_break  + '\n')
    print(str_output)
    print(str_output_break)
    
    for candidate in candidates:
        votes = candidates[candidate]
        votes_percent = format((votes / total_votes), ".03%")

        if winner_vote < votes:
            winner_vote = votes
            winner_name = candidate

        str_output = f'{candidate} : {votes_percent} ( {votes} ) \n'
        txt_file.write(str_output + '\n')
        print(str_output)

    txt_file.write(str_output_break + '\n')
    print(str_output_break)

    str_output = f'Winner: {winner_name} \n'
    txt_file.write(str_output + '\n')
    print(str_output)

    txt_file.write(str_output_break + '\n')
    print(str_output_break)
