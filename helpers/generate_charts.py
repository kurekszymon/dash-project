from dash import html
import plotly.express as px

from components import error_component


def generate_table(dataframe):
    """Generates Custom HTML Table based on `dataframe`"""
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
        ],
    )


PROVIDE_MORE_DETAILS = error_component("Define dimension and measure")

# maybe add title possibility?
def generate_bar_chart(dataframe, dimension, measure):
    if not dimension or not measure:
        return PROVIDE_MORE_DETAILS
    return px.bar(dataframe, x=dimension, y=measure, barmode="group")


def generate_line_chart(dataframe, dimension, measure):
    if not dimension or not measure:
        return PROVIDE_MORE_DETAILS
    return px.line(dataframe, x=dimension, y=measure)


def generate_scatter_chart(dataframe, dimension, measure):
    if not dimension or not measure:
        return PROVIDE_MORE_DETAILS
    return px.scatter(dataframe, x=dimension, y=measure)


def generate_heatmap(dataframe, dimension, measure):
    if not dimension or not measure:
        return PROVIDE_MORE_DETAILS
    return px.density_heatmap(dataframe, x=dimension, y=measure)


def generate_pie_chart(dataframe, dimension, measure):
    if not dimension or not measure:
        return PROVIDE_MORE_DETAILS
    return px.pie(dataframe, values=dimension, names=measure)
