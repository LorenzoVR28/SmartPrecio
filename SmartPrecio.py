import streamlit as st
import pandas as pd
import numpy as np

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="SmartPrecio PRO",
    layout="wide"
)

# ---------------- ESTILOS + ANIMACIONES ----------------
st.markdown("""
<style>

/* Fondo */
.stApp {
    background-color: #0E1117;
}

/* Animación fade */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Cards */
.card {
    background: linear-gradient(145deg, #1f2430, #161a22);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.05);
    animation: fadeIn 0.6s ease-in-out;
}

/* Hover efecto */
.card:hover {
    transform: scale(1.02);
    transition: 0.25s;
}

/* Títulos */
h1, h2, h3 {
    color: #00FFD1 !important;
}

/* Texto */
.card, .card p, .card span, .card div {
    color: #FFFFFF !important;
}

/* Métricas */
.metric {
    font-size: 16px;
    color: #AAAAAA;
}

/* Números grandes */
.big-number {
    font-size: 32px;
    font-weight: bold;
}

/* Estados */
.success { color: #00FF88; font-weight: bold; }
.warning { color: #FFA500; font-weight: bold; }
.danger { color: #FF4B4B; font-weight: bold; }
.info { color: #00D1FF; font-weight: bold; }

/* Botón estilo premium */
.stButton button {
    background: linear-gradient(90deg, #00FFD1, #00BFFF);
    color: black;
    border-radius: 10px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN PRO ----------------
st.sidebar.title("🔐 Acceso PRO")

usuarios = {
    "admin": "1234",
    "pro": "pro2025"
}

user = st.sidebar.text_input("Usuario")
password = st.sidebar.text_input("Contraseña", type="password")

acceso_pro = user in usuarios and usuarios[user] == password

if acceso_pro:
    st.sidebar.success("Modo PRO activado")
else:
    st.sidebar.warning("Modo gratuito")

# ---------------- HEADER ----------------
st.title("💰 SmartPrecio PRO")
st.subheader("Calculadora inteligente de precios con análisis avanzado")

# ---------------- INPUTS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    costo = st.number_input("Costo del producto", min_value=0.0)

with col2:
    precio = st.number_input("Precio de venta", min_value=0.0)

with col3:
    ventas = st.number_input("Ventas mensuales", min_value=0)

# ---------------- LÓGICA ----------------
if costo > 0 and precio > 0:

    ganancia_unitaria = precio - costo
    margen = (ganancia_unitaria / precio) * 100
    ganancia_total = ganancia_unitaria * ventas

    margen_optimo = 40
    precio_sugerido = costo / (1 - margen_optimo/100)

    # Estado
    if ganancia_unitaria <= 0:
        estado = "❌ Estás perdiendo dinero"
        clase = "danger"
    elif margen < 20:
        estado = "⚠ Margen bajo"
        clase = "warning"
    elif margen <= 50:
        estado = "✅ Buen margen"
        clase = "success"
    else:
        estado = "🔥 Margen alto (posible sobreprecio)"
        clase = "info"

    # ---------------- DASHBOARD ----------------
    st.markdown("## 📊 Resultados")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="card">
            <div class="metric">Ganancia por unidad</div>
            <div class="big-number">S/ {ganancia_unitaria:.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="card">
            <div class="metric">Margen</div>
            <div class="big-number">{margen:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="card">
            <div class="metric">Ganancia mensual</div>
            <div class="big-number">S/ {ganancia_total:.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- ANÁLISIS ----------------
    st.markdown("## 🧠 Análisis inteligente")

    st.markdown(f"""
    <div class="card">
        <div class="{clase}">{estado}</div>
        <p>📌 Precio sugerido óptimo: <b>S/ {precio_sugerido:.2f}</b></p>
    </div>
    """, unsafe_allow_html=True)

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
        st.warning("Sube tu precio o reduce costos para mejorar rentabilidad.")
    elif margen > 50:
        st.info("Podrías estar perdiendo ventas por precio alto.")
    else:
        st.success("Tu precio está bien optimizado.")

    # ---------------- PRO ----------------
    if acceso_pro:

        riesgo = "Bajo" if margen > 30 else "Medio" if margen > 10 else "Alto"
        precio_psicologico = round(precio_sugerido) - 0.01
        proyeccion = ganancia_total * 12

        st.markdown("## 🔓 Modo PRO")

        st.markdown(f"""
        <div class="card">
            <h3>📊 Análisis avanzado</h3>
            <p>✔ Precio psicológico: S/ {precio_psicologico:.2f}</p>
            <p>✔ Riesgo del negocio: {riesgo}</p>
            <p>✔ Proyección anual: S/ {proyeccion:.2f}</p>
            <p>✔ Recomendación IA: Ajustar hacia precio óptimo</p>
        </div>
        """, unsafe_allow_html=True)

        # Comparación visual
        st.markdown("### 📊 Comparación")

        df_pro = pd.DataFrame({
            "Tipo": ["Actual", "Óptimo"],
            "Precio": [precio, precio_sugerido]
        })

        st.bar_chart(df_pro.set_index("Tipo"))

    else:
        st.markdown("## 🔒 Versión PRO")
        st.info("Desbloquea análisis avanzado y proyecciones.")

else:
    st.warning("Ingresa datos para comenzar")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("🚀 SmartPrecio PRO | Herramienta para emprendedores")
