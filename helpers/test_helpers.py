import constants
from components.error import error_component
from .helpers import is_figure, format_render_vis
from .generate_charts import generate_table, generate_line_chart

dataframe = constants.dataframes["premier_league_df"]
linechart = generate_line_chart(dataframe, "Home Team", "Home Team")
err = error_component("Error")
table = generate_table(dataframe)


def test_is_figure_custom_component():
    assert is_figure(table) is False


def test_is_figure_plotly_component():
    assert is_figure(linechart) is True


def test_format_render_vis_plotly_component():
    rendered_vis = format_render_vis(linechart, err)

    assert rendered_vis == [err, {}, linechart, {}]


def test_format_render_vis_custom_component():
    rendered_vis = format_render_vis({}, table)

    assert rendered_vis == [table, {"display": "flex"}, {}, {"display": "none"}]
