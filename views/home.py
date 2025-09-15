from dash import html, dcc
import dash_bootstrap_components as dbc

# ====== parámetros/constantes que puedes reemplazar desde tus settings ======
# Si ya los tienes definidos en otro módulo, impórtalos y borra esto.
nombre_lineas = ["11", "7"]  # ejemplo
interval = 30_000  # 30s, ajusta a tu valor real
colors = {"background": "#0f0f10", "text": "#ddd"}  # ejemplo de tema oscuro

# ====== estilos reutilizables ======
COLOR_HEADER = "#5dade2"
COLOR_INPUT_BG = "#000"
COLOR_INPUT_TEXT = "white"

style_title_bar = {
    "width": "100%",
    "backgroundColor": COLOR_HEADER,
    "color": "white",
    "textAlign": "center",
    "fontSize": "35px",
    "fontWeight": "bold",
}

style_subtitle_bar = {
    "marginTop": "10px",
    "width": "100%",
    "backgroundColor": COLOR_INPUT_BG,
    "color": COLOR_INPUT_TEXT,
    "textAlign": "center",
    "fontSize": "25px",
}

style_metric_input = {
    "marginTop": "20px",
    "width": "100%",
    "backgroundColor": COLOR_INPUT_BG,
    "color": COLOR_INPUT_TEXT,
    "textAlign": "center",
    "fontSize": "30px",
}

style_big_message = {
    "marginTop": "20px",
    "width": "100%",
    "marginLeft": "5px",
    "backgroundColor": COLOR_HEADER,
    "color": "white",
    "textAlign": "center",
    "fontSize": "45px",
    "fontWeight": "bold",
}

card_frame_style = {
    "height": "33rem",
    "border": "2px solid black",
    "textAlign": "left",
    "marginTop": "10px",
    "marginLeft": "10px",
}

right_card_frame_style = {
    "height": "33rem",
    "width": "65rem",
    "border": "2px solid black",
    "textAlign": "center",
    "marginTop": "10px",
}

# ====== componentes helper ======
def make_line_card(line_name: str,
                   rend_teo_id: str,
                   ege_id: str,
                   disp_id: str,
                   desem_id: str,
                   tdeten_id: str):
    """Crea una tarjeta de línea (columna izquierda)."""
    return dbc.Card(
        dbc.CardBody([
            # Título (Línea X)
            dbc.Row([
                dbc.Col([
                    dcc.Input(
                        value=f"Línea {line_name}",
                        type="text",
                        disabled=True,
                        style=style_title_bar,
                    )
                ])
            ]),

            # Subtítulo
            dbc.Row([
                dbc.Col([
                    dcc.Input(
                        value="Rendimiento Teórico",
                        type="text",
                        disabled=True,
                        style=style_subtitle_bar,
                    )
                ])
            ]),

            # Valor Rend. Teórico (lo llenas por callback en el Div)
            dbc.Row([dbc.Col([html.Div(id=rend_teo_id)])]),

            # EGE
            dbc.Row([
                dbc.Col([html.H6("EGE", style={"marginTop": "30px"})]),
                dbc.Col([
                    dcc.Input(
                        value="0000",
                        type="text",
                        id=ege_id,
                        disabled=True,
                        style=style_metric_input,
                    )
                ]),
            ]),

            # Disponibilidad
            dbc.Row([
                dbc.Col([html.H6("Disponibilidad", style={"marginTop": "30px"})]),
                dbc.Col([
                    dcc.Input(
                        value="0000",
                        type="text",
                        id=disp_id,
                        disabled=True,
                        style=style_metric_input,
                    )
                ]),
            ]),

            # Desempeño
            dbc.Row([
                dbc.Col([html.H6("Desempeño", style={"marginTop": "30px"})]),
                dbc.Col([
                    dcc.Input(
                        value="0000",
                        type="text",
                        id=desem_id,
                        disabled=True,
                        style=style_metric_input,
                    )
                ]),
            ]),

            # Tiempo de detención
            dbc.Row([
                dbc.Col([html.H6("T.Detención", style={"marginTop": "30px"})]),
                dbc.Col([
                    dcc.Input(
                        value="---",
                        type="text",
                        id=tdeten_id,
                        disabled=True,
                        style=style_metric_input,
                    )
                ]),
            ]),
        ]),
        style=card_frame_style,
    )


def make_right_card(title_text: str, textarea_id: str):
    """Crea una tarjeta grande de la derecha con Textarea."""
    return dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Input(
                        value=title_text,
                        type="text",
                        disabled=True,
                        style=style_title_bar,
                    )
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Textarea(
                        placeholder="",
                        id=textarea_id,
                        value="",
                        style={
                            "width": "100%",
                            "marginTop": "10px",
                            "marginBottom": "5px",
                            "backgroundColor": COLOR_INPUT_BG,
                            "color": COLOR_INPUT_TEXT,
                            "textAlign": "center",
                            "fontSize": "40px",
                            "fontWeight": "bold",
                        },
                        cols=3,
                        rows=7,
                    )
                ])
            ]),
        ]),
        style=right_card_frame_style,
    )


# ====== layout principal ======
layout = html.Div([
    # Refresh auto (igual que tu ejemplo)
    html.Meta(httpEquiv="refresh", content="300"),

    dbc.Row([
        # ------------------------- Columna izquierda (2) -------------------------
        dbc.Col([
            # Línea 1
            dbc.Row([
                make_line_card(
                    line_name=nombre_lineas[0],
                    rend_teo_id="rend_teo1_home2",
                    ege_id="dato1_home2",
                    disp_id="dato2_home2",
                    desem_id="dato3_home2",
                    tdeten_id="t_deten_1_home2",
                )
            ]),
            # Línea 2
            dbc.Row([
                make_line_card(
                    line_name=nombre_lineas[1],
                    rend_teo_id="rend_teo2_home2",
                    ege_id="ege_ad_home2",
                    disp_id="disp_ad_home2",
                    desem_id="desem_ad_home2",
                    tdeten_id="t_deten_2_home2",
                )
            ]),

            # Interval para últimos datos (como en tu ejemplo)
            dcc.Interval(id="interval-ultimos-datos_home2", interval=interval, n_intervals=0),
        ], width=2),

        # ------------------------- Columna central (7) --------------------------
        dbc.Col([
            # Mensaje superior 1
            dbc.Row([
                dbc.Col([
                    dcc.Input(
                        value="----",
                        type="text",
                        id="msj1_home2",
                        disabled=True,
                        style=style_big_message
                    )
                ])
            ]),

            # Gráfico 1
            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                        id="grafico_1_home2",
                        figure={
                            "layout": {
                                "title": "",
                                "height": 425,
                                "width": 1100,
                                "margin": {"l": 40, "r": 20, "t": 25, "b": 40},
                                "plot_bgcolor": colors["background"],
                                "paper_bgcolor": colors["background"],
                                "font": {"color": colors["text"]},
                            }
                        },
                        style={"marginTop": "15px", "marginLeft": "5px"},
                    ),
                    dcc.Interval(id="interval-grafico_1_home2", interval=interval, n_intervals=0),
                ])
            ]),

            # Mensaje superior 2
            dbc.Row([
                dbc.Col([
                    dcc.Input(
                        value="----",
                        type="text",
                        id="msj2_home2",
                        disabled=True,
                        style=style_big_message
                    )
                ])
            ]),

            # Gráfico 2
            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                        id="grafico_2_home2",
                        figure={
                            "layout": {
                                "title": "",
                                "height": 425,
                                "width": 1100,
                                "margin": {"l": 40, "r": 20, "t": 25, "b": 40},
                                "plot_bgcolor": colors["background"],
                                "paper_bgcolor": colors["background"],
                                "font": {"color": colors["text"]},
                            }
                        },
                        style={"marginTop": "15px", "marginLeft": "5px"},
                    ),
                    dcc.Interval(id="interval-grafico_2_home2", interval=interval, n_intervals=0),
                ])
            ]),

            dcc.Interval(id="interval-op_home2", interval=interval, n_intervals=0),
        ], width=7),

        # ------------------------- Columna derecha (3) --------------------------
        dbc.Col([
            dbc.Row([make_right_card("Próxima Fabricación", "text_area_msj1_home2")]),
            dbc.Row([make_right_card("Próxima Fabricación", "text_area_msj2_home2")]),
            dcc.Interval(id="interval-msjs_home2", interval=interval, n_intervals=0),
        ], width=3),
    ])
], style={"backgroundColor": colors["background"], "minHeight": "100vh", "paddingBottom": "20px"})
