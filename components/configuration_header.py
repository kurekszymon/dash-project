from dash import html


def configurations_header_component():
    return html.Div(
        children=["Configure ", html.I(className="fa-solid fa-sliders")],
        className="configure-header",
    )
