import os
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from views import login, home

PREFIX = "/dashunicon/"


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    requests_pathname_prefix=PREFIX,
    routes_pathname_prefix=PREFIX,
    assets_url_path=f"{PREFIX}assets",
    serve_locally=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

server = app.server

port_web = int(os.environ.get('PUERTO_WEB', '8596'))

store_token = dcc.Store(id='token-store', storage_type='session')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    store_token,
    html.Div(id='page-content')
])

# Registrar callbacks de login
login.register_callbacks(app)
home.register_callbacks(app)

def _normalize_path(pathname: str) -> str:
    if not pathname:
        return "/"
    if pathname.startswith(PREFIX):
        rest = pathname[len(PREFIX):] 
        return "/" + rest.lstrip("/") 
    return pathname 

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'),
    Input('token-store', 'data')
)
def display_page(pathname, token):
    path = _normalize_path(pathname)
    if path == '/home':
        return home.layout if token else login.layout
    return login.layout

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_web)
