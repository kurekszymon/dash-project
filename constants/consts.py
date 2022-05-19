import pandas as pd

charts = {
    "table": "Table",
    "line": "Line Chart",
    "bar": "Bar Chart",
    "scatter": "Scatter Chart",
    "heatmap": "Heatmap",
    "pie": "Pie Chart",
}

visualisation_options = [
    {"label": charts["table"], "value": charts["table"]},
    {"label": charts["bar"], "value": charts["bar"]},
    {"label": charts["line"], "value": charts["line"]},
    {"label": charts["scatter"], "value": charts["scatter"]},
    {"label": charts["heatmap"], "value": charts["heatmap"]},
    {"label": charts["pie"], "value": charts["pie"]},
]


datasets_options = [
    {"label": "Example Dataset 1", "value": "example_df"},
    {"label": "Example Dataset 2", "value": "example_df2"},
    {"label": "Premier League", "value": "premier_league_df"},
    {"label": "Bundesliga 1", "value": "bundesliga_df"},
    {"label": "La Liga", "value": "la_liga_df"},
    {"label": "Chamions League Clubs Ranking", "value": "cl_clubs_ranking"},
    {"label": "Chamions League Countries Ranking", "value": "cl_countries_ranking"},
    {"label": "Chamions League Players Appearances", "value": "cl_players_appearances"},
    {"label": "Chamions League Players Goals", "value": "cl_players_goals"},
    {"label": "Chamions League Top Goal Scorers", "value": "cl_goal_scorers"}
]

dataframes = {
    "premier_league_df": pd.read_csv("data/premier_league.csv"),
    "bundesliga_df": pd.read_csv("data/Bundesliga_1_Seasons_11_12_to_20_21.csv"),
    "la_liga_df": pd.read_csv("data/LaLiga_Matches_1995-2021.csv"),
    "cl_clubs_ranking": pd.read_csv("data/Champions_League_AllTimeRankingByClub.csv"),
    "cl_countries_ranking": pd.read_csv("data/Champions_League_AllTimeRankingByCountry.csv"),
    "cl_players_appearances": pd.read_csv("data/Champions_League_PlayerAppearDetails.csv"),
    "cl_players_goals": pd.read_csv("data/Champions_League_PlayerGoalDetails.csv"),
    "cl_goal_scorers": pd.read_csv("data/Champions_League_TopGoalScorer.csv"),
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
