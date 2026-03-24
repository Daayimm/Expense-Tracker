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
def viewCSV():
    rows = list(readCSV())
    
    for r in rows:
        print(r)


def deleteRow(id):
    rows = list(readCSV())
    rows = [r for r in rows if r[0]!= str(id)]
        
    with open('expenses.csv','w',newline='') as f:
        
        writer = csv.writer(f)
        writer.writerows(rows)

def sumamry(month):
    rows = list(readCSV())
    sum = 0
    
    filter_rows = []
    
    if month is not None:
        for r in rows:
            date_parts = r[1].split('-')
            row_month = int(date_parts[1])
            if row_month == month:
                filter_rows.append(r)
        rows = filter_rows
        for r in rows:
            sum += float(r[3])
        print(sum)
    else:
        for r in rows:
            sum += float(r[3])
        print(sum)
    
            
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
elif args.command == 'delete':
    deleteRow(args.ID)
elif args.command == 'summary':
    sumamry(args.month)
elif args.command == 'view':
    viewCSV()



        


