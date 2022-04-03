from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from components import example
from helpers import generate_html_table

app = Dash(__name__)

colors = {"background": "#666666", "text": "#7FDBFF"}

df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

df2 = pd.read_csv(
    "https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv"
)

df3 = pd.read_csv(
    "https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv"
)

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors["background"],
    paper_bgcolor=colors["background"],
    font_color=colors["text"],
)

fig2 = px.scatter(
    df3,
    x="gdp per capita",
    y="life expectancy",
    size="population",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)


app.layout = html.Div(
    children=[
        html.H1(
            children="Hello Dash",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            children="Dash: A web application framework for your data.",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        dcc.Graph(id="example-graph-2", figure=fig),
        dcc.Graph(id="life-exp-vs-gdp", figure=fig2),
        example(),
        generate_html_table(df2),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
