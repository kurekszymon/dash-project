from dash import Dash, dcc, html, Output, Input, State
import plotly.express as px
import pandas as pd

from helpers import generate_table, choose_visualisation

app = Dash(__name__)

colors = {"background": "#666666", "text": "#7FDBFF"}

selected_dataframe = "example_df"
dataframes = {
    "premier_league_df": pd.read_csv("data/final_dataset_head.csv", header=[1]),
    "example_df": pd.DataFrame(
        {
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
        }
    ),
    "example_df2": pd.read_csv(
        "https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv"
    ),
    "example_df3": pd.read_csv(
        "https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv"
    )
}

@app.callback(
    Output('content__vis--chart', 'children'),
    Input('content__panel--load-df', 'n_clicks'),
    State('dataset-dropdown', 'value'),
    State('vis-dropdown', 'value')
)
def update_output(n_clicks, dataset, visualisation):
    if not dataset and not visualisation:
        return "Define dataset and visualisation"

    return choose_visualisation(visualisation=visualisation, dataframe=dataframes[dataset])
    

app.layout = html.Div(
    children=[
        html.Div(
            className="title",
            children=[
                html.H1(children=[html.Code("Dash"), "-board project"]),
                html.H2("Developed by"),
                html.H3("Przemysław Babulski, Szymon Kurek"),
            ],
        ),
        html.Div(
            className="content",
            children=[
                html.Div(
                    className="content__panel",
                    children=[
                        dcc.Dropdown(
                            options=[
                                {"label": "df1", "value": "example_df"},
                                {"label": "df2", "value": "example_df2"},
                                {"label": "Premier League", "value": "premier_league_df"},
                            ],
                            id="dataset-dropdown",
                        ),
                        dcc.Dropdown(
                            options=[
                                {"label": "Table", "value": "Table"},
                                {"label": "Bar Chart", "value": "Bar Chart"},
                                {"label": "Line Chart", "value": "Line Chart"},
                            ],
                            id="vis-dropdown",
                        ),
                        html.Button("Generate Chart", id="content__panel--load-df", n_clicks=0),
                    ],
                ),
                html.Div(className="content__vis", children=[
                    html.Div(id="content__vis--chart"),
                ]),
            ],
        ),
    ],
)

if __name__ == "__main__":
    print(
        "\n\n\nIf you ran this app using `docker compose up` then your app awaits you at http://127.0.0.1:8080\n"
    )
    app.run_server(debug=True, host="0.0.0.0", port=5000)
