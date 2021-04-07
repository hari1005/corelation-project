import csv 
import numpy as np

def getDataSource(data_path):
    marks_percentage=[]
    day_present=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks_percentage.append(float(row("Marks in Percentage")))
            day_present.append(float(row("Days Present")))

    return{x:marks_percentage,y:day_present}

def findCorrelation(datasource):
    correlation:np.corrcoef(datasource['x'],datasource['y'])
    print("corelation between marks and days present:-",correlation[0,1])

def setup():
    data_path="mvd.csv"

    data_scource=getDataSource(data_path)
    findCorrelation(data_scource)

setup()