from dash import Dash, html, Output, Input, dcc, State
import dash_bootstrap_components as dbc

from constants import dataframes, datasets_options, visualisation_options
from components import (
    header_component,
    upload_component,
    configurations_header_component,
    dataset_dropdown_component,
    x_dropdown_component,
    y_dropdown_component,
    visualisation_dropdown_component,
    error_component,
)
from helpers import (
    choose_visualisation,
    is_figure,
    format_render_vis,
    parse_upload_contents,
)

app = Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)

web_server = app.server

# Think how to extract callbacks to different file.
@app.callback(
    Output("upload-data", "contents"),
    Output("x-dropdown", "value"),
    Output("y-dropdown", "value"),
    Output("vis-dropdown", "value"),
    Input("remove-uploaded-file", "n_clicks"),
)
def remove_uploaded_file(click):
    # pylint: disable=unused-argument
    return [None] * 4


@app.callback(
    Output("dataset-dropdown", "placeholder"),
    Output("output-data-upload-text", "children"),
    Output("output-data-upload", "className"),
    Output("dataset-dropdown", "disabled"),
    Output("upload-data", "disabled"),
    Input("dataset-dropdown", "value"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
)
def block_datasets(dataset, file_content, file_name):
    is_file_uploaded = bool(file_content)
    is_dataset_chosen = bool(dataset)

    is_visible = "visible" if is_file_uploaded else "hidden"
    message = (
        "Remove uploaded dataset to choose"
        if is_file_uploaded
        else "Select Datasets or"
    )
    return [
        message,
        file_name,
        is_visible,
        is_file_uploaded,
        is_file_uploaded or is_dataset_chosen,
    ]


@app.callback(
    Output("x-dropdown", "options"),
    Output("y-dropdown", "options"),
    Output("x-dropdown", "className"),
    Output("y-dropdown", "className"),
    Input("dataset-dropdown", "value"),
    Input("vis-dropdown", "value"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
)
def define_axis_options(dataset, visualisation, file_content, file_name):
    if (not dataset or not file_content) and (
        not visualisation or visualisation == "Table"
    ):
        # should not show Dimension and Measure Axises if not needed.
        return [[], [], "hidden", "hidden"]

    if file_content and file_name:
        dataframe = parse_upload_contents(file_content, file_name)
    elif dataset:
        dataframe = dataframes[dataset]
    else:
        return [[], [], "hidden", "hidden"]

    drodpown_options = list(dataframe.columns)
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
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
)
def render_vis(dataset, visualisation, dimension, measure, file_content, file_name):
    # pylint: disable=too-many-arguments
    if (not visualisation and not dataset) or (not visualisation and not file_content):
        return format_render_vis({})

    try:
        fig = choose_visualisation(
            visualisation,
            parse_upload_contents(file_content, file_name)
            if file_content
            else dataframes[dataset],
            dimension,
            measure,
        )

        if is_figure(fig):
            return format_render_vis(fig=fig, vis={})

        return format_render_vis(vis=fig, fig={})
    except Exception as error:
        # Think if I can fix the fact that two callbacks should be merged into one to not cause exceptions.
        print(error)
        return format_render_vis(
            vis=error_component("Something is wrong, try different parameters"),
            fig={},
        )


app.layout = html.Div(
    children=[
        header_component(),
        html.Div(
            className="content",
            children=[
                html.Div(
                    id="content__vis",
                ),
                dcc.Graph(id="content__fig"),
                html.Div(
                    className="content__panel",
                    children=[
                        configurations_header_component(),
                        dataset_dropdown_component(datasets_options),
                        upload_component(),
                        visualisation_dropdown_component(visualisation_options),
                        x_dropdown_component(),
                        y_dropdown_component(),
                    ],
                ),
            ],
        ),
    ],
)

if __name__ == "__main__":
    print(
        "\n\n\nIf you ran this app using `docker compose up` then your app awaits you at http://127.0.0.1:8080\n"
    )
    app.run_server(debug=True, host="0.0.0.0", port=5000)
