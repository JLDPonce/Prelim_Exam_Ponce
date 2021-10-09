import csv
import json
pathFile="/home/devasc/labs/devnet-src/PrelimExam_CPE028/covid_cases.json"
pathFile2="/home/devasc/labs/devnet-src/PrelimExam_CPE028/covid_csvfile.csv"

with open(pathFile,'r') as x:
    x1=json.loads(x.read())
with open(pathFile2,'w') as y:
    new=csv.writer(y)
    new.writerow(['dataRep','countriesAndTerritories','cases','deaths'])
    for i in x1["records"]:
        new.writerow([i["dateRep"],i["countriesAndTerritories"],i["cases"],i["deaths"]])

print(x1)
    

