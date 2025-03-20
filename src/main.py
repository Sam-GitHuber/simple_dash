import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Grapes"],
    "Amount": [10, 20, 15, 5],
    "City": ["NYC", "SF", "LA", "Chicago"]
})

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Simple Dash App Example"),
    html.Label("Choose a graph type:"),
    dcc.RadioItems(
        id='graph-type',
        options=[
            {"label": "Bar Chart", "value": "bar"},
            {"label": "Line Chart", "value": "line"}
        ],
        value="bar",
        inline=True
    ),
    dcc.Graph(id="example-graph")
])

# Callback for interactive updates
@app.callback(
    Output("example-graph", "figure"),
    [Input("graph-type", "value")]
)
def update_graph(graph_type):
    if graph_type == "bar":
        return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    elif graph_type == "line":
        return px.line(df, x="Fruit", y="Amount", color="City")

if __name__ == '__main__':
    app.run_server(debug=True)
