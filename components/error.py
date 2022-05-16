from dash import html


def error_component(message):
    return html.Div(
        className="error-wrapper",
        children=[html.Div(message, className="error-message")],
    )
