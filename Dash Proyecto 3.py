from dash import Dash, Input, Output, html, dcc
import dash_bootstrap_components as dbc

#Lanzar app
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


#Distribución de la app
app.layout=dbc.Container([
    dbc.Row([dbc.Col(html.H1("Aplicación Predictiva", className="text-center text-info mb-4"), width=12)

    ])
])



if __name__ == "__main__":
    app.run_server(debug=True)