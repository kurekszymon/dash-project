from plotly.basedatatypes import BaseFigure

def is_figure(obj):
    return isinstance(obj, BaseFigure)

def format_render_vis(vis="Define dataset and visualisation", styles_vis={"display": "flex"}, fig={}, styles_fig={"display": "none"}):
    if not vis:
        styles_vis = {"display": "none"}
        styles_fig = {"display": "block"}
    
    return [vis, styles_vis, fig, styles_fig]
    
