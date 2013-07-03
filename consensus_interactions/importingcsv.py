import csv

def incomescsv(filename):
    
    out=open(filename,"r")
    data=csv.reader(out)
    data=[row for row in data]
    out.close()

    return data
