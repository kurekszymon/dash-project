from plotly.basedatatypes import BaseFigure


def is_figure(obj):
    """Checks if object is instance of `BaseFigure` class

    `BaseFigure` comes from dash, describes objects that have to be shown with `obj.show()` method
    instead of being passed as children"""
    return isinstance(obj, BaseFigure)


def format_render_vis(
    fig,
    vis="Define dataset and visualisation",
):
    """Designed for render_vis function, returns 4 values, as needed for Dash Outputs,
    `could be further refactored` to assign class instead of style"""
    if not vis:
        styles_vis = {"display": "none"}
        styles_fig = {"display": "block"}
    if not fig:
        styles_fig = {"display": "none"}
        styles_vis = {"display": "flex"}
    return [vis, styles_vis, fig, styles_fig]
