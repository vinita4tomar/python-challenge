import os
import csv

'Initialize variables'
total_months = 0
total_profitLoss = 0
max_profit = 0
max_loss = 0
average_change = 0

bank_csv = os.path.join("Resources", "budget_data.csv")


'Open file to read and analyze data'
with open(bank_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        month_profit = int(row[1])
        total_profitLoss = month_profit + total_profitLoss

        if total_months > 0:
            change_Profit = month_profit - last_month
            average_change = average_change + change_Profit

            if change_Profit > max_profit:
                max_profit = change_Profit
                max_profit_month = row[0]
            if change_Profit < max_loss:
                max_loss = change_Profit
                max_loss_month = row[0]       

        last_month = int(row[1])
        total_months = total_months + 1

average_change = average_change / (total_months - 1)

'Write results to terminal and text file'
output_path = os.path.join("Analysis", "bankResults.txt")

with open(output_path, "w", newline = '\n') as txt_file:

    str_output = "Financial Analysis"
    txt_file.write(str_output + '\n\n')
    print(str_output)

    str_output = "------------------------------------"
    txt_file.write(str_output + '\n\n')
    print(str_output)

    str_output = "Total months: " + str(total_months) 
    txt_file.write(str_output + '\n\n')
    print(str_output)

    str_output = "Total: $" + str(total_profitLoss)
    txt_file.write(str_output + '\n\n')
    print(str_output)

    str_output = "Average Change: $" + str("{:.2f}".format(average_change))
    txt_file.write(str_output + '\n\n')
    print(str_output)

    str_output = "Greatest Increase in Profits: " + max_profit_month + " ($" + str(max_profit) + ")"
    txt_file.write(str_output + '\n\n')
    print(str_output)

    str_output = "Greatest Decrease in Profits: " + max_loss_month + " ($" + str(max_loss) + ")"
    txt_file.write(str_output + '\n\n')
    print(str_output)

