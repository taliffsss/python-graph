import pandas_datareader.data as web
from pandas_datareader import data
import time
import datetime
import pytz
from pytz import timezone
import dash
import dash_core_components as dcc
import dash_html_components as html
import fix_yahoo_finance as yf

#Set TimeZone
asia = timezone('Asia/Manila')

#Current Date Time
now = datetime.datetime.now()

timestamp = now.strftime('%Y-%m-%d')
yf.pdr_override()

app = dash.Dash()
stock = 'TSLA'
start = datetime.datetime(2015, 1, 1)
end = now.strftime('%Y-%m-%d')
df = data.get_data_yahoo(stock, start, end)

app.layout = html.Div(children=[
    html.H1(children='Whoa, a graph!'),

    html.Div(children='''
        Making a stock graph!.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock},
            ],
            'layout': {
                'title': stock
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)