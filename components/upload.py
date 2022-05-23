from dash import dcc, html


def upload_component():
    return html.Div(
        [
            dcc.Upload(
                id="upload-data",
                children=html.Div(
                    [html.H1("Select file or drop it here"), html.P("(*.csv, *.xls)")]
                ),
            ),
            html.Div(
                id="output-data-upload",
                children=[
                    html.Span(id="output-data-upload-text"),
                    html.I(className="fa fa-trash", id="remove-uploaded-file"),
                ],
            ),
        ]
    )
