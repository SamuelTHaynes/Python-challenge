import os
import csv

budget_data_csv = os.path.join(".", "Resources", "PyBank", "Resources", "budget_data.csv")
election_data_csv = os.path.join(".", "Resources", "PyPoll", "Resources", "election_data.csv")

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
        current_month_profit = int(row[1])
        if total_months > 1:
            profit_loss_change.append(current_month_profit - last_month_profit)
            months_list = []
        last_month_profit = current_month_profit

        # add profit/loss for current month to monthly_profit_loss list
        monthly_profit_loss.append(int(row[1]))

# calculate average change in profit/loss in total and greatest changes
average_change = sum(profit_loss_change) / total_months

greatest_increase = max(profit_loss_change)
greatest_decrease = min(profit_loss_change)

# print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change $ {average_change}")
print(f"Greatest Increase in Profits $ {greatest_increase}")
print(f"Greatest Decrease in Profits $ {greatest_decrease}")

# export to text file
with open("financial_results.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("-------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${net_profit_loss}\n")
    f.write(f"Average Change $ {average_change}\n")
    f.write(f"Greatest Increase in Profits $ {greatest_increase}\n")
    f.write(f"Greatest Decrease in Profits $ {greatest_decrease}\n")

# PyPoll
# declare variables
total_votes = 0
candidates = []
candidate_votes = {}

# open csv and loop rows
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        # add candidate to the list if not already present
        if candidate not in candidates:
            candidates.append(candidate)
            
        # increment the vote count for the candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# declare variables
winner = ""
max_votes = 0

# calculating votes
results = {}
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    results[candidate] = (votes, percentage)

    # check if the candidate has the most votes so far
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    votes, percentage = results[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# export to text file
with open("election_results.txt", "w") as x:
    x.write("Election Results\n")
    x.write("-------------------------\n")
    x.write(f"Total Votes: {total_votes}\n")
    x.write("-------------------------\n")

    for candidate in candidates:
        votes, percentage = results[candidate]
        x.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    x.write("-------------------------\n")
    x.write(f"Winner: {winner}\n")
    x.write("-------------------------\n")