# views/home.py
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# === extras para traer datos y armar figuras ===
import os
import requests
import plotly.graph_objects as go
from datetime import datetime, timezone
from requests.adapters import HTTPAdapter, Retry

# ================== CONFIG ==================
GRAFICO_URL = os.getenv("GRAFICO_URL", "http://10.6.0.21:9090/grafico/")

# Nombres legibles de canales (ajústalos a gusto)
CANAL_NOMBRES = {
    "ch0": "Canal 0",
    "ch1": "Canal 1",
    "ch2": "Canal 2",
    "ch3": "Canal 3",
}

# Reutiliza sesión HTTP con reintentos
_session = requests.Session()
_retries = Retry(total=3, backoff_factor=0.3, status_forcelist=(429, 500, 502, 503, 504))
_session.mount("http://", HTTPAdapter(max_retries=_retries))
DEFAULT_TIMEOUT = 6

# ====== parámetros ======
nombre_lineas = ["11", "7"]  # ejemplo
interval = 30_000  # 30s
colors = {"background": "#001f3f", "text": "white"}  # azul oscuro de fondo

# ====== estilos ======
COLOR_HEADER = "#007bff"     # azul Bootstrap
COLOR_METRIC_BG = "#ffc107"  # amarillo Bootstrap
COLOR_TEXT = "white"
COLOR_LABEL = "#001f3f"      # azul oscuro para texto sobre fondo blanco

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

style_metric_label = {
    "marginTop": "30px",
    "color": COLOR_LABEL,       # <- visible sobre card blanca
    "fontWeight": "600",
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

# ====== helpers de UI ======
def make_line_card(line_name: str,
                   rend_teo_id: str,
                   ege_id: str, disp_id: str, desem_id: str, tdeten_id: str,
                   lbl_ege_id: str, lbl_disp_id: str, lbl_desem_id: str, lbl_tdeten_id: str):
    return dbc.Card(
        dbc.CardBody([
            # Título principal
            dbc.Row([
                dbc.Col([
                    dcc.Input(
                        value=f"Línea {line_name}",
                        type="text",
                        disabled=True,
                        style=style_title_bar,
                    )
                ])
            ], className="g-0"),

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
            ], className="g-0"),

            # Valor Rend. Teórico (placeholder para futuro)
            dbc.Row([dbc.Col([html.Div(id=rend_teo_id)])], className="g-0"),

            # Métrica 1
            dbc.Row([
                dbc.Col([html.H6(id=lbl_ege_id, children="—", style=style_metric_label)], width=6),
                dbc.Col([dcc.Input(value="0000", type="text", id=ege_id, disabled=True, style=style_metric_input)], width=6),
            ], className="g-0"),

            # Métrica 2
            dbc.Row([
                dbc.Col([html.H6(id=lbl_disp_id, children="—", style=style_metric_label)], width=6),
                dbc.Col([dcc.Input(value="0000", type="text", id=disp_id, disabled=True, style=style_metric_input)], width=6),
            ], className="g-0"),

            # Métrica 3
            dbc.Row([
                dbc.Col([html.H6(id=lbl_desem_id, children="—", style=style_metric_label)], width=6),
                dbc.Col([dcc.Input(value="0000", type="text", id=desem_id, disabled=True, style=style_metric_input)], width=6),
            ], className="g-0"),

            # Métrica 4
            dbc.Row([
                dbc.Col([html.H6(id=lbl_tdeten_id, children="—", style=style_metric_label)], width=6),
                dbc.Col([dcc.Input(value="---", type="text", id=tdeten_id, disabled=True, style=style_metric_input)], width=6),
            ], className="g-0"),
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
                    ege_id="dato1_home2", disp_id="dato2_home2", desem_id="dato3_home2", tdeten_id="t_deten_1_home2",
                    lbl_ege_id="lbl_ch0_l1", lbl_disp_id="lbl_ch1_l1", lbl_desem_id="lbl_ch2_l1", lbl_tdeten_id="lbl_ch3_l1",
                )
            ], className="g-0"),
            dbc.Row([
                make_line_card(
                    line_name=nombre_lineas[1],
                    rend_teo_id="rend_teo2_home2",
                    ege_id="ege_ad_home2", disp_id="disp_ad_home2", desem_id="desem_ad_home2", tdeten_id="t_deten_2_home2",
                    lbl_ege_id="lbl_ch0_l2", lbl_disp_id="lbl_ch1_l2", lbl_desem_id="lbl_ch2_l2", lbl_tdeten_id="lbl_ch3_l2",
                )
            ], className="g-0"),
            dcc.Interval(id="interval-ultimos-datos_home2", interval=interval, n_intervals=0),
        ], width=3),

        # Columna central (mensajes y gráficos)
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dcc.Input(value="----", type="text", id="msj1_home2", disabled=True, style=style_big_message)
                ])
            ], className="g-0"),

            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                        id="grafico_1_home2",
                        figure={
                            "layout": {
                                "title": "",
                                "height": 425,
                                "autosize": False,
                                "margin": {"l": 40, "r": 20, "t": 25, "b": 40},
                                "plot_bgcolor": colors["background"],
                                "paper_bgcolor": colors["background"],
                                "font": {"color": colors["text"]},
                            }
                        },
                        config={"responsive": True},                       # <- usa todo el ancho
                        style={"marginTop": "15px", "marginLeft": "5px",
                               "height": "425px", "width": "100%"},        # <- ancho completo
                    ),
                    dcc.Interval(id="interval-grafico_1_home2", interval=interval, n_intervals=0),
                ])
            ], className="g-0"),

            dbc.Row([
                dbc.Col([
                    dcc.Input(value="----", type="text", id="msj2_home2", disabled=True, style=style_big_message)
                ])
            ], className="g-0"),

            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                        id="grafico_2_home2",
                        figure={
                            "layout": {
                                "title": "",
                                "height": 425,
                                "autosize": False,
                                "margin": {"l": 40, "r": 20, "t": 25, "b": 40},
                                "plot_bgcolor": colors["background"],
                                "paper_bgcolor": colors["background"],
                                "font": {"color": colors["text"]},
                            }
                        },
                        config={"responsive": True},
                        style={"marginTop": "15px", "marginLeft": "5px",
                               "height": "425px", "width": "100%"},
                    ),
                    dcc.Interval(id="interval-grafico_2_home2", interval=interval, n_intervals=0),
                ])
            ], className="g-0"),

            dcc.Interval(id="interval-op_home2", interval=interval, n_intervals=0),
        ], width=9, style={"maxHeight": "calc(100vh - 40px)", "overflowY": "auto"}),
    ], className="g-0")
], style={"backgroundColor": colors["background"], "minHeight": "100vh", "paddingBottom": "20px"})


# =============== LÓGICA: traer datos y armar figuras ===============
def _fetch_grafico_data(timeout=DEFAULT_TIMEOUT):
    r = _session.get(GRAFICO_URL, timeout=timeout)
    r.raise_for_status()
    data = r.json()
    if not isinstance(data, list):
        raise ValueError("El endpoint no retornó una lista.")
    return data

def _to_dt(ms):
    return datetime.fromtimestamp(ms/1000.0, tz=timezone.utc)

def _figure_from_series(x, series_dict, title="Lecturas por canal"):
    fig = go.Figure()
    for name, y in series_dict.items():
        if y is None:
            continue
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines+markers", name=name))
    fig.update_layout(
        title=title,
        height=425,
        autosize=False,
        margin=dict(l=40, r=20, t=30, b=40),
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font=dict(color=colors["text"]),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(title="Tiempo"),
        yaxis=dict(title="Valor"),
    )
    return fig

def _error_figure(msg):
    fig = go.Figure()
    fig.add_annotation(text=f"Error cargando datos<br><sup>{msg}</sup>",
                       x=0.5, y=0.5, xref="paper", yref="paper", showarrow=False)
    fig.update_layout(
        height=425, autosize=False,
        plot_bgcolor=colors["background"], paper_bgcolor=colors["background"],
        font=dict(color=colors["text"]),
        margin=dict(l=40, r=20, t=30, b=40),
    )
    return fig


# =============== REGISTRO DE CALLBACKS ===============
def register_callbacks(app):
    # Gráfico 1 (todas las series)
    @app.callback(
        Output("grafico_1_home2", "figure"),
        Input("interval-grafico_1_home2", "n_intervals"),
    )
    def _update_grafico_1(_n):
        try:
            raw = _fetch_grafico_data()
            raw = sorted(raw, key=lambda d: d.get("fecha", 0))
            x = [_to_dt(d["fecha"]) for d in raw if "fecha" in d]
            ch0 = [d.get("ch0") for d in raw]
            ch1 = [d.get("ch1") for d in raw]
            ch2 = [d.get("ch2") for d in raw]
            ch3 = [d.get("ch3") for d in raw]
            return _figure_from_series(x, {"ch0": ch0, "ch1": ch1, "ch2": ch2, "ch3": ch3},
                                       title="Lecturas por canal")
        except Exception as e:
            return _error_figure(str(e))

    # Gráfico 2 (ejemplo ch0 y ch1)
    @app.callback(
        Output("grafico_2_home2", "figure"),
        Input("interval-grafico_2_home2", "n_intervals"),
    )
    def _update_grafico_2(_n):
        try:
            raw = _fetch_grafico_data()
            raw = sorted(raw, key=lambda d: d.get("fecha", 0))
            x = [_to_dt(d["fecha"]) for d in raw if "fecha" in d]
            ch0 = [d.get("ch0") for d in raw]
            ch1 = [d.get("ch1") for d in raw]
            return _figure_from_series(x, {"ch0": ch0, "ch1": ch1}, title="ch0 vs ch1")
        except Exception as e:
            return _error_figure(str(e))

    # Tarjetas izquierdas: nombres de canales + último valor
    @app.callback(
        # Valores tarjeta 1
        Output("dato1_home2", "value"),
        Output("dato2_home2", "value"),
        Output("dato3_home2", "value"),
        Output("t_deten_1_home2", "value"),
        # Valores tarjeta 2
        Output("ege_ad_home2", "value"),
        Output("disp_ad_home2", "value"),
        Output("desem_ad_home2", "value"),
        Output("t_deten_2_home2", "value"),
        # Labels tarjeta 1
        Output("lbl_ch0_l1", "children"),
        Output("lbl_ch1_l1", "children"),
        Output("lbl_ch2_l1", "children"),
        Output("lbl_ch3_l1", "children"),
        # Labels tarjeta 2
        Output("lbl_ch0_l2", "children"),
        Output("lbl_ch1_l2", "children"),
        Output("lbl_ch2_l2", "children"),
        Output("lbl_ch3_l2", "children"),
        Input("interval-ultimos-datos_home2", "n_intervals"),
    )
    def _update_cards(_n):
        try:
            raw = _fetch_grafico_data()
            if not raw:
                raise ValueError("Lista vacía")

            last = max(raw, key=lambda d: d.get("fecha", 0))

            def fmt(v):
                return "---" if v is None else f"{v:.1f}"

            v_ch0 = fmt(last.get("ch0"))
            v_ch1 = fmt(last.get("ch1"))
            v_ch2 = fmt(last.get("ch2"))
            v_ch3 = fmt(last.get("ch3"))

            n_ch0 = CANAL_NOMBRES.get("ch0", "ch0")
            n_ch1 = CANAL_NOMBRES.get("ch1", "ch1")
            n_ch2 = CANAL_NOMBRES.get("ch2", "ch2")
            n_ch3 = CANAL_NOMBRES.get("ch3", "ch3")

            return (
                v_ch0, v_ch1, v_ch2, v_ch3,   # valores card 1
                v_ch0, v_ch1, v_ch2, v_ch3,   # valores card 2 (mismo endpoint)
                n_ch0, n_ch1, n_ch2, n_ch3,   # labels card 1
                n_ch0, n_ch1, n_ch2, n_ch3,   # labels card 2
            )
        except Exception:
            # Fallbacks seguros
            n_ch0 = CANAL_NOMBRES.get("ch0", "ch0")
            n_ch1 = CANAL_NOMBRES.get("ch1", "ch1")
            n_ch2 = CANAL_NOMBRES.get("ch2", "ch2")
            n_ch3 = CANAL_NOMBRES.get("ch3", "ch3")
            return (
                "---", "---", "---", "---",
                "---", "---", "---", "---",
                n_ch0, n_ch1, n_ch2, n_ch3,
                n_ch0, n_ch1, n_ch2, n_ch3,
            )
