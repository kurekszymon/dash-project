from components import error_component
from constants import charts

from .generate_charts import (
    generate_bar_chart,
    generate_line_chart,
    generate_table,
    generate_scatter_chart,
    generate_heatmap,
    generate_pie_chart,
)


def choose_visualisation(visualisation, dataframe, dimension=None, measure=None):
    """Determines which `visualisation` to generate and returns it."""
    return {
        charts["table"]: generate_table(dataframe),
        charts["bar"]: generate_bar_chart(dataframe, dimension, measure),
        charts["line"]: generate_line_chart(dataframe, dimension, measure),
        charts["scatter"]: generate_scatter_chart(dataframe, dimension, measure),
        charts["heatmap"]: generate_heatmap(dataframe, dimension, measure),
        charts["pie"]: generate_pie_chart(dataframe, dimension, measure),
    }.get(visualisation, error_component("Choose proper visualisation"))
