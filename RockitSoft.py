# pip install plotly
# pip install dash
# pip install pandas

from tkinter.ttk import Style
import pandas as pd
import plotly.express as px
import webbrowser
from threading import Timer
import sys

from dash import Dash, dcc, html
from dash.dependencies import Input, Output


app = Dash(__name__, title='Rockit Graph')

tabs_styles = {
    'height': '30px',

}
tab_style = {
    'padding': '6px',
    'font-family': 'Arial, Helvetica, sans-serif',
    'font-size': '12px',
    'fontWeight': 'normal'
}

tab_selected_style = {
    'padding': '6px',
    'border-style': 'solid',
    'border-color': 'grey',
    'font-family': 'Arial, Helvetica, sans-serif',
    'font-size': '12px',
    'fontWeight': 'bold'
}

filename = input("Enter filename with extension: ")
df = pd.read_csv(str(filename))
columns = pd.read_csv(str(filename), nrows=1).columns.tolist()

col = [1]

for x in columns:
    col.append(df[x].to_list())


app.layout = html.Div([
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label=columns[1].title(), value='tab-1-example-graph',
                style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label=columns[2].title(), value='tab-2-example-graph',
                style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label=columns[3].title(), value='tab-3-example-graph',
                style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label=columns[4].title(), value='tab-4-example-graph',
                style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label=columns[5].title(), value='tab-5-example-graph',
                style=tab_style, selected_style=tab_selected_style),

    ]),
    html.Div(id='tabs-content-example-graph')
])


@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1-example-graph':
        return html.Div([
            dcc.Graph(
                id='graph-1-tabs',
                figure={
                    'data': [{
                        'x': col[1],
                        'y': col[2],
                        'type': 'line'
                    }], "layout": {
                        "title": {
                            'text': columns[1] + ' vs Time',
                            'font': {
                                'family': 'Arial, Helvetica, sans-serif',
                                'size': '15',
                                'weight': 'bold'
                            },
                        },
                        "height": 620,  # px
                        'xaxis': {
                            'title': columns[0]
                        },
                        'yaxis':{
                            'title': columns[1],
                            'fontWeight': 'bold'
                        }
                    },
                }
            )
        ])
    elif tab == 'tab-2-example-graph':
        return html.Div([
            dcc.Graph(
                id='graph-2-tabs',
                figure={
                    'data': [{
                        'x': col[1],
                        'y': col[3],
                        'type': 'line'
                    }],
                    "layout": {
                        "title": columns[2] + ' vs Time',
                        "height": 620,  # px
                        'xaxis': {
                            'title': columns[0]
                        },
                        'yaxis':{
                            'title': columns[2]
                        }
                    },
                }
            )
        ])
    elif tab == 'tab-3-example-graph':
        return html.Div([
            dcc.Graph(
                id='graph-3-tabs',
                figure={
                    'data': [{
                        'x': col[1],
                        'y': col[4],
                        'type': 'line'
                    }],
                    "layout": {
                        "title": columns[3] + ' vs Time',
                        "height": 620,  # px
                        'xaxis': {
                            'title': columns[0]
                        },
                        'yaxis':{
                            'title': columns[3]
                        }
                    },
                }
            )
        ])
    elif tab == 'tab-4-example-graph':
        return html.Div([
            dcc.Graph(
                id='graph-4-tabs',
                figure={
                    'data': [{
                        'x': col[1],
                        'y': col[5],
                        'type': 'line'
                    }],
                    "layout": {
                        "title": columns[4] + ' vs Time',
                        "height": 620,  # px
                        'xaxis': {
                            'title': columns[0]
                        },
                        'yaxis':{
                            'title': columns[4]
                        }
                    },
                }
            )
        ])
    elif tab == 'tab-5-example-graph':
        return html.Div([
            dcc.Graph(
                id='graph-4-tabs',
                figure={
                    'data': [{
                        'x': col[1],
                        'y': col[6],
                        'type': 'line'
                    }],
                    "layout": {
                        "title": columns[5] + ' vs Time',
                        "height": 620,  # px
                        'xaxis': {
                            'title': columns[0]
                        },
                        'yaxis':{
                            'title': columns[5]
                        }
                    },
                }
            )
        ])


port = 8009


def open_browser():
    webbrowser.open("http://localhost:{}".format(port))


if __name__ == '__main__':

    Timer(1, open_browser).start()
    app.run_server(port=port, debug=True, use_reloader=False)
