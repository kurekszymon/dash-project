from dash import dcc


def dataset_dropdown_component(options):
    return dcc.Dropdown(
        options=options, id="dataset-dropdown", placeholder="Select Dataset"
    )
