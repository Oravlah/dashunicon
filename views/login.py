# login.py

from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from utils import api_login

# ====== estilos ======
BG_COLOR = "#0f1b2b"          # fondo app (azul muy oscuro)
CARD_BG = "#172739"           # fondo tarjeta
ACCENT   = "#c08a2b"          # dorado del botón/borde (ajústalo si quieres)

card_style = {
    "backgroundColor": CARD_BG,
    "border": f"1px solid rgba(255,255,255,0.08)",
    "borderRadius": "14px",
    "boxShadow": "0 10px 24px rgba(0,0,0,0.35)",
    "padding": "28px",
    "width": "100%",
    "maxWidth": "520px",
}

label_style = {
    "color": "rgba(255,255,255,0.9)",
    "fontSize": "0.95rem",
    "marginBottom": "6px",
}

input_style = {
    "backgroundColor": "#0e1b2a",
    "color": "white",
    "border": "1px solid rgba(255,255,255,0.15)",
}

title_style = {
    "color": "white",
    "fontWeight": "700",
    "textAlign": "center",
    "marginTop": "8px",
    "marginBottom": "18px",
}

button_style = {
    "backgroundColor": ACCENT,
    "borderColor": ACCENT,
    "width": "100%",
    "fontWeight": "600",
}

footer_style = {
    "color": "rgba(255,255,255,0.7)",
    "fontSize": "0.8rem",
    "textAlign": "center",
    "marginTop": "12px",
}

layout = html.Div(
    [
        # Centrado vertical/horizontal de toda la vista
        html.Div(
            dbc.Card(
                dbc.CardBody(
                    [
                        # Logo
                        html.Div(
                            html.Img(
                                #src="/assets/tensor_logo.png",
                                style={
                                    "height": "56px",
                                    "objectFit": "contain",
                                    "filter": "drop-shadow(0 2px 6px rgba(0,0,0,0.5))",
                                },
                            ),
                            style={"display": "flex", "justifyContent": "center", "marginBottom": "6px"},
                        ),

                        html.H4("Inicio de sesión", style=title_style),

                        # Correo
                        html.Label("Correo", style=label_style),
                        dbc.Input(
                            id="email",
                            type="email",
                            placeholder="nombre.apellido@ejemplo.com",
                            value="",
                            style=input_style,
                        ),
                        html.Div(style={"height": "12px"}),

                        # Password
                        html.Label("Contraseña", style=label_style),
                        dbc.Input(
                            id="password",
                            type="password",
                            placeholder="••••••••",
                            value="",
                            style=input_style,
                        ),
                        html.Div(style={"height": "18px"}),

                        # Botón
                        dbc.Button("Iniciar sesión", id="btn-login", n_clicks=0, style=button_style),

                        # Mensaje de error / feedback (con spinner mientras valida)
                        dcc.Loading(
                            type="dot",
                            color="white",
                            children=html.Div(id="login-msg", style={"color": "#ff6b6b", "marginTop": "12px"}),
                        ),

                        # Footer
                        html.Div("© 2025 Tensor. Todos los derechos reservados.", style=footer_style),
                    ]
                ),
                style=card_style,
            ),
            style={
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "minHeight": "100vh",
                "padding": "24px",
            },
        )
    ],
    style={"backgroundColor": BG_COLOR},
)


def register_callbacks(app):
    @app.callback(
        Output("login-msg", "children"),
        Output("token-store", "data"),
        Output("url", "pathname"),
        Input("btn-login", "n_clicks"),
        State("email", "value"),
        State("password", "value"),
        prevent_initial_call=False,
    )
    def login_callback(n_clicks, email, password):
        # Render inicial sin mensaje
        if not n_clicks:
            return "", None, "/"

        if not email or not password:
            return "Debe ingresar correo y contraseña.", None, "/"

        try:
            result = api_login(email, password)
        except Exception as e:
            return f"Error de conexión: {e}", None, "/"

        if result and "access" in result:
            token = result["access"]
            return "", token, "/home"

        return "Usuario o contraseña incorrectos.", None, "/"
