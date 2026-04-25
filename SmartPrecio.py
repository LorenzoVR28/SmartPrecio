import streamlit as st
import pandas as pd
import numpy as np

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="SmartPrecio PRO",
    layout="wide"
)

# ---------------- ESTILOS PREMIUM ----------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
}
h1, h2, h3 {
    color: #00FFD1;
}
.metric {
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN PRO ----------------
st.sidebar.title("🔐 Acceso PRO")

usuarios = {
    "admin": "1234",
    "cliente1": "abc123",
    "pro": "pro2025"
}

user = st.sidebar.text_input("Usuario")
password = st.sidebar.text_input("Contraseña", type="password")

acceso_pro = False

if user in usuarios and usuarios[user] == password:
    acceso_pro = True
    st.sidebar.success("Acceso PRO activado")
else:
    st.sidebar.warning("Modo gratuito")

# ---------------- TITULO ----------------
st.title("💰 SmartPrecio PRO")
st.subheader("Calculadora inteligente de precios + simulador de ganancias")

# ---------------- INPUTS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    costo = st.number_input("Costo del producto", min_value=0.0)

with col2:
    precio = st.number_input("Precio de venta", min_value=0.0)

with col3:
    ventas = st.number_input("Ventas estimadas (mensual)", min_value=0)

# ---------------- VALIDACIÓN ----------------
if costo > 0 and precio > 0:

    # ---------------- CÁLCULOS ----------------
    ganancia_unitaria = precio - costo
    margen = (ganancia_unitaria / precio) * 100
    ganancia_total = ganancia_unitaria * ventas

    # ---------------- PRECIO SUGERIDO (LÓGICA MEJORADA) ----------------
    margen_optimo = 40

    precio_sugerido = costo / (1 - margen_optimo/100)

    # ---------------- ESTADO REAL ----------------
    if ganancia_unitaria <= 0:
        estado = "❌ Estás perdiendo dinero"
        color = "red"
    elif margen < 20:
        estado = "⚠ Margen bajo"
        color = "orange"
    elif margen <= 50:
        estado = "✅ Buen margen"
        color = "green"
    else:
        estado = "🔥 Margen alto (posible sobreprecio)"
        color = "blue"

    # ---------------- DASHBOARD ----------------
    st.markdown("## 📊 Resultados")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"<div class='card'><div class='metric'>Ganancia/unidad</div><h2>S/ {ganancia_unitaria:.2f}</h2></div>", unsafe_allow_html=True)

    with c2:
        st.markdown(f"<div class='card'><div class='metric'>Margen</div><h2>{margen:.2f}%</h2></div>", unsafe_allow_html=True)

    with c3:
        st.markdown(f"<div class='card'><div class='metric'>Ganancia mensual</div><h2>S/ {ganancia_total:.2f}</h2></div>", unsafe_allow_html=True)

    # ---------------- MENSAJE INTELIGENTE ----------------
    st.markdown("## 🧠 Análisis inteligente")

    st.markdown(f"<div class='card'><h3 style='color:{color}'>{estado}</h3></div>", unsafe_allow_html=True)

    st.write(f"📌 Precio sugerido óptimo: **S/ {precio_sugerido:.2f}**")

    # ---------------- GRÁFICA ----------------
    st.markdown("## 📈 Simulación de ganancias")

    precios = np.linspace(costo, costo * 3, 50)
    ganancias = (precios - costo) * ventas

    df = pd.DataFrame({
        "Precio": precios,
        "Ganancia": ganancias
    })

    st.line_chart(df.set_index("Precio"))

    # ---------------- PSEUDO IA ----------------
    st.markdown("## 🤖 Recomendación automática")

    if margen < 20:
        st.warning("Tu margen es bajo. Deberías subir el precio o reducir costos.")
    elif margen > 50:
        st.info("Tu margen es alto. Evalúa si estás perdiendo ventas por precio elevado.")
    else:
        st.success("Tu precio está bien optimizado.")

    # ---------------- PRO ----------------
    if acceso_pro:
        st.markdown("## 🔓 Modo PRO")

        riesgo = "Bajo" if margen > 30 else "Medio" if margen > 10 else "Alto"

        precio_psicologico = round(precio_sugerido) - 0.01

        proyeccion = ganancia_total * 12

        st.markdown(f"""
        <div class='card'>
        <h3>📊 Análisis avanzado</h3>
        ✔ Precio psicológico: S/ {precio_psicologico:.2f}<br>
        ✔ Riesgo del negocio: {riesgo}<br>
        ✔ Proyección anual: S/ {proyeccion:.2f}<br>
        ✔ Recomendación IA: Ajustar hacia precio óptimo<br>
        </div>
        """, unsafe_allow_html=True)

        # Comparación visual PRO
        st.markdown("### 📉 Comparación de precios")

        df_pro = pd.DataFrame({
            "Tipo": ["Actual", "Óptimo"],
            "Precio": [precio, precio_sugerido]
        })

        st.bar_chart(df_pro.set_index("Tipo"))

    else:
        st.markdown("## 🔒 Desbloquea PRO")
        st.info("Accede a análisis avanzados, precios psicológicos y proyecciones.")

else:
    st.warning("Ingresa datos para comenzar")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("🚀 SmartPrecio PRO | Herramienta para emprendedores")
