import plotly
import plotly.graph_objects as go
import pandas as pd

#retrieve inputs

input = sys.argv[1] #file type e.g. workbook.xlsx
filepath = sys.argv[2] # pathway to said file
x_axis = sys.argv[3] #column to be plotted on x_axis
y_axis = sys.argv[4] #column to be plotted on y_axis
title = sys.argv[5] #title of chart
xaxis_title = sys.argv[6] # xaxis title
yaxis_title = sys.argv[7] # yaxis title
outfile = sys.argv[8] #output file

#function to decipher which data type is to be usedd
def get_data(input, filepath):
    if input.endswith(".csv"):
        df = pd.read_csv(filepath)
    elif input.endswith(".xlsx"):
        df = pd.read_excel(filepath)
    else:
        print('This program only excepts excel aand csv formatting')
    return df

#calling function
get_data(input,filepath)

# declare data visualistaion

data = [go.Scatter( x=df[x_axis], y=df[y_axis])]

#plot figure

fig = go.Figure(data)

#add detail

fig.update_layout(
    title= title,
    xaxis_title= xaxis_title,
    yaxis_title= yaxis_title
)
#show figure

fig.show()

#print to html file for quick sharing

plotly.offline.plot(fig, filename=outfile)
