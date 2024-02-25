import os
import csv

# Read CSV file
pybank_csv = os.path.join("Resources", "budget_data.csv")
with open(pybank_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    # Skip header
    csv_header = next(csv_file)
    
    # Declare variables
    months = []
    total_months = 0
    PL = 0
    previous_PL = 0
    net_PL = 0
    change_PL = []
    
    # Read through file
    for row in csv_reader:
        # Create list of months
        months.append(row[0])
        # Find total number of months
        total_months += 1
        # Read profits/losses
        PL = int(row[1])
        # Add to net profits/losses
        net_PL = net_PL + PL
        # Create list of profits/losses changes
        change_PL.append(PL - previous_PL)
        # Set current profits/losses to last month
        previous_PL = PL
    
    # Remove first "change" from data (no data for Dec-09)
    del change_PL[0]
    
    # Calculate average change in profits/losses
    average_change = sum(change_PL)/len(change_PL)
    # Find greatest increase in profit and the month to match
    greatest_inc = max(change_PL)
    index = change_PL.index(greatest_inc)
    greatest_inc_month = months[index+1]
    # Find greatest decrease in profit and the month to match
    greatest_dec = min(change_PL)
    index = change_PL.index(greatest_dec)
    greatest_dec_month = months[index+1]
    
    # Print results to terminal
    print(f"\nFinancial Analysis\n\n----------------------------\n")
    print(f"Total Months: {total_months}")
    print(f"\nTotal: ${net_PL}")
    print(f"\nAverage Change: ${average_change:.2f}") # rounded to 2 decimal points
    print(f"\nGreatest Increase in Profits: {greatest_inc_month} (${greatest_inc})")
    print(f"\nGreatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")
    
    # Print results to output file
    pybank_results = os.path.join("analysis","pybank_results.txt")
    with open(pybank_results, 'w') as results_file:
        results_file.write(f"\nFinancial Analysis\n\n----------------------------\n\nTotal Months: {total_months}\n\nTotal: ${net_PL}\n\nAverage Change: ${average_change:.2f}\n\nGreatest Increase in Profits: {greatest_inc_month} (${greatest_inc})\n\nGreatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")
    
        
