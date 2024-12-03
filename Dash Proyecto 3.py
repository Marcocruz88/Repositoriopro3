from dash import Dash, html, dcc, Input, Output, State, no_update
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

from dash import Dash, html, Input, Output, dcc  # Asegúrate de importar callback_context
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model


modelo = load_model("ModeloFinal.keras")

#Lanzar app
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR], suppress_callback_exceptions=True)

from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

# Inicializa la app
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR], suppress_callback_exceptions=True)

# Layout principal
app.layout = dbc.Container([
    # Título
    dbc.Row([
        dbc.Col(html.H1("Puntaje prueba ICFES", className="text-center text-light mb-4"), width=12)
    ]),

    # Pestañas
    dbc.Row([
        dbc.Col(
            dcc.Tabs(id="tabs", value="tab1", children=[
                dcc.Tab(label="Entrada de datos", value="tab1"),
                dcc.Tab(label="Resultados", value="tab2")
            ]),
            width=12
        )
    ]),

    # Contenido de la pestaña "Entrada de Datos"
    html.Div(id="tab1-content", children=[
        html.Br(),
        dbc.Row([
            dbc.Col(html.H3("Entrada de Datos", className="text-light mb-7 text-center"), width=12)
        ]),

        dbc.Row([
            dbc.Col([
                html.Label("Edad del estudiante:", className="text-success mb-2 text-center"),
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

                html.Label("Selecciona el género del estudiante:", className="text-success mb-2 text-center"),
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

                html.Label("Selecciona la nacionalidad del estudiante:", className="text-success mb-2 text-center"),
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
                )
            ], width=6),

            # Segunda columna (8 categorías)
            dbc.Col([
                html.Label("Nivel educativo de la madre:", className="text-success mb-2 text-center"),
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

                html.Label("Nivel educativo del padre:", className="text-success mb-2 text-center"),
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

                html.Label("Estrato de la vivienda:", className="text-success mb-2 text-center"),
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

                html.Label("Número de personas en el hogar:", className="text-success mb-2 text-center"),
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

                html.Label("¿La familia tiene automóvil?", className="text-success mb-2 text-center"),
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

                html.Label("¿La familia tiene computador?", className="text-success mb-2 text-center"),
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

                html.Label("¿La familia tiene internet?", className="text-success mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-tieneinternet",
                    options=[
                        {"label": "Desconocido", "value": "Desconocido"},
                        {"label": "Sí", "value": "Si"},
                        {"label": "No", "value": "No"}
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción..."
                ),
                html.Br(),

                html.Label("¿La familia tiene lavadora?", className="text-success mb-2 text-center"),
                dcc.Dropdown(
                    id="dropdown-tienelavadora",
                    options=[
                        {"label": "Desconocido", "value": "Desconocido"},
                        {"label": "Sí", "value": "Si"},
                        {"label": "No", "value": "No"}
                    ],
                    value="Desconocido",
                    placeholder="Selecciona una opción..."
                )
            ], width=6)
        ])
    ], style={"display": "block"}),  # Visible por defecto

    # Contenido de la pestaña "Resultados"
    html.Div(id="tab2-content", children=[
        html.Br(),
        dbc.Row([
            dbc.Col(html.H3("Predicción de Puntaje:", className="text-light mb-7 text-center"), width=12)
        ]),

        dbc.Row([
            dbc.Col(html.H1(id="contador-puntaje", className="display-3 text-center"), width=12)
        ]),

        dbc.Row([
            dbc.Col(
                dbc.Button("Calcular Puntaje", id="boton-calcular", color="primary", className="mt-3"),
                width={"size": 4, "offset": 4}  # Centrado
            )
        ]),

        dcc.Interval(
            id="intervalo-contador",
            interval=30,
            n_intervals=0,
            max_intervals=100,
            disabled=True
        ),

        dcc.Store(id="store-puntaje")

    ], style={"display": "none"})  # Oculto por defecto
], fluid=True)

# Callback para alternar las pestañas
@app.callback(
    [Output("tab1-content", "style"), Output("tab2-content", "style")],
    [Input("tabs", "value")]
)
def toggle_tabs(tab):
    if tab == "tab1":
        return {"display": "block"}, {"display": "none"}
    elif tab == "tab2":
        return {"display": "none"}, {"display": "block"}
    return {"display": "none"}, {"display": "none"}





@app.callback(
    Output("output-dummies", "children"),
    [
        Input("slider-edad", "value"),
        Input("dropdown-ubicacion", "value"),
        Input("dropdown-bilingue", "value"),
        Input("dropdown-calendario", "value"),
        Input("dropdown-caracter", "value"),
        Input("dropdown-jornada", "value"),
        Input("dropdown-naturaleza", "value"),
        Input("dropdown-genero", "value"),
        Input("dropdown-nacionalidad", "value"),
        Input("dropdown-educacionmadre", "value"),
        Input("dropdown-educacionpadre", "value"),
        Input("dropdown-estratovivienda", "value"),
        Input("dropdown-personashogar", "value"),
        Input("dropdown-tieneautomovil", "value"),
        Input("dropdown-tienecomputador", "value"),
        Input("dropdown-tieneinternet", "value"),
        Input("dropdown-tienelavadora", "value"),
    ]
)
def actualizar_dummies(edad,ubicacion, bilingue, calendario, caracter, jornada, naturaleza, genero, nacionalidad,
                       educacionmadre, educacionpadre, estratovivienda, personashogar, tieneautomovil,
                       tienecomputador, tieneinternet, tienelavadora):
    # Generar variables dummy
    dummies = {

        #Edad
        "edad_estudiante" : edad,

        # Ubicación
        "cole_area_ubicacion_URBANO": 1 if ubicacion == "URBANO" else 0,
        #"cole_area_ubicacion_RURAL": 1 if ubicacion == "RURAL" else 0,

        # Colegio bilingüe
        "cole_bilingue_N": 1 if bilingue == "N" else 0,
        "cole_bilingue_S": 1 if bilingue == "S" else 0,
        #"cole_bilingue_Desconocido": 1 if bilingue == "Desconocido" else 0,

        # Calendario
        #"cole_calendario_A": 1 if calendario == "A" else 0,
        "cole_calendario_B": 1 if calendario == "B" else 0,

        # Carácter del colegio
        #"cole_caracter_ACADEMICO": 1 if caracter == "ACADÉMICO" else 0,
        "cole_caracter_Desconocido": 1 if caracter == "Desconocido" else 0,
        "cole_caracter_NO_APLICA": 1 if caracter == "NO APLICA" else 0,
        "cole_caracter_TECNICO": 1 if caracter == "TÉCNICO" else 0,
        "cole_caracter_TECNICO_ACADEMICO": 1 if caracter == "TÉCNICO/ACADÉMICO" else 0,
        
        

        # Jornada del colegio
        "cole_jornada_MANIANA": 1 if jornada == "MAÑANA" else 0,
        "cole_jornada_NOCHE": 1 if jornada == "NOCHE" else 0,
        "cole_jornada_SABATINA": 1 if jornada == "SABATINA" else 0,
        "cole_jornada_TARDE": 1 if jornada == "TARDE" else 0,
        "cole_jornada_UNICA": 1 if jornada == "ÚNICA" else 0,
        #"cole_jornada_COMPLETA": 1 if jornada == "COMPLETA" else 0,
        

        # Naturaleza del colegio
        "cole_naturaleza_OFICIAL": 1 if naturaleza == "OFICIAL" else 0,
        #"cole_naturaleza_NO_OFICIAL": 1 if naturaleza == "NO OFICIAL" else 0,

        # Género del estudiante
        "genero_F": 1 if genero == "F" else 0,
        "genero_M": 1 if genero == "M" else 0,
        #"genero_Desconocido": 1 if genero == "Desconocido" else 0,

        # Nacionalidad del estudiante
        #"nacionalidad_COLOMBIA": 1 if nacionalidad == "COLOMBIA" else 0,
        "nacionalidad_ECUADOR": 1 if nacionalidad == "ECUADOR" else 0,
        "nacionalidad_ESPANIA": 1 if nacionalidad == "ESPAÑA" else 0,
        "nacionalidad_GUATEMALA": 1 if nacionalidad == "GUATEMALA" else 0,
        "nacionalidad_VENEZUELA": 1 if nacionalidad == "VENEZUELA" else 0,
    

        # Nivel educativo de la madre  SE QUITÓ DESCONOCIDO
        **{f"educacion_madre_{nivel}": 1 if educacionmadre == nivel else 0 for nivel in [
            "Educación profesional completa", "Educación profesional incompleta", "Ninguno", "No Aplica",
            "No sabe", "Postgrado", "Primaria completa", "Primaria incompleta","Secundaria (Bachillerato) completa",
            "Secundaria (Bachillerato) incompleta", "Técnica o tecnológica completa", "Técnica o tecnológica incompleta"
        ]},



        # Nivel educativo del padre SE QUITÓ DESCONOCIDO
        **{f"educacion_padre_{nivel}": 1 if educacionpadre == nivel else 0 for nivel in [
            "Educación profesional completa", "Educación profesional incompleta", "Ninguno", "No Aplica",
            "No sabe", "Postgrado", "Primaria completa", "Primaria incompleta","Secundaria (Bachillerato) completa",
            "Secundaria (Bachillerato) incompleta", "Técnica o tecnológica completa", "Técnica o tecnológica incompleta"
        ]},

        # Estrato de la vivienda SE QUITÓ DESCONOCIDO
        **{f"estrato_vivienda_{estrato}": 1 if estratovivienda == estrato else 0 for estrato in [
            "Estrato 1", "Estrato 2", "Estrato 3", "Estrato 4", "Estrato 5", "Estrato 6", "Sin Estrato"
        ]},

        # Número de personas en el hogar SE QUITO "1 a 2"
        **{f"personas_hogar_{personas}": 1 if personashogar == personas else 0 for personas in [
             "3 a 4", "5 a 6", "7 a 8", "9 o más","Cinco", "Cuatro", "Desconocido", "Diez", "Doce o más", 
             "Dos", "Nueve", "Ocho", "Once", "Seis","Siete","Tres", "Una"
     
        ]},

        # Automóvil
        "familia_tiene_automovil_No": 1 if tieneautomovil == "No" else 0,
        "familia_tiene_automovil_Si": 1 if tieneautomovil == "Si" else 0,
        #"familia_tiene_automovil_Desconocido": 1 if tieneautomovil == "Desconocido" else 0,

        # Computador
        "familia_tiene_computador_No": 1 if tienecomputador == "No" else 0,
        "familia_tiene_computador_Si": 1 if tienecomputador == "Si" else 0,
        #"familia_tiene_computador_Desconocido": 1 if tienecomputador == "Desconocido" else 0,

        # Internet
        "familia_tiene_internet_No": 1 if tieneinternet == "No" else 0,
        "familia_tiene_internet_Si": 1 if tieneinternet == "Si" else 0,
        #"familia_tiene_internet_Desconocido": 1 if tieneinternet == "Desconocido" else 0,

        # Lavadora
        "familia_tiene_lavadora_No": 1 if tienelavadora == "No" else 0,
        "familia_tiene_lavadora_Si": 1 if tienelavadora == "Si" else 0,
        #"familia_tiene_lavadora_Desconocido": 1 if tienelavadora == "Desconocido" else 0,
    }

    # Formato legible para mostrar en el frontend

    return dummies

def preparar_datos_para_modelo(dummies):

    # Extraer los valores de las dummies en el orden correcto
    dummy_values = list(dummies.values())
    
    # Convertir a un array de numpy
    array_dummies = np.array(dummy_values).reshape(1, -1)  # Forma (1, n_features)
    
    return array_dummies



from dash.exceptions import PreventUpdate  # Importar PreventUpdate

@app.callback(
    [
        Output("contador-puntaje", "children"),  # Mostrar el puntaje
        Output("contador-puntaje", "style"),  # Cambiar el estilo del puntaje
    ],
    [
        Input("boton-calcular", "n_clicks"),  # Botón de cálculo
    ],
    [
        State("slider-edad", "value"),
        State("dropdown-ubicacion", "value"),
        State("dropdown-bilingue", "value"),
        State("dropdown-calendario", "value"),
        State("dropdown-caracter", "value"),
        State("dropdown-jornada", "value"),
        State("dropdown-naturaleza", "value"),
        State("dropdown-genero", "value"),
        State("dropdown-nacionalidad", "value"),
        State("dropdown-educacionmadre", "value"),
        State("dropdown-educacionpadre", "value"),
        State("dropdown-estratovivienda", "value"),
        State("dropdown-personashogar", "value"),
        State("dropdown-tieneautomovil", "value"),
        State("dropdown-tienecomputador", "value"),
        State("dropdown-tieneinternet", "value"),
        State("dropdown-tienelavadora", "value"),
    ],
)
def calcular_puntaje(
    n_clicks,
    edad,
    ubicacion,
    bilingue,
    calendario,
    caracter,
    jornada,
    naturaleza,
    genero,
    nacionalidad,
    educacionmadre,
    educacionpadre,
    estratovivienda,
    personashogar,
    tieneautomovil,
    tienecomputador,
    tieneinternet,
    tienelavadora,
):
    if not n_clicks:
        raise PreventUpdate  # No hacer nada si el botón no ha sido presionado

    try:
        # Generar las dummies y calcular la predicción
        dummies = actualizar_dummies(
            edad,
            ubicacion,
            bilingue,
            calendario,
            caracter,
            jornada,
            naturaleza,
            genero,
            nacionalidad,
            educacionmadre,
            educacionpadre,
            estratovivienda,
            personashogar,
            tieneautomovil,
            tienecomputador,
            tieneinternet,
            tienelavadora,
        )
        datos_array = preparar_datos_para_modelo(dummies)
        puntaje_final = int(modelo.predict(datos_array)[0][0])
    except Exception:
        puntaje_final = 400  # Valor predeterminado en caso de error

    # Definir el color basado en el puntaje
    color = "red" if puntaje_final <= 200 else "orange" if puntaje_final <= 400 else "green"

    # Devolver el puntaje y el estilo correspondiente
    return f"{puntaje_final:,}", {"fontSize": "120px", "textAlign": "center", "color": color}





if __name__ == "__main__":
    app.run_server(debug=True)