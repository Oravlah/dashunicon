from dash import html, dcc
import dash_bootstrap_components as dbc

# ====== parámetros ======
nombre_lineas = ["11", "7"]  # ejemplo
interval = 30_000  # 30s
colors = {"background": "#001f3f", "text": "white"}  # azul oscuro de fondo

# ====== estilos ======
COLOR_HEADER = "#007bff"     # azul Bootstrap
COLOR_METRIC_BG = "#ffc107"  # amarillo Bootstrap
COLOR_TEXT = "white"

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
    "backgroundColor": COLOR_HEADER,
    "color": "white",
    "textAlign": "center",
    "fontSize": "25px",
}

style_metric_input = {
    "marginTop": "20px",
    "width": "100%",
    "backgroundColor": COLOR_METRIC_BG,
    "color": COLOR_TEXT,
    "textAlign": "center",
    "fontSize": "30px",
    "fontWeight": "bold",
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

# ====== helper ======
def make_line_card(line_name: str,
                   rend_teo_id: str,
                   ege_id: str,
                   disp_id: str,
                   desem_id: str,
                   tdeten_id: str):
    return dbc.Card(
        dbc.CardBody([
            # Título
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

            # Valor Rend. Teórico
            dbc.Row([dbc.Col([html.Div(id=rend_teo_id)])]),

            # EGE
            dbc.Row([
                dbc.Col([html.H6("EGE", style={"marginTop": "30px", "color": "white"})]),
                dbc.Col([
                    dcc.Input(value="0000", type="text", id=ege_id, disabled=True, style=style_metric_input)
                ]),
            ]),

            # Disponibilidad
            dbc.Row([
                dbc.Col([html.H6("Disponibilidad", style={"marginTop": "30px", "color": "white"})]),
                dbc.Col([
                    dcc.Input(value="0000", type="text", id=disp_id, disabled=True, style=style_metric_input)
                ]),
            ]),

            # Desempeño
            dbc.Row([
                dbc.Col([html.H6("Desempeño", style={"marginTop": "30px", "color": "white"})]),
                dbc.Col([
                    dcc.Input(value="0000", type="text", id=desem_id, disabled=True, style=style_metric_input)
                ]),
            ]),

            # Tiempo de detención
            dbc.Row([
                dbc.Col([html.H6("T.Detención", style={"marginTop": "30px", "color": "white"})]),
                dbc.Col([
                    dcc.Input(value="---", type="text", id=tdeten_id, disabled=True, style=style_metric_input)
                ]),
            ]),
        ]),
        style=card_frame_style,
    )


# ====== layout ======
layout = html.Div([
    html.Meta(httpEquiv="refresh", content="300"),

    dbc.Row([
        # Columna izquierda (líneas)
        dbc.Col([
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
            dcc.Interval(id="interval-ultimos-datos_home2", interval=interval, n_intervals=0),
        ], width=3),

        # Columna central (mensajes y gráficos)
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dcc.Input(value="----", type="text", id="msj1_home2", disabled=True, style=style_big_message)
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                        id="grafico_1_home2",
                        figure={
                            "layout": {
                                "title": "",
                                "height": 425,
                                "autosize": False,  # ⬅️ fija la altura
                                "margin": {"l": 40, "r": 20, "t": 25, "b": 40},
                                "plot_bgcolor": colors["background"],
                                "paper_bgcolor": colors["background"],
                                "font": {"color": colors["text"]},
                            }
                        },
                        config={"responsive": False},  # ⬅️ evita crecer por responsivo
                        style={"marginTop": "15px", "marginLeft": "5px", "height": "425px"},  # ⬅️ reserva en CSS
                    ),
                    dcc.Interval(id="interval-grafico_1_home2", interval=interval, n_intervals=0),
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Input(value="----", type="text", id="msj2_home2", disabled=True, style=style_big_message)
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                        id="grafico_2_home2",
                        figure={
                            "layout": {
                                "title": "",
                                "height": 425,
                                "autosize": False,  # ⬅️ fija la altura
                                "margin": {"l": 40, "r": 20, "t": 25, "b": 40},
                                "plot_bgcolor": colors["background"],
                                "paper_bgcolor": colors["background"],
                                "font": {"color": colors["text"]},
                            }
                        },
                        config={"responsive": False},  # ⬅️ evita crecer por responsivo
                        style={"marginTop": "15px", "marginLeft": "5px", "height": "425px"},  # ⬅️ reserva en CSS
                    ),
                    dcc.Interval(id="interval-grafico_2_home2", interval=interval, n_intervals=0),
                ])
            ]),
            dcc.Interval(id="interval-op_home2", interval=interval, n_intervals=0),
        ], width=9, style={"maxHeight": "calc(100vh - 40px)", "overflowY": "auto"}),  # ⬅️ opcional anti-desborde
    ])
], style={"backgroundColor": colors["background"], "minHeight": "100vh", "paddingBottom": "20px"})
