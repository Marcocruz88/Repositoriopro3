from dash import Dash, html, Input, Output, dcc  # Asegúrate de importar callback_context
import dash_bootstrap_components as dbc
import pandas as pd

#Lanzar app
app = Dash(__name__, external_stylesheets=[dbc.themes.LITERA], suppress_callback_exceptions=True)


def tab1_layout():
    return dbc.Container([
        html.Br(),
        # Título
        dbc.Row([
            dbc.Col(html.H3("Entrada de Datos", className="text-link mb-7 text-center"), width=12)
        ]),

        dbc.Row([
            dbc.Col([
                html.Label("Edad del estudiante:", className="text-primary mb-2 text-center"),
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
                html.Label("Área de ubicación del colegio:", className="text-primary mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-ubicacion",
                    options=[
                        {"label": "URBANO", "value": "URBANO"},
                        {"label": "RURAL", "value": "RURAL"}
                    ],
                    value="URBANO",
                    placeholder="Selecciona una opción...",
                ),
                html.Br(),

                html.Label("¿El colegio es bilingüe?", className="text-primary mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-bilingue",
                    options=[
                        {"label": "No", "value": "N"},
                        {"label": "Desconocido", "value": "Desconocido"},
                        {"label": "Sí", "value": "S"}
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("Calendario del colegio:", className="text-primary mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-calendario",
                    options=[
                        {"label": "A", "value": "A"},
                        {"label": "B", "value": "B"}
                    ],
                    value="A",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("Carácter del colegio:", className="text-primary mb-2 text-center"),
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
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("Jornada del colegio:", className="text-primary mb-2 text-center"),
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
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("Naturaleza del colegio:", className="text-primary mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-naturaleza",
                    options=[
                        {"label": "OFICIAL", "value": "OFICIAL"},
                        {"label": "NO OFICIAL", "value": "NO OFICIAL"}
                    ],
                    value="OFICIAL",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("Selecciona el género del estudiante:", className="text-info mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-genero",
                    options=[
                        {"label": "Femenino", "value": "F"},
                        {"label": "Masculino", "value": "M"},
                        {"label": "Desconocido", "value": "Desconocido"}
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("Selecciona la nacionalidad del estudiante:", className="text-info mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-nacionalidad",
                    options=[
                        {"label": "Colombia", "value": "COLOMBIA"},
                        {"label": "Venezuela", "value": "VENEZUELA"},
                        {"label": "España", "value": "ESPAÑA"},
                        {"label": "Ecuador", "value": "ECUADOR"},
                        {"label": "Guatemala", "value": "GUATEMALA"}
                    ],
                    value="COLOMBIA",
                    placeholder="Selecciona una opción..."
                ),
            ], width=6),

            # Segunda columna (8 categorías)
            dbc.Col([
                html.Label("Nivel educativo de la madre:", className="text-info mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-educacionmadre",
                    options=[
                        {"label": nivel, "value": nivel} for nivel in [
                            'Desconocido', 'Secundaria (Bachillerato) completa', 'Primaria incompleta',
                            'Educación profesional completa', 'Técnica o tecnológica completa',
                            'Secundaria (Bachillerato) incompleta', 'Primaria completa', 'No sabe',
                            'Ninguno', 'Educación profesional incompleta', 'Postgrado', 'No Aplica',
                            'Técnica o tecnológica incompleta'
                        ]
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("Nivel educativo del padre:", className="text-info mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-educacionpadre",
                    options=[
                        {"label": nivel, "value": nivel} for nivel in [
                            'Desconocido', 'Secundaria (Bachillerato) completa', 'Primaria incompleta',
                            'Educación profesional completa', 'Técnica o tecnológica completa',
                            'Secundaria (Bachillerato) incompleta', 'Primaria completa', 'No sabe',
                            'Ninguno', 'Educación profesional incompleta', 'Postgrado', 'No Aplica',
                            'Técnica o tecnológica incompleta'
                        ]
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("Estrato de la vivienda:", className="text-info mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-estratovivienda",
                    options=[
                        {"label": estrato, "value": estrato} for estrato in [
                            'Desconocido', 'Estrato 1', 'Estrato 2', 'Estrato 3',
                            'Estrato 4', 'Estrato 5', 'Estrato 6', 'Sin Estrato'
                        ]
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("Número de personas en el hogar:", className="text-info mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-personashogar",
                    options=[
                        {"label": numero, "value": numero} for numero in [
                            'Desconocido', '1 a 2', '3 a 4', '5 a 6', '7 a 8',
                            '9 o más', 'Una', 'Dos', 'Tres', 'Cuatro', 'Cinco',
                            'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez', 'Once',
                            'Doce o más'
                        ]
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("¿La familia tiene automóvil?", className="text-info mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-tieneautomovil",
                    options=[
                        {"label": "Desconocido", "value": "Desconocido"},
                        {"label": "Sí", "value": "Si"},
                        {"label": "No", "value": "No"}
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("¿La familia tiene computador?", className="text-info mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-tienecomputador",
                    options=[
                        {"label": "Desconocido", "value": "Desconocido"},
                        {"label": "Sí", "value": "Si"},
                        {"label": "No", "value": "No"}
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("¿La familia tiene internet?", className="text-info mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-tieneinternet",
                    options=[
                        {"label": "Desconocido", "value": "Desconocido"},
                        {"label": "Sí", "value": "Si"},
                        {"label": "No", "value": "No"}
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción...",
                    style={
                    "backgroundColor": "#f0f0f0",  # Cambia el color de fondo
                    "color": "#000000",           # Cambia el color del texto
                    "border": "1px solid #ccc",   # Cambia el estilo del borde
                    "borderRadius": "5px"         # Añade bordes redondeados
                    }
                ),
                html.Br(),

                html.Label("¿La familia tiene lavadora?", className="text-info mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-tienelavadora",
                    options=[
                        {"label": "Desconocido", "value": "Desconocido"},
                        {"label": "Sí", "value": "Si"},
                        {"label": "No", "value": "No"}
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción...",
                ),
            ], width=6),
        ]),
    ], fluid=True)


def tab2_layout():
    return dbc.Container([
        html.Br(),
        # Primera fila: Predicción de Puntaje
        dbc.Row([
            dbc.Col([
                html.H3("Predicción de Puntaje:", className="text-link mb-2 text-center"),
                html.Br(),
                html.Br(),
                html.H1(
                    id="contador-puntaje",
                    className="display-3 text-center",
                    style={
                        "fontSize": "120px",  # Tamaño del texto
                        "textAlign": "center"  # Centrar el texto
                    }  # Color se controlará dinámicamente
                ),  # Número dinámico
            ], width=12)
        ]),

        # Intervalo para el efecto del contador
        dcc.Interval(
            id="intervalo-contador",
            interval=30,  # Actualiza cada 30ms
            n_intervals=0,  # Comienza desde 0
            max_intervals=100  # Número máximo de iteraciones
        )
    ], fluid=True)


@app.callback(
    Output("contador-puntaje", "children"),
    Output("contador-puntaje", "style"),
    Input("intervalo-contador", "n_intervals")
)
def actualizar_puntaje(n_intervals):
    # Lógica del contador
    valor_final = 432  # Número final deseado
    valor_actual = int((n_intervals / 100) * valor_final)  # Incremento proporcional
    if n_intervals >= 100:
        valor_actual = valor_final  # Detener en el valor final

    # Cambiar color basado en el valor actual
    if valor_actual <= 200:
        color = "red"
    elif 201 <= valor_actual <= 400:
        color = "orange"
    else:
        color = "green"

    # Devolver valor y estilo
    return f"{valor_actual:,}", {
        "fontSize": "120px",  # Tamaño del texto
        "textAlign": "center",  # Centrar el texto
        "color": color  # Cambiar el color dinámicamente
    }



#Distribución de la app
app.layout=dbc.Container([

    #Titulo
    dbc.Row([
        dbc.Col(html.H1("Puntaje prueba ICFES", className="text-center text-link mb-4"), width=12)
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