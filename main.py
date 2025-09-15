import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from views import login, home
import os
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

port_web = os.environ.get('PUERTO_WEB')

store_token = dcc.Store(id='token-store', storage_type='session')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    store_token,
    html.Div(id='page-content')
])

# Registrar callbacks de login
login.register_callbacks(app)

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'),
    Input('token-store', 'data')
)
def display_page(pathname, token):
    if pathname == '/home':
        if token:
            return home.layout
        else:
            return login.layout
    return login.layout

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_web)
