import os
import csv

budget_data_csv = os.path.join(".", "Starter_Code", "PyBank", "Resources", "budget_data.csv")
output_path = os.path.join("Exported_Data.py")

total_months = 0
net_profit_loss = 0
monthly_profit_loss = []
last_month_profit = 0
current_month_profit = 0
profit_loss_change = []

# open csv and loop rows
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    next(csvreader)

    for row in csvreader:
        # count months
        total_months += 1

        # count net profit/loss
        net_profit_loss += int(row[1])

        # calculate profit/loss for current month
        current_month_profit += int(row[1])
        if total_months > 1:
            profit_loss_change.append(current_month_profit - last_month_profit)
        last_month_profit = current_month_profit

        # add profit/loss for current month to monthly_profit_loss list
        monthly_profit_loss.append(int(row[1]))

# calculate average change in profit/loss in total
average_profit_loss_change = net_profit_loss / total_months

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change $ {average_profit_loss_change}")