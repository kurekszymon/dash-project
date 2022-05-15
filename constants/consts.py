import pandas as pd

charts = {"table": "Table", "line": "Line Chart", "bar": "Bar Chart", "scatter": "Scatter Chart", "heatmap": "Heatmap", "pie": "Pie Chart"}

visualisation_options = [
    {"label": charts["table"], "value": charts["table"]},
    {"label": charts["bar"], "value": charts["bar"]},
    {"label": charts["line"], "value": charts["line"]},
    {"label": charts["scatter"], "value": charts["scatter"]},
    {"label": charts["heatmap"], "value": charts["heatmap"]},
    {"label": charts["pie"], "value": charts["pie"]},
]


datasets_options = [
    {"label": "df1", "value": "example_df"},
    {"label": "df2", "value": "example_df2"},
    {"label": "Premier League", "value": "premier_league_df"},
]

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
    ),
}
