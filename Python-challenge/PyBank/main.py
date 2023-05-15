# Modules
import os
import csv

# Set path for file
budget_data = os.path.join("Resources", "budget_data.csv")

# Open and read the CSV file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # Declare profits and months 
    Profit = []
    months = []

    # loop to read each row of data
    for rows in csvreader:
        Profit.append(int(rows[1]))
        months.append(rows[0])

    # loop to find the profit change
    profit_change =[]

    for x in range(1, len(Profit)):
        profit_change.append((int(Profit[x]) - int(Profit[x-1])))

    # find the average profit change
    profit_average = round((sum(profit_change) / len(profit_change)),2)
 

    # find the total length of months
    total_months = len(months)

    # greatest increase in profit
    greatest_increase = max(profit_change)

    #greatest decrease in profit
    greatest_decrease = min(profit_change)


    # Print Results on the screen
    print() 
    print ("Financial Analysis"+"\n")
    
    print("------------------------------------------"+"\n")
 
    print ("Total Months:" + str(total_months)+"\n")


    print("Total:" + "$" + str(sum(Profit))+"\n")
    
    print ("Average Change:" + "$" + str(profit_average)+"\n")
    
    print("Greatest Increase in Profits: " + str(months[profit_change.index(max(profit_change))+1]) + " " + "($" + str(greatest_increase)+")"+"\n")
    
    print("Greatest Decrease in Profits: " + str(months[profit_change.index(min(profit_change))+1]) + " " + "($" + str(greatest_decrease)+")"+"\n")
    

    # Write to my output text file
    file = open("output.txt","w")

    file.write("Financial Analysis"+"\n\n")
    
    file.write("--------------------------------------"+"\n\n")

    file.write("total months: " + str(total_months)+"\n\n")

    file.write("Total: " + "$" + str(sum(Profit))+"\n\n")

    file.write("Average change: " + "$" + str(profit_average)+"\n\n")

    file.write("Greatest Increase in Profits: " + str(months[profit_change.index(max(profit_change))+1]) + " " + "($" + str(greatest_increase)+")"+"\n\n")

    file.write("Greatest Decrease in Profits: " + str(months[profit_change.index(min(profit_change))+1]) + " " + "($" + str(greatest_decrease)+")"+"\n\n")

    file.close()