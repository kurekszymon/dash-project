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
                id="interval-component", interval=1000, n_intervals=0  # in milliseconds
            ),
        ],
    )


def generate_bar_chart(dataframe, x, y):
    if not x or not y:
        return "Define x and y axis"
    return px.bar(dataframe, x=x, y=y, barmode="group")
