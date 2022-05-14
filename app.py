from dash import Dash, html, Output, Input, dcc
import pandas as pd
import plotly.express as px
from components.axis_dropdowns import x_dropdown_component, y_dropdown_component

from constants import dataframes, datasets_options, visualisation_options
from components import title_component, dataset_dropdown_component
from components.visualisation_dropdown import visualisation_dropdown_component
from helpers import choose_visualisation, is_figure, format_render_vis

app = Dash(__name__)

@app.callback(
    Output("x-dropdown", 'options'),
    Output("y-dropdown", "options"),
    Input("dataset-dropdown", "value"),
)
def define_axis_options(dataset):
    # Function returns list because there are 2 outputs

    if dataset is None:
        return [[], []]
    d = list(dataframes[dataset].columns)
    return [d, d]

@app.callback(
    Output("content__vis", "children"),
    Output("content__vis", "style"),
    Output("content__fig", "figure"),
    Output("content__fig", "style"),
    Input("dataset-dropdown", "value"),
    Input("vis-dropdown", "value"),
    Input("x-dropdown", "value"),
    Input("y-dropdown", "value"),
)
def render_vis(dataset, visualisation, x, y):
    if not dataset or not visualisation:
        return format_render_vis()

    try:
        fig = choose_visualisation(
            visualisation=visualisation, dataframe=dataframes[dataset], x=x, y=y
        )

        if(is_figure(fig)):
            # return [{}, {"display": "none"}, fig, {"display: block"}]
            return format_render_vis(fig=fig, vis={})
            return [{}, {"display": "none"}, fig, {"display": "block"}]
        
        return [fig, {"display": "flex"}, {}, {"display": "none"}]
    except Exception as e:
        print(e)
        return ["Something is no yes with your visualisation, try different parameters", {"display": "flex"}, {}, {"display": "none"}]

app.layout = html.Div(
    children=[
        title_component(),
        html.Div(
            className="content",
            children=[
                html.Div(
                    className="content__panel",
                    children=[
                        dataset_dropdown_component(datasets_options),
                        visualisation_dropdown_component(visualisation_options),
                        x_dropdown_component(),
                        y_dropdown_component()
                    ],
                ),
                html.Div(
                    id="content__vis",
                ),
                dcc.Graph(id="content__fig")
            ],
        ),
    ],
)

if __name__ == "__main__":
    print(
        "\n\n\nIf you ran this app using `docker compose up` then your app awaits you at http://127.0.0.1:8080\n"
    )
    app.run_server(debug=True, host="0.0.0.0", port=5000)
