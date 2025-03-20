"""
Simple dash app example
"""
#Standard imports

#3rd party imports
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

#Local imports
from functions import read_csv, select_stock

# Load data
stock_df = read_csv("stock.csv")
demands_df = read_csv("demands.csv")
targets_df = read_csv("targets.csv")

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Stock and fill rate calculator"),
    html.Label("Choose your grouping"),
    dcc.RadioItems(
        id='stock-group',
        options=[
            {"label": "A", "value": "A"},
            {"label": "B", "value": "B"},
            {"label": "C", "value": "C"}
        ],
        value="A",
        inline=True
    ),
    dcc.Graph(id="stock-graph")
])

# Callback for interactive updates
@app.callback(
    Output("stock-graph", "figure"),
    [Input("stock-group", "value")]
)
def update_graph(stock_group):
    display_df = select_stock(data=stock_df, stock_group=stock_group)
    return px.line(stock_df[stock_df['group'] == stock_group], x="date", y="quantity")

if __name__ == '__main__':
    app.run_server(debug=True)
 