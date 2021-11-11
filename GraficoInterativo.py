import pip

pip install plotly
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)
trace = go.Scatter(x = df['yr_built'],
                   y = df['price'],
                   mode = 'markers')
data = [trace]
py.iplot(data)