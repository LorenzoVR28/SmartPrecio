import streamlit as st
import pandas as pd

# CONFIG
st.set_page_config(page_title="SmartPrecio PRO", page_icon="💰", layout="wide")

# ESTILOS PRO
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background-color: #0f172a;
}
.card {
    background: #1e293b;
    padding: 25px;
    border-radius: 20px;
    color: white;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}
.metric {
    font-size: 32px;
    font-weight: bold;
}
.label {
    color: #94a3b8;
}
.highlight {
    color: #38bdf8;
}
.warning {
    background: #fef3c7;
    padding: 20px;
    border-radius: 15px;
    color: #92400e;
}
.success {
    background: #dcfce7;
    padding: 20px;
    border-radius: 15px;
    color: #065f46;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.title("💰 SmartPrecio PRO")
st.caption("Optimiza tu precio y gana más sin complicarte")

st.markdown("---")

# INPUTS EN TARJETA
st.markdown("## 📦 Datos de tu producto")

col1, col2 = st.columns(2)

with col1:
    costo = st.number_input("Costo del producto (S/)", value=13.0)

with col2:
    precio_actual = st.number_input("Precio actual (S/)", value=30.0)

col3, col4 = st.columns(2)

with col3:
    margen = st.slider("Margen deseado (%)", 0, 200, 100)

with col4:
    unidades = st.number_input("Ventas por día", value=10)

dias = st.slider("Periodo (días)", 1, 30, 30)

# CÁLCULOS
precio_sugerido = costo * (1 + margen / 100)

ganancia_actual = (precio_actual - costo) * unidades * dias
ganancia_sugerida = (precio_sugerido - costo) * unidades * dias

diferencia = ganancia_sugerida - ganancia_actual
ganancia_unitaria = precio_sugerido - costo

st.markdown("---")

# DASHBOARD
st.markdown("## 📊 Dashboard de ganancias")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="label">Precio sugerido</div>
        <div class="metric highlight">S/ {precio_sugerido:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="label">Ganancia estimada</div>
        <div class="metric">S/ {ganancia_sugerida:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="label">Ganancia por unidad</div>
        <div class="metric">S/ {ganancia_unitaria:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# MENSAJE INTELIGENTE
st.markdown("## 🧠 Decisión inteligente")

if diferencia > 0:
    st.markdown(f"""
    <div class="warning">
    ⚠️ Estás dejando de ganar <b>S/ {abs(diferencia):.2f}</b> en {dias} días.<br><br>
    👉 Subir tu precio a <b>S/ {precio_sugerido:.2f}</b> podría mejorar tu negocio.
    </div>
    """, unsafe_allow_html=True)

elif diferencia < 0:
    st.markdown(f"""
    <div class="success">
    ✅ Estás ganando más que el promedio (+S/ {abs(diferencia):.2f}).<br><br>
    💡 Pero revisa si tu precio afecta tus ventas.
    </div>
    """, unsafe_allow_html=True)

else:
    st.success("Tu precio está perfectamente optimizado.")

# SIMULADOR EXTRA (esto sube MUCHO el valor)
st.markdown("## 🔬 Simulación de escenarios")

nuevo_precio = st.slider("Prueba otro precio", float(costo), float(precio_actual * 2), float(precio_actual))

ganancia_test = (nuevo_precio - costo) * unidades * dias

st.metric("Ganancia con este precio", f"S/ {ganancia_test:.2f}")

# GRÁFICO
st.markdown("## 📈 Comparación visual")

data = pd.DataFrame({
    "Escenario": ["Actual", "Sugerido", "Simulado"],
    "Ganancia": [ganancia_actual, ganancia_sugerida, ganancia_test]
})

st.bar_chart(data.set_index("Escenario"))

# CIERRE (VENTA)
st.markdown("---")
st.markdown("## 🚀 Lleva tu negocio al siguiente nivel")

st.markdown("""
🔓 **Versión PRO incluirá:**
- Predicción automática de ventas con IA  
- Recomendación dinámica de precios  
- Historial y seguimiento  
- Reportes descargables  

💰 Ideal para emprendedores que quieren crecer rápido.
""")
