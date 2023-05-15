# Modules
import os
import csv

# open and read CSV file
csvpath=os.path.join("Resources","election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    
    # Declaring variables
    votes = []
    county = []
    candidates = []
    Charles_Casper_Stockham = []
    Diana_DeGette = []
    Raymon_Anthony_Doane = []
    Charles_Casper_Stockham_votes = 0
    Diana_DeGette_votes = 0
    Raymon_Anthony_Doane_votes = 0

    # Loop to read each row of data after header
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # Total votes
    total_votes = (len(votes))
 

    # Loop to find v,otes by candiate 
    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            Charles_Casper_Stockham.append(candidates)
            Charles_Casper_Stockham_votes = len(Charles_Casper_Stockham)
            
        elif candidate == "Diana DeGette":
            Diana_DeGette.append(candidates)
            Diana_DeGette_votes = len(Diana_DeGette)
            
        else:
            Raymon_Anthony_Doane.append(candidates)
            Raymon_Anthony_Doane_votes = len(Raymon_Anthony_Doane)
   
    
    # Calculate percentages
    Charles_Casper_Stockham_percent = round(((Charles_Casper_Stockham_votes / total_votes) * 100), 3)
    Diana_DeGette_percent = round(((Diana_DeGette_votes / total_votes) * 100), 3)
    Raymon_Anthony_Doane_percent = round(((Raymon_Anthony_Doane_votes / total_votes) * 100), 3)
    

    
    # Find out who the winner is
    if Charles_Casper_Stockham_percent > max(Diana_DeGette_percent, Raymon_Anthony_Doane_percent):
        winner = "Charles Casper Stockham"
    elif Diana_DeGette_percent > max(Charles_Casper_Stockham_percent, Raymon_Anthony_Doane_percent):
        winner = "Diana DeGette"  
    else:
        winner = "Raymon Anthony Doane"


# Print Statements

print("\n\nElection Results \n\n")
print("-----------------------------------\n")
print("Total Votes: "+ str(total_votes)+"\n")
print("-----------------------------------\n")
print ("Charles Casper Stockham: "+ str(Charles_Casper_Stockham_percent)+"%" +" (" + str(Charles_Casper_Stockham_votes)+")"+"\n")
print("Diana DeGette: "+str(Diana_DeGette_percent)+"%" +"("+str(Diana_DeGette_votes)+")"+"\n")
print ("Raymon Anthony Doane: "+str(Raymon_Anthony_Doane_percent)+"%"+ "("+str(Raymon_Anthony_Doane_votes)+")"+"\n\n")
print("-----------------------------------\n")
print ("Winner: "+ winner+"\n")
print("-----------------------------------\n")


# Analysis to a text file
file = open("output.txt","w")
file.write("\nElection Results\n\n")
file.write("-----------------------------------\n\n")
file.write("Total Votes:" +str(total_votes)+"\n\n")
file.write("-----------------------------------\n\n")
file.write("Charles Casper Stockham:"+str(Charles_Casper_Stockham_percent)+"%" +"("+ str(Charles_Casper_Stockham_votes)+")"+"\n")
file.write("Diana DeGette:" + str(Diana_DeGette_percent) + "%" +"("+ str(Diana_DeGette_votes)+")"+"\n")
file.write("Raymon Anthony Doane:"+str(Raymon_Anthony_Doane_percent)+"%"+ "("+ str(Raymon_Anthony_Doane_votes)+")"+"\n\n")
file.write("-----------------------------------\n\n")
file.write("Winner:" +winner+"\n\n")
file.write("-----------------------------------\n")
file.close()