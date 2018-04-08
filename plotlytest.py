import plotly as py
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime




df = pd.read_csv("novss2.csv")
trace1 = go.Scatter(x=df.Date,
                    y=df['Humidity'],
                    name="Vlaznost SS2",
                    line=dict(
                        color="red",
                        width=1,
                        dash='line'
                    )
                    )
df1 = pd.read_csv("novoh.csv")
trace2 = go.Scatter(x=df1.Date,
                    y=df1['Humidity'],
                    name="Vlaznost OH",
                    line=dict(
                        color="blue",
                        width=1,
                        dash='line'
                    ))
fig = py.tools.make_subplots(rows=2,cols=1)
# data = [trace1, trace2]
fig.append_trace(trace1, 1, 1)
# fig.append_trace(trace2, 1, 2)
fig.append_trace(trace2, 2, 1)
# fig.append_trace(trace4, 2, 2)
py.offline.plot(fig, filename='test.html')
