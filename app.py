from dash import Dash, html, Output, Input, dcc

from constants import dataframes, datasets_options, visualisation_options
from components import (
    title_component,
    dataset_dropdown_component,
    x_dropdown_component,
    y_dropdown_component,
    visualisation_dropdown_component,
)
from helpers import choose_visualisation, is_figure, format_render_vis

app = Dash(__name__)


# add callback for disabling x and y axis for table
@app.callback(
    Output("x-dropdown", "options"),
    Output("y-dropdown", "options"),
    Output("x-dropdown", "className"),
    Output("y-dropdown", "className"),
    Input("dataset-dropdown", "value"),
    Input("vis-dropdown", "value"),
)
def define_axis_options(dataset, visualisation):
    if dataset is None or visualisation is None or visualisation == "Table":
        # should not show Dimension and Measure Axises if not needed.
        return [[], [], "hidden", "hidden"]

    drodpown_options = list(dataframes[dataset].columns)
    return [drodpown_options, drodpown_options, "visible", "visible"]


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
def render_vis(dataset, visualisation, dimension, measure):
    if not dataset or not visualisation:
        return format_render_vis({})

    try:
        fig = choose_visualisation(
            visualisation,
            dataframes[dataset],
            dimension,
            measure,
        )

        if is_figure(fig):
            return format_render_vis(fig=fig, vis={})

        return format_render_vis(vis=fig, fig={})
    except Exception as error:
        print(error)
        return format_render_vis(
            vis="Something is wrong, and it's most likely a bug. Please report it and for now, try different parameters",
            fig={},
        )


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
                        y_dropdown_component(),
                    ],
                ),
                html.Div(
                    id="content__vis",
                ),
                dcc.Graph(id="content__fig"),
            ],
        ),
    ],
)

if __name__ == "__main__":
    print(
        "\n\n\nIf you ran this app using `docker compose up` then your app awaits you at http://127.0.0.1:8080\n"
    )
    app.run_server(debug=True, host="0.0.0.0", port=5000)
