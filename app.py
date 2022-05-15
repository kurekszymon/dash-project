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
    Input("dataset-dropdown", "value"),
)
def define_axis_options(dataset):
    # Function returns list because there are 2 outputs

    if dataset is None:
        return [[], []]
    drodpown_options = list(dataframes[dataset].columns)
    return [drodpown_options, drodpown_options]


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
def render_vis(dataset, visualisation, x_axis, y_axis):
    if not dataset or not visualisation:
        return format_render_vis({})

    try:
        fig = choose_visualisation(
            visualisation=visualisation,
            dataframe=dataframes[dataset],
            x_axis=x_axis,
            y_axis=y_axis,
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
