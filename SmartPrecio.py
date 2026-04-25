import streamlit as st
import pandas as pd
import numpy as np

# ---------------- CONFIG ----------------
st.set_page_config(page_title="SmartPrecio PRO", layout="wide")

# ---------------- ESTILOS ----------------
st.markdown("""
<style>

/* Fondo */
.stApp {
    background-color: #0E1117;
}

/* Animación */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(8px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Cards */
.card {
    background-color: #1c1f26;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.05);
    animation: fadeIn 0.4s ease-in-out;
}

/* Hover */
.card:hover {
    transform: scale(1.01);
    transition: 0.2s;
}

/* Textos */
.card * {
    color: #FFFFFF !important;
}

/* Títulos */
h1, h2, h3 {
    color: #00FFD1 !important;
}

/* Métricas */
.metric {
    font-size: 14px;
    color: #BBBBBB;
}

.value {
    font-size: 28px;
    font-weight: bold;
}

/* Estados */
.ok { color: #00FF88; font-weight: bold; }
.warn { color: #FFA500; font-weight: bold; }
.bad { color: #FF4B4B; font-weight: bold; }
.info { color: #00D1FF; font-weight: bold; }

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("💰 SmartPrecio PRO")
st.caption("Simulador inteligente de precios y ganancias")

# ---------------- INPUTS ----------------
st.subheader("⚙️ Configuración")

c1, c2, c3 = st.columns(3)

with c1:
    costo = st.number_input("Costo (S/)", min_value=0.0, value=10.0)

with c2:
    precio = st.number_input("Precio actual (S/)", min_value=0.0, value=20.0)

with c3:
    ventas_dia = st.number_input("Ventas por día", min_value=0, value=5)

margen_objetivo = st.slider("Margen objetivo (%)", 10, 80, 40)
dias = st.slider("Días a simular", 7, 90, 30)

# ---------------- VALIDACIÓN ----------------
if costo > 0 and precio > 0:

    # Cálculos base
    ganancia_unit = precio - costo
    margen = (ganancia_unit / precio) * 100 if precio else 0
    ganancia_total = ganancia_unit * ventas_dia * dias

    precio_optimo = costo / (1 - margen_objetivo/100)

    # ---------------- RESULTADOS ----------------
    st.subheader("📊 Resultados")

    r1, r2, r3 = st.columns(3)

    r1.markdown(f"""
    <div class="card">
        <div class="metric">Ganancia por unidad</div>
        <div class="value">S/ {ganancia_unit:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

    r2.markdown(f"""
    <div class="card">
        <div class="metric">Margen</div>
        <div class="value">{margen:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

    r3.markdown(f"""
    <div class="card">
        <div class="metric">Ganancia total</div>
        <div class="value">S/ {ganancia_total:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- ANÁLISIS ----------------
    st.subheader("🧠 Análisis")

    diff = precio - precio_optimo

    if ganancia_unit <= 0:
        mensaje = "❌ Estás perdiendo dinero"
        clase = "bad"
    elif diff > 0:
        mensaje = f"⚠ Precio alto (+S/ {diff:.2f} sobre óptimo)"
        clase = "info"
    elif diff < 0:
        mensaje = f"⚠ Precio bajo (-S/ {-diff:.2f} bajo óptimo)"
        clase = "warn"
    else:
        mensaje = "✅ Precio óptimo"
        clase = "ok"

    st.markdown(f"""
    <div class="card">
        <div class="{clase}">{mensaje}</div>
        <p>Precio sugerido: <b>S/ {precio_optimo:.2f}</b></p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- ESCENARIOS ----------------
    st.subheader("🚀 Simulación por escenarios")

    escenarios = {
        "Conservador": 0.8,
        "Actual": 1,
        "Optimista": 1.2,
        "Agresivo": 1.5
    }

    data = []

    for nombre, factor in escenarios.items():
        ventas = ventas_dia * factor
        ganancia = (precio_optimo - costo) * ventas * dias
        data.append([nombre, ganancia])

    df_esc = pd.DataFrame(data, columns=["Escenario", "Ganancia"])

    st.bar_chart(df_esc.set_index("Escenario"))

    # ---------------- CURVA ----------------
    st.subheader("📈 Ganancia según precio")

    precios = np.linspace(costo, costo * 3, 50)
    ganancias = (precios - costo) * ventas_dia * dias

    df = pd.DataFrame({"Precio": precios, "Ganancia": ganancias})

    st.line_chart(df.set_index("Precio"))

    # ---------------- IA ----------------
    st.subheader("🤖 Recomendación")

    if margen < 20:
        st.warning("Margen bajo → sube precio o reduce costo")
    elif margen > 50:
        st.info("Margen alto → podrías perder ventas")
    else:
        st.success("Buen equilibrio precio-ganancia")

    # ---------------- INSIGHTS ----------------
    st.subheader("🔥 Insights")

    riesgo = "Bajo" if margen > 30 else "Medio" if margen > 10 else "Alto"
    psicologico = round(precio_optimo) - 0.01
    anual = ganancia_total * 12

    st.markdown(f"""
    <div class="card">
        <p>✔ Precio psicológico: S/ {psicologico:.2f}</p>
        <p>✔ Riesgo: {riesgo}</p>
        <p>✔ Proyección anual: S/ {anual:.2f}</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.info("Ingresa valores válidos para iniciar")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("SmartPrecio PRO — Simulador para emprendedores")
