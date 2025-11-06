

import os
import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output


df = pd.read_csv("edadmedia.csv")


df_long = df.melt(id_vars=["Year"], var_name="Departamento", value_name="EdadMedia")


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server 

app.title = "Evolución de la Edad Media (Guatemala)"


departamentos = sorted(df_long["Departamento"].unique())

# Layout

app.layout = html.Div([
    html.H3("Evolución de la Edad Media por Departamento en Guatemala", className="mt-3"),
    html.P("Selecciona los departamentos que deseas visualizar:"),
    
    # Dropdown 
    dcc.Dropdown(
        id="departamento_dropdown",
        options=[{"label": d, "value": d} for d in departamentos],
        value=departamentos[:5],  # muestra los primeros 5 por defecto
        multi=True,
        style={"width": "80%", "margin": "auto"}
    ),
    
    # Gráfica
    dcc.Graph(id="grafico"),
], style={"padding": "20px"})


# Callback

@app.callback(
    Output("grafico", "figure"),
    Input("departamento_dropdown", "value")
)
def actualizar_grafico(depts):
    # Filtrar los datos por los departamentos seleccionados
    if not depts:
        depts = departamentos[:5]
    dff = df_long[df_long["Departamento"].isin(depts)]
    
 
    fig = px.line(
        dff,
        x="Year",
        y="EdadMedia",
        color="Departamento",
        title="Evolución de la Edad Media por Departamento en Guatemala",
        labels={"Year": "Año", "EdadMedia": "Edad media (años)"},
        markers=True
    )
    

    fig.update_layout(
        title_font_size=20,
        legend_title_text="Departamento",
        plot_bgcolor="white",
        hovermode="x unified"
    )
    
    return fig


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render asigna el puerto
    app.run_server(host="0.0.0.0", port=port, debug=False)
