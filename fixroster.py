import pandas as pd
import json
import fileinput
import sys


def main():

    for line in fileinput.input('./gradebook.csv', inplace=1):
        sys.stdout.write(line.lower())

    for line in fileinput.input('./caesarroster.csv', inplace=1):
        sys.stdout.write(line.lower())

    caesarCSV = open("./caesarroster.csv")
    canvasCSV = open("./gradebook.csv")
    
    a = pd.read_csv(caesarCSV)
    b = pd.read_csv(canvasCSV)
    
    merged = a.merge(b, on='netid')
    merged.to_csv("roster.csv", index=False)

if __name__ == '__main__':
    main()
