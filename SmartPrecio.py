import streamlit as st

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="SmartPrecio",
    page_icon="💰",
    layout="wide"
)

# ESTILOS (mejor presentación tipo dashboard)
st.markdown("""
    <style>
    .metric-card {
        background-color: #111827;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
    }
    .big-text {
        font-size: 28px;
        font-weight: bold;
    }
    .positive {
        color: #10B981;
    }
    .negative {
        color: #EF4444;
    }
    .warning {
        background-color: #FEF3C7;
        padding: 15px;
        border-radius: 10px;
        color: #92400E;
    }
    .success {
        background-color: #D1FAE5;
        padding: 15px;
        border-radius: 10px;
        color: #065F46;
    }
    </style>
""", unsafe_allow_html=True)

# TÍTULO
st.title("💰 SmartPrecio")
st.subheader("Calcula el precio óptimo de tu producto y maximiza tus ganancias")

# INPUTS
st.header("📦 Tu producto")

col1, col2 = st.columns(2)

with col1:
    costo = st.number_input("¿Cuánto te cuesta tu producto? (S/)", min_value=0.0, value=13.0)

with col2:
    precio_actual = st.number_input("¿A cuánto lo vendes actualmente? (S/)", min_value=0.0, value=30.0)

margen = st.slider("¿Qué margen de ganancia quieres (%)?", 0, 200, 100)

unidades = st.number_input("¿Cuántas unidades vendes al día?", min_value=1, value=10)

dias = st.slider("Días a simular", 1, 30, 30)

# CÁLCULOS
precio_sugerido = costo * (1 + margen / 100)

ganancia_actual = (precio_actual - costo) * unidades * dias
ganancia_sugerida = (precio_sugerido - costo) * unidades * dias

diferencia = ganancia_sugerida - ganancia_actual

# RESULTADOS
st.header("📊 Resultados clave")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div>Precio sugerido</div>
        <div class="big-text">S/ {precio_sugerido:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div>Ganancia mensual</div>
        <div class="big-text">S/ {ganancia_sugerida:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    ganancia_unitaria = precio_sugerido - costo
    st.markdown(f"""
    <div class="metric-card">
        <div>Ganancia por unidad</div>
        <div class="big-text">S/ {ganancia_unitaria:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# ANÁLISIS INTELIGENTE
st.header("🧠 Análisis")

if diferencia > 0:
    st.markdown(f"""
    <div class="warning">
    ⚠️ Estás dejando de ganar <b>S/ {abs(diferencia):.2f}</b> al mes con tu precio actual.<br><br>
    👉 Recomendación: Ajusta tu precio a <b>S/ {precio_sugerido:.2f}</b> para mejorar tu rentabilidad.
    </div>
    """, unsafe_allow_html=True)

elif diferencia < 0:
    st.markdown(f"""
    <div class="success">
    ✅ Estás ganando <b>S/ {abs(diferencia):.2f}</b> más al mes que el precio sugerido.<br><br>
    ⚠️ Pero cuidado: un precio alto podría reducir tus ventas.
    </div>
    """, unsafe_allow_html=True)

else:
    st.success("✔️ Tu precio ya está optimizado.")

# INSIGHT DE NEGOCIO (esto vende)
st.header("🚀 Insight estratégico")

if precio_actual > precio_sugerido:
    st.info("Tu precio es alto. Podrías estar perdiendo clientes aunque ganes más por unidad.")
elif precio_actual < precio_sugerido:
    st.info("Tu precio es bajo. Estás sacrificando rentabilidad.")
else:
    st.info("Tu precio está bien equilibrado.")

# MINI GRÁFICO (simple pero poderoso)
st.header("📈 Comparación")

import pandas as pd

data = pd.DataFrame({
    "Escenario": ["Actual", "Sugerido"],
    "Ganancia": [ganancia_actual, ganancia_sugerida]
})

st.bar_chart(data.set_index("Escenario"))

# CTA (esto es CLAVE para vender)
st.markdown("---")
st.markdown("### 🔥 ¿Quieres llevar tu negocio al siguiente nivel?")
st.markdown("""
- Predicción de ventas con IA  
- Recomendación automática de precios  
- Análisis de competencia  
- Guardado de datos y reportes  

👉 Próximamente versión PRO
""")
