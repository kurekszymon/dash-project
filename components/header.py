from dash import html
from .title import title_component


def header_component():
    return html.Header(
        children=[
            html.Div(className="logo-wrapper", children=[
                html.Img(className="logo", src="assets/data-scientist.svg"),
                html.Span("Teges-śmeges development"),
            ]),
            title_component(),
        ],
        className="top-header",
    )
