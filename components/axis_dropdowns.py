from dash import dcc

def x_dropdown_component():
    return dcc.Dropdown(options=[], id="x-dropdown")

def y_dropdown_component():
    return dcc.Dropdown(options=[], id="y-dropdown")