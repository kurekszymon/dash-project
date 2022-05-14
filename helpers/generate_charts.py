from dash import html, dcc
import plotly.express as px



def generate_table(dataframe):
    """
    Example helper
    """
    return html.Table(
        [
            html.Thead(html.Tr([html.Th(col) for col in dataframe.columns])),
            html.Tbody(
                [
                    html.Tr(
                        [html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]
                    )
                    for i in range(min(len(dataframe), 100))
                ]
            ),
            dcc.Interval(
            id='interval-component',
            interval=1000, # in milliseconds
            n_intervals=0
        )
        ],
    )

def generate_bar_chart(dataframe):
    return px.bar(dataframe, x="Fruit", y="Amount", color="City", barmode="group")
