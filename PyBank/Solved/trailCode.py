import os
import csv

bd_csv = os.path.join("..", "Resources", "budget_data.csv")

#holders for data
months=[]
profitsLoss=[]


# Open and read csv
with open(bd_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read through each row of data after the header
    for row in csvreader:
        months.append(str(row[0]))
        profitsLoss.append(str(row[1]))

#print(profitsLoss)

for x in profitsLoss:
    totalloss=0
    totalloss=totalloss + x   
        
print(f'$:{int(totalloss)}')


    

#months in column
##totalMonths=len(months)
##print(f"Total Months:{int(totalMonths)}")
##proflost=sum(profitsLoss)
##print(f"money:{int(proflost)}")


#net Profit/Losses in column
#netProfLoss=0

#for x in profitsLoss=netProfLoss + x

#average Profit/Losses
#averageChange=[]
#previousMonth=0

#for x in range(len(profitsLoss)):
    #if x ==0:
        #previousMonth=profitsLoss[x]
    #else
        
