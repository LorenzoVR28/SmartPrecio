import streamlit as st
import pandas as pd

# CONFIG
st.set_page_config(page_title="SmartPrecio AI", page_icon="💰", layout="wide")

# ESTILOS PRO
st.markdown("""
<style>
.main {background-color: #0f172a;}
.card {
    background: #1e293b;
    padding: 25px;
    border-radius: 20px;
    color: white;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}
.metric {font-size: 32px; font-weight: bold;}
.label {color: #94a3b8;}
.highlight {color: #38bdf8;}
.warning {background: #fef3c7; padding: 20px; border-radius: 15px; color: #92400e;}
.success {background: #dcfce7; padding: 20px; border-radius: 15px; color: #065f46;}
</style>
""", unsafe_allow_html=True)

# HEADER
st.title("💰 SmartPrecio AI")
st.caption("Optimiza tu precio con simulación inteligente de mercado")

st.markdown("---")

# INPUTS
st.markdown("## 📦 Datos del producto")

col1, col2 = st.columns(2)

with col1:
    costo = st.number_input("Costo del producto (S/)", min_value=0.0, value=13.0)

with col2:
    precio_actual = st.number_input("Precio actual (S/)", min_value=0.0, value=30.0)

col3, col4 = st.columns(2)

with col3:
    margen = st.slider("Margen deseado (%)", 0, 150, 100)

with col4:
    unidades = st.number_input("Ventas por día", min_value=1, value=10)

dias = st.slider("Periodo (días)", 1, 30, 30)

# VALIDACIONES
if precio_actual < costo:
    st.error("⚠️ Estás vendiendo por debajo de tu costo. Estás perdiendo dinero.")

if margen > 100:
    st.warning("⚠️ Un margen muy alto puede reducir tus ventas.")

if unidades > 1000:
    st.warning("⚠️ Verifica tus ventas diarias, parecen muy altas.")

# CÁLCULOS BASE
precio_sugerido = costo * (1 + margen / 100)

# 🧠 PSEUDO IA (SIMULACIÓN DE DEMANDA)
def demanda_estimada(precio, precio_base, unidades_base):
    if precio_base == 0:
        return unidades_base
    
    cambio_precio = (precio - precio_base) / precio_base
    
    # Elasticidad simple
    elasticidad = 1.2  # puedes ajustar esto
    
    factor = 1 - (cambio_precio * elasticidad)
    factor = max(0.2, min(1.5, factor))  # límites realistas
    
    return unidades_base * factor

# DEMANDAS
demanda_actual = unidades
demanda_sugerida = demanda_estimada(precio_sugerido, precio_actual, unidades)

# GANANCIAS
ganancia_actual = (precio_actual - costo) * demanda_actual * dias
ganancia_sugerida = (precio_sugerido - costo) * demanda_sugerida * dias

diferencia = ganancia_sugerida - ganancia_actual
ganancia_unitaria = precio_sugerido - costo

st.markdown("---")

# DASHBOARD
st.markdown("## 📊 Dashboard inteligente")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="label">Precio óptimo</div>
        <div class="metric highlight">S/ {precio_sugerido:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="label">Ganancia proyectada</div>
        <div class="metric">S/ {ganancia_sugerida:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="label">Demanda estimada</div>
        <div class="metric">{demanda_sugerida:.1f} / día</div>
    </div>
    """, unsafe_allow_html=True)

# ANÁLISIS INTELIGENTE
st.markdown("## 🧠 Recomendación del sistema")

if diferencia > 0:
    st.markdown(f"""
    <div class="warning">
    ⚠️ Según el modelo, podrías ganar <b>S/ {abs(diferencia):.2f}</b> adicionales.<br><br>
    💡 Subir el precio a <b>S/ {precio_sugerido:.2f}</b> mejoraría tu rentabilidad
    incluso considerando posible reducción en ventas.
    </div>
    """, unsafe_allow_html=True)

elif diferencia < 0:
    st.markdown(f"""
    <div class="success">
    ✅ Tu precio actual es más rentable que el sugerido (+S/ {abs(diferencia):.2f}).<br><br>
    🔎 Probablemente tu mercado tolera precios altos.
    </div>
    """, unsafe_allow_html=True)

else:
    st.success("Tu precio ya está optimizado según el modelo.")

# SIMULADOR AVANZADO
st.markdown("## 🔬 Simulación avanzada")

max_precio = max(precio_actual * 2, costo + 1)

nuevo_precio = st.slider(
    "Simula otro precio",
    float(costo),
    float(max_precio),
    float(precio_actual)
)

demanda_test = demanda_estimada(nuevo_precio, precio_actual, unidades)
ganancia_test = (nuevo_precio - costo) * demanda_test * dias

st.metric("Ganancia estimada", f"S/ {ganancia_test:.2f}")
st.caption("Modelo basado en comportamiento estimado del cliente (elasticidad de precio)")

# GRÁFICO
st.markdown("## 📈 Comparación de escenarios")

data = pd.DataFrame({
    "Escenario": ["Actual", "Óptimo", "Simulado"],
    "Ganancia": [ganancia_actual, ganancia_sugerida, ganancia_test]
})

st.bar_chart(data.set_index("Escenario"))

# INSIGHT PRO (ESTO VENDE)
st.markdown("## 🚀 Insight estratégico")

if precio_actual < precio_sugerido:
    st.info("Estás compitiendo por precio. Podrías subirlo sin perder demasiados clientes.")
elif precio_actual > precio_sugerido:
    st.info("Estás en zona premium. Tu mercado tolera precios altos.")
else:
    st.info("Tu estrategia de precios está equilibrada.")

# CTA
st.markdown("---")
st.markdown("## 🔓 Versión PRO próximamente")

st.markdown("""
- Predicción real con machine learning  
- Análisis de competencia  
- Guardado de datos  
- Reportes automáticos  

💰 Convierte datos en decisiones inteligentes.
""")
