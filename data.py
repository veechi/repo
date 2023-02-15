import pandas as panda
import plotly.express as PlotX
import datetime
import json, plotly

#Note Columns Date, Close/Last, Volume, Open, High, Low   

DataFrame = panda.read_csv(f"apple.csv",
                            names=('Date', 'Close', 'Volume', 'Open', 'High', 'Low')
                          )   
year_list = []
for i in range(0, len(DataFrame)):
    split_date = DataFrame["Date"][i][:10]
    year = split_date[6:10]
    year_list.append(year)

DataFrame.insert(6, "Year", year_list, True)

print(DataFrame)

def create_line():
# #Note Don't Delete
    fig = PlotX.line(DataFrame, x="Date", y="Volume", color="Year")
    return json.dumps(obj=fig , cls=plotly.utils.PlotlyJSONEncoder) 

def create_bar():
    #Note Don't Delete
    fig = PlotX.bar(DataFrame, y='Volume', x='Year', color="Year")
    return json.dumps(obj=fig , cls=plotly.utils.PlotlyJSONEncoder)  

def create_sunburst():
    fig = PlotX.sunburst(DataFrame, path=['Year'], values='Volume')
    return json.dumps(obj=fig , cls=plotly.utils.PlotlyJSONEncoder) 
