from constants import charts

from .generate_charts import (
    generate_bar_chart,
    generate_line_chart,
    generate_table,
    generate_scatter_chart,
    generate_heatmap,
    generate_pie_chart,
)


# Rename x/y axis to dimension/measure
def choose_visualisation(visualisation, dataframe, x_axis=None, y_axis=None):
    """Determines which `visualisation` to generate and returns it."""
    return {
        charts["table"]: generate_table(dataframe),
        charts["bar"]: generate_bar_chart(dataframe, x_axis, y_axis),
        charts["line"]: generate_line_chart(dataframe, x_axis, y_axis),
        charts["scatter"]: generate_scatter_chart(dataframe, x_axis, y_axis),
        charts["heatmap"]: generate_heatmap(dataframe, x_axis, y_axis),
        charts["pie"]: generate_pie_chart(dataframe, x_axis, y_axis),
    }.get(visualisation, "Choose proper visualisation")
