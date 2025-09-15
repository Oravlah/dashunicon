# login.py

from dash import html, dcc
from dash.dependencies import Input, Output, State
from utils import api_login

layout = html.Div([
    html.H2("Login"),
    dcc.Input(id="email", type="email", placeholder="Correo electrónico", value=""),
    dcc.Input(id="password", type="password", placeholder="Contraseña", value=""),
    html.Button("Ingresar", id="btn-login"),
    html.Div(id="login-msg", style={"color": "red", "marginTop": "10px"})
])

def register_callbacks(app):
    @app.callback(
        Output("login-msg", "children"),
        Output("token-store", "data"),
        Output("url", "pathname"),
        Input("btn-login", "n_clicks"),
        State("email", "value"),
        State("password", "value")
    )
    def login_callback(n_clicks, email, password):
        print(f"Callback login disparado - n_clicks: {n_clicks}, email: {email}, password: {password}", flush=True)
        if not n_clicks:
            return "", None, "/"

        if not email or not password:
            return "Debe ingresar correo y contraseña", None, "/"

        result = api_login(email, password)
        print("Resultado API:", result, flush=True)

        if result and "access" in result:
            token = result["access"]
            return "", token, "/home"
        else:
            return "Usuario o contraseña incorrectos", None, "/"
