import csv
import argparse
from datetime import datetime






date = datetime.now().strftime("%Y-%m-%d")




def CSVWriter(description,amount):
    
        with open("expenses.csv",'a',newline='') as f:
            id = len(readCSV())
            writer = csv.writer(f)
            writer.writerow([id,date,description,amount])
            

def readCSV():
    try:
        with open('expenses.csv','r') as f:
            return list(csv.reader(f) )
    except FileNotFoundError as e:
        
        print(e)
        return[] 

parser = argparse.ArgumentParser(description="Expense Tracker")
subparsers = parser.add_subparsers(dest="command")

addParser = subparsers.add_parser('add',help = 'Add an expenese')
addParser.add_argument("--amount",type=float,required=True)
addParser.add_argument("--desc",type=str,required=True)

deleteParser = subparsers.add_parser("delete",help='delete an expense by ID')
deleteParser.add_argument('--ID',type=int,required=True)

viewParser = subparsers.add_parser('view',help='view your expenses')

summaryParser = subparsers.add_parser('summary')
summaryParser.add_argument('--month',type = int)

args = parser.parse_args()
if args.command == "add":
    CSVWriter(args.desc,args.amount)




        


