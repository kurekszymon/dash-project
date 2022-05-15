from dash import dcc


def visualisation_dropdown_component(options):
    return dcc.Dropdown(
        options=options,
        id="vis-dropdown",
        placeholder="Select visualisation"
    )
