from .generate_charts import (
    generate_bar_chart,
    generate_line_chart,
    generate_table,
    generate_scatter_chart,
    generate_heatmap,
    generate_pie_chart,
)

from constants import charts


def choose_visualisation(visualisation, dataframe, x_axis=None, y_axis=None):
    if visualisation == charts["table"]:
        return generate_table(dataframe)
    if visualisation == charts["bar"]:
        return generate_bar_chart(dataframe, x_axis, y_axis)
    if visualisation == charts["line"]:
        return generate_line_chart(dataframe, x_axis, y_axis)
    if visualisation == charts["scatter"]:
        return generate_scatter_chart(dataframe, x_axis, y_axis)
    if visualisation == charts["heatmap"]:
        return generate_heatmap(dataframe, x_axis, y_axis)
    if visualisation == charts["pie"]:
        return generate_pie_chart(dataframe, x_axis, y_axis)
    return "Choose proper visualisation"
