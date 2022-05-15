import base64
import io
import pandas as pd
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


def parse_upload_contents(contents, filename):
    _, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            dataframe = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            dataframe = pd.read_excel(io.BytesIO(decoded))
    except Exception as exception:
        print(exception)
        return "There was an error processing this file."

    return dataframe
