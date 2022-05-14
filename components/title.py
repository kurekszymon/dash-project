from dash import html


def title_component():
    return html.Section(
        className="title",
        children=[
            html.H1(children=[html.Code("Dash"), "-board project"]),
            html.H2("Developed by"),
            html.H3("Przemysław Babulski, Szymon Kurek"),
        ],
    )
