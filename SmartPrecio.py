import streamlit as st
import pandas as pd

# CONFIG
st.set_page_config(page_title="SmartPrecio AI", page_icon="💰", layout="wide")

# 🎨 ESTILO PREMIUM
st.markdown("""
<style>
.main {background-color: #020617;}
.card {
    background: linear-gradient(145deg, #0f172a, #020617);
    padding: 25px;
    border-radius: 18px;
    color: white;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.6);
    border: 1px solid rgba(255,255,255,0.05);
}
.metric {font-size: 34px; font-weight: bold;}
.label {color: #94a3b8; font-size: 14px;}
.highlight {color: #22c55e;}
.premium-box {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    padding: 25px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.1);
}
.cta {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# 🔐 PRO LOGIN
st.sidebar.markdown("## 🔐 Acceso PRO")
password = st.sidebar.text_input("Clave", type="password")
PRO_PASSWORD = "PRO2026"
is_pro = password == PRO_PASSWORD

if is_pro:
    st.sidebar.success("Modo PRO activado")
else:
    st.sidebar.info("Versión gratuita")

# HEADER
st.title("💰 SmartPrecio AI")
st.caption("Sistema inteligente para maximizar ganancias en tu negocio")

st.markdown("---")

# INPUTS
st.markdown("## 📦 Configuración del producto")

col1, col2 = st.columns(2)

with col1:
    costo = st.number_input("Costo (S/)", min_value=0.0, value=13.0)

with col2:
    precio_actual = st.number_input("Precio actual (S/)", min_value=0.0, value=30.0)

col3, col4 = st.columns(2)

with col3:
    margen = st.slider("Margen objetivo (%)", 0, 150, 100)

with col4:
    unidades = st.number_input("Ventas diarias", min_value=1, value=10)

dias = st.slider("Periodo (días)", 1, 30, 30)

# VALIDACIONES
if precio_actual < costo:
    st.error("⚠️ Estás perdiendo dinero en cada venta.")

# 🧠 MODELO
def demanda_estimada(precio, precio_base, unidades_base):
    if precio_base == 0:
        return unidades_base
    cambio = (precio - precio_base) / precio_base
    elasticidad = 1.2
    factor = 1 - (cambio * elasticidad)
    factor = max(0.3, min(1.5, factor))
    return unidades_base * factor

precio_optimo = costo * (1 + margen / 100)

demanda_optima = demanda_estimada(precio_optimo, precio_actual, unidades)

ganancia_actual = (precio_actual - costo) * unidades * dias
ganancia_optima = (precio_optimo - costo) * demanda_optima * dias

st.markdown("---")

# 📊 DASHBOARD PREMIUM
st.markdown("## 📊 Panel de decisiones")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="label">Precio óptimo</div>
        <div class="metric highlight">S/ {precio_optimo:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="label">Ganancia proyectada</div>
        <div class="metric">S/ {ganancia_optima:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="label">Demanda estimada</div>
        <div class="metric">{demanda_optima:.1f} / día</div>
    </div>
    """, unsafe_allow_html=True)

# 🧠 MENSAJE PRO
st.markdown("## 🧠 Recomendación estratégica")

diferencia = ganancia_optima - ganancia_actual

if diferencia > 0:
    st.markdown(f"""
    <div class="premium-box">
    Estás dejando de ganar aproximadamente <b>S/ {abs(diferencia):.2f}</b>.<br><br>
    Ajustar tu precio a <b>S/ {precio_optimo:.2f}</b> aumentaría tu rentabilidad
    sin afectar significativamente la demanda.
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="premium-box">
    Tu estrategia actual es eficiente.<br>
    Tu mercado acepta bien tu precio actual.
    </div>
    """, unsafe_allow_html=True)

# 🔬 PRO FEATURE
st.markdown("## 🔬 Simulación avanzada")

if is_pro:
    nuevo_precio = st.slider("Simular precio", float(costo), float(precio_actual*2), float(precio_actual))
    demanda_test = demanda_estimada(nuevo_precio, precio_actual, unidades)
    ganancia_test = (nuevo_precio - costo) * demanda_test * dias
    st.metric("Ganancia estimada", f"S/ {ganancia_test:.2f}")
else:
    st.markdown("""
    <div class="premium-box">
    🔒 Función exclusiva PRO<br><br>
    Simula escenarios y encuentra el punto exacto de máxima ganancia.
    </div>
    """, unsafe_allow_html=True)

# 📈 GRÁFICO
st.markdown("## 📈 Comparación")

data = pd.DataFrame({
    "Escenario": ["Actual", "Óptimo"],
    "Ganancia": [ganancia_actual, ganancia_optima]
})

st.bar_chart(data.set_index("Escenario"))

# 💰 CTA PREMIUM
st.markdown("---")

st.markdown("""
<div class="cta">
🚀 Desbloquea SmartPrecio PRO por solo S/10<br>
Optimiza tus precios como un negocio profesional
</div>
""", unsafe_allow_html=True)

st.markdown("📲 Escríbeme para acceso inmediato")
