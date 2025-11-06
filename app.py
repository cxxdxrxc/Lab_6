import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Evolución de la Edad Media por Departamento en Guatemala")

df = pd.read_csv("edadmedia.csv")
df_long = df.melt(id_vars=["Year"], var_name="Departamento", value_name="EdadMedia")

fig = px.line(
    df_long,
    x="Year",
    y="EdadMedia",
    color="Departamento",
    title="Evolución de la Edad Media por Departamento (Guatemala)",
    labels={"Year": "Año", "EdadMedia": "Edad media (años)"},
    markers=True
)
st.plotly_chart(fig)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))  # Render provee PORT
    app.run_server(host="0.0.0.0", port=port, debug=False)
