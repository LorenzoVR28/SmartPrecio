import streamlit as st
import pandas as pd
import numpy as np

# ---------------- CONFIG ----------------
st.set_page_config(page_title="SmartPrecio PRO", layout="wide")

# ---------------- ESTILOS ----------------
st.markdown("""
<style>
.stApp { background-color: #0E1117; }

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(10px);}
    to {opacity: 1; transform: translateY(0);}
}

.card {
    background: linear-gradient(145deg, #1f2430, #161a22);
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.5);
    animation: fadeIn 0.5s ease-in-out;
    border: 1px solid rgba(255,255,255,0.05);
}

.card:hover {
    transform: scale(1.02);
    transition: 0.2s;
}

h1, h2, h3 { color: #00FFD1 !important; }

.metric { color: #AAA; font-size: 14px; }
.big { font-size: 30px; font-weight: bold; }

.success { color: #00FF88; font-weight: bold; }
.warning { color: #FFA500; font-weight: bold; }
.danger { color: #FF4B4B; font-weight: bold; }
.info { color: #00D1FF; font-weight: bold; }

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("💰 SmartPrecio PRO")
st.subheader("Simulador inteligente de precios y ganancias")

# ---------------- INPUTS ----------------
st.markdown("## ⚙️ Configuración")

col1, col2 = st.columns(2)

with col1:
    costo = st.number_input("Costo del producto (S/)", min_value=0.0)
    precio = st.number_input("Precio actual (S/)", min_value=0.0)

with col2:
    ventas_dia = st.number_input("Ventas por día", min_value=0)

margen_objetivo = st.slider("Margen objetivo (%)", 10, 80, 40)
dias = st.slider("Días a simular", 7, 90, 30)

# ---------------- CÁLCULOS ----------------
if costo > 0 and precio > 0:

    ganancia_unitaria = precio - costo
    margen = (ganancia_unitaria / precio) * 100 if precio > 0 else 0
    ganancia_total = ganancia_unitaria * ventas_dia * dias

    precio_optimo = costo / (1 - margen_objetivo/100)

    # ---------------- DASHBOARD ----------------
    st.markdown("## 📊 Resultados actuales")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"<div class='card'><div class='metric'>Ganancia/unidad</div><div class='big'>S/ {ganancia_unitaria:.2f}</div></div>", unsafe_allow_html=True)

    with c2:
        st.markdown(f"<div class='card'><div class='metric'>Margen</div><div class='big'>{margen:.2f}%</div></div>", unsafe_allow_html=True)

    with c3:
        st.markdown(f"<div class='card'><div class='metric'>Ganancia total</div><div class='big'>S/ {ganancia_total:.2f}</div></div>", unsafe_allow_html=True)

    # ---------------- ANÁLISIS ----------------
    st.markdown("## 🧠 Análisis inteligente")

    diferencia = precio - precio_optimo

    if ganancia_unitaria <= 0:
        estado = "❌ Estás perdiendo dinero"
        clase = "danger"
    elif diferencia > 0:
        estado = f"⚠ Estás S/ {diferencia:.2f} por encima del precio óptimo"
        clase = "info"
    elif diferencia < 0:
        estado = f"⚠ Estás S/ {-diferencia:.2f} por debajo del precio óptimo"
        clase = "warning"
    else:
        estado = "✅ Precio óptimo"
        clase = "success"

    st.markdown(f"""
    <div class="card">
        <div class="{clase}">{estado}</div>
        <p>📌 Precio óptimo sugerido: <b>S/ {precio_optimo:.2f}</b></p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- SIMULADOR PRO ----------------
    st.markdown("## 🚀 Simulador PRO (Escenarios)")

    escenarios = {
        "Conservador": 0.9,
        "Actual": 1,
        "Optimista": 1.2,
        "Agresivo": 1.4
    }

    resultados = []

    for nombre, factor in escenarios.items():
        ventas_escenario = ventas_dia * factor
        ganancia = (precio_optimo - costo) * ventas_escenario * dias

        resultados.append({
            "Escenario": nombre,
            "Ganancia": ganancia
        })

    df_escenarios = pd.DataFrame(resultados)

    st.bar_chart(df_escenarios.set_index("Escenario"))

    # ---------------- GRÁFICA ----------------
    st.markdown("## 📈 Simulación por precio")

    precios = np.linspace(costo, costo * 3, 50)
    ganancias = (precios - costo) * ventas_dia * dias

    df = pd.DataFrame({
        "Precio": precios,
        "Ganancia": ganancias
    })

    st.line_chart(df.set_index("Precio"))

    # ---------------- PSEUDO IA ----------------
    st.markdown("## 🤖 Recomendación IA")

    if margen < 20:
        st.warning("Sube precios o reduce costos. Rentabilidad baja.")
    elif margen > 50:
        st.info("Precio alto. Podrías estar perdiendo clientes.")
    else:
        st.success("Buen equilibrio entre precio y ventas.")

    # ---------------- EXTRA PRO ----------------
    st.markdown("## 🔥 Insights avanzados")

    riesgo = "Bajo" if margen > 30 else "Medio" if margen > 10 else "Alto"
    precio_psicologico = round(precio_optimo) - 0.01
    proyeccion_anual = ganancia_total * 12

    st.markdown(f"""
    <div class="card">
        ✔ Precio psicológico: S/ {precio_psicologico:.2f} <br>
        ✔ Riesgo del negocio: {riesgo} <br>
        ✔ Proyección anual: S/ {proyeccion_anual:.2f} <br>
        ✔ Recomendación: Ajustar hacia precio óptimo
    </div>
    """, unsafe_allow_html=True)

else:
    st.warning("Ingresa datos para comenzar")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("🚀 SmartPrecio PRO | Simulador de decisiones para emprendedores")
