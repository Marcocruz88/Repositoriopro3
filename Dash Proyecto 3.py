from dash import Dash, Input, Output, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd



#Lanzar app
app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

def tab1_layout():
    return dbc.Container([
        # Título
        dbc.Row([
            dbc.Col(html.H3("Pestaña: Entrada de Datos", className="text-info mb-4 text-center"), width=12)
        ]),

        # Slider de Edad
        dbc.Row([
            dbc.Col([
                html.Label("Edad del estudiante:", className="text-info mb-4"),
                dcc.Slider(
                    id="slider-edad",
                    min=0,
                    max=100,
                    step=1,
                    value=10,
                    marks={i: str(i) for i in range(0, 101, 5)},
                    tooltip={"placement": "bottom", "always_visible": True}
                )
            ], width=12)
        ]),

        # Contenido dividido en dos columnas
        dbc.Row([
            # Primera columna (8 categorías)
            dbc.Col([
                html.Label("Área de ubicación del colegio:", className="text-info mb-4"),
                dcc.Dropdown(
                    id="dropdown-ubicacion",
                    options=[
                        {"label": "URBANO", "value": "URBANO"},
                        {"label": "RURAL", "value": "RURAL"}
                    ],
                    value="URBANO",
                    placeholder="Selecciona una opción...",
                    style={
                        "backgroundColor": "#2d3436",  # Fondo oscuro del dropdown
                        "color": "#FFFFFF",  # Texto claro
                        "border": "1px solid #00cec9",  # Borde con un color turquesa vivo
                        "borderRadius": "5px",  # Bordes redondeados
                        "padding": "8px",  # Espaciado interno
                        "fontSize": "14px",  # Tamaño de fuente
                        "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.1)",  # Sombra ligera
                    },
                ),
                html.Br(),

                html.Label("¿El colegio es bilingüe?", className="text-info mb-4"),
                dcc.Dropdown(
                    id="dropdown-bilingue",
                    options=[
                        {"label": "No", "value": "N"},
                        {"label": "Desconocido", "value": "Desconocido"},
                        {"label": "Sí", "value": "S"}
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción...",
                ),
                html.Br(),

                html.Label("Calendario del colegio:", className="text-info mb-4"),
                dcc.Dropdown(
                    id="dropdown-calendario",
                    options=[
                        {"label": "A", "value": "A"},
                        {"label": "B", "value": "B"}
                    ],
                    value="A",
                    placeholder="Selecciona una opción...",
                ),
                html.Br(),

                html.Label("Carácter del colegio:", className="text-info mb-4"),
                dcc.Dropdown(
                    id="dropdown-caracter",
                    options=[
                        {"label": "ACADÉMICO", "value": "ACADÉMICO"},
                        {"label": "TÉCNICO", "value": "TÉCNICO"},
                        {"label": "TÉCNICO/ACADÉMICO", "value": "TÉCNICO/ACADÉMICO"},
                        {"label": "Desconocido", "value": "Desconocido"},
                        {"label": "NO APLICA", "value": "NO APLICA"}
                    ],
                    value="ACADÉMICO",
                    placeholder="Selecciona una opción...",
                ),
                html.Br(),

                html.Label("Jornada del colegio:", className="text-info mb-4"),
                dcc.Dropdown(
                    id="dropdown-jornada",
                    options=[
                        {"label": "ÚNICA", "value": "ÚNICA"},
                        {"label": "TARDE", "value": "TARDE"},
                        {"label": "NOCHE", "value": "NOCHE"},
                        {"label": "MAÑANA", "value": "MAÑANA"},
                        {"label": "COMPLETA", "value": "COMPLETA"},
                        {"label": "SABATINA", "value": "SABATINA"}
                    ],
                    value="ÚNICA",
                    placeholder="Selecciona una opción...",
                ),
            ], width=6),

            # Segunda columna
            dbc.Col([
                html.Label("Nivel educativo de la madre:", className="text-info mb-4"),
                dcc.Dropdown(
                    id="dropdown-educacionmadre",
                    options=[
                        {"label": "Desconocido", "value": "Desconocido"},
                        {"label": "Primaria completa", "value": "Primaria completa"},
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción...",
                ),
            ], width=6),
        ]),
    ], fluid=True)






def tab2_layout():
    return html.Div([
        html.H3("Pestaña: Resultados", className="text-info mb-4"),
        html.P("Aquí se mostrarán los resultados de la predicción.", className="text-light"),
        dcc.Graph(
            id="result-graph",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "Ejemplo"}
                ],
                "layout": {
                    "title": "Gráfico de Resultados",
                    "template": "plotly_dark"
                }
            }
        )
    ])




#Distribución de la app
app.layout=dbc.Container([

    #Titulo
    dbc.Row([
        dbc.Col(html.H1("Aplicación Predictiva", className="text-center text-info mb-4"), width=12)
    ]),

    #Pestañas: Introducir datos y visualizar resultados
    dbc.Row([
        dbc.Col(
            dcc.Tabs(id="tabs", value="tab1", children=[
                dcc.Tab(label="Entrada de datos", value="tab1", className="custom-tab"),
                dcc.Tab(label="Resultados", value="tab2", className="custom-tab")
            ], className="custom-tabs-container"), width=12
        )

    ]),

    # Contenedor para el contenido dinámico de las pestañas
    dbc.Row([
        dbc.Col(html.Div(id="tabs-content"), width=12)
    ])


], fluid=True)

@app.callback(
    Output("tabs-content", "children"),
    Input("tabs", "value")
)
def render_tab_content(tab):
    if tab == "tab1":
        return tab1_layout()
    elif tab == "tab2":
        return tab2_layout()



if __name__ == "__main__":
    app.run_server(debug=True)