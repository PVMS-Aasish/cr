import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    icecream_sales=[]
    colddrink_sales=[]
    with open(data_path)as f:
        df=csv.DictReader(f)

        for row in df:
            icecream_sales.append(float(row["Temperature"]))
            colddrink_sales.append(float(row["Ice-cream Sales( â‚¹ )"]))
    return {"x":icecream_sales,"y":colddrink_sales}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation: ",correlation[0,1])

def setup():
    data_path="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()