from plotly.basedatatypes import BaseFigure


def is_figure(obj):
    return isinstance(obj, BaseFigure)


def format_render_vis(
    fig,
    vis="Define dataset and visualisation",
):
    if not vis:
        styles_vis = {"display": "none"}
        styles_fig = {"display": "block"}
    if not fig:
        styles_fig = {"display": "none"}
        styles_vis = {"display": "flex"}
    return [vis, styles_vis, fig, styles_fig]
