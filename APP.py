import streamlit as st
import pandas as pd

# Configuración
st.set_page_config(page_title="SmartPrecio", page_icon="💰", layout="centered")

# Título
st.title("💰 SmartPrecio")
st.markdown("Descubre cuánto deberías cobrar para ganar más sin perder clientes.")

st.divider()

# =========================
# INPUTS
# =========================
st.header("🧮 Calculadora de Precio")

col1, col2 = st.columns(2)

with col1:
    costo = st.number_input("Costo del producto (S/)", min_value=0.0, format="%.2f")

with col2:
    margen = st.number_input("Margen deseado (%)", min_value=0.0, format="%.2f")

# =========================
# RESULTADOS
# =========================
if costo > 0:
    precio = costo * (1 + margen / 100)
    ganancia = precio - costo

    st.subheader("📊 Resultados")

    col1, col2 = st.columns(2)

    col1.metric("💵 Precio de venta", f"S/ {precio:.2f}")
    col2.metric("📈 Ganancia por unidad", f"S/ {ganancia:.2f}")

    # Mensajes inteligentes
    st.subheader("🧠 Análisis inteligente")

    if margen < 20:
        st.warning("⚠️ Margen muy bajo. Estás ganando poco.")
    elif 20 <= margen <= 40:
        st.info("ℹ️ Margen aceptable, pero mejorable.")
    elif 40 < margen <= 70:
        st.success("✅ Buen margen.")
    else:
        st.warning("⚠️ Margen muy alto. Podrías perder clientes.")

st.divider()

# =========================
# SIMULADOR
# =========================
st.header("📈 Simulador de Ganancias")

cantidad = st.number_input("Cantidad vendida por día", min_value=0)
dias = st.slider("Días a simular", 1, 30, 30)

if costo > 0 and cantidad > 0:
    ganancia_dia = ganancia * cantidad
    ganancia_mes = ganancia_dia * dias

    col1, col2 = st.columns(2)

    col1.metric("💰 Ganancia diaria", f"S/ {ganancia_dia:.2f}")
    col2.metric("📅 Ganancia total", f"S/ {ganancia_mes:.2f}")

    # =========================
    # COMPARADOR
    # =========================
    st.subheader("⚖️ Comparación de escenarios")

    precio_actual = st.number_input("Tu precio actual (S/)", min_value=0.0, format="%.2f")

    if precio_actual > 0:
        ganancia_actual = (precio_actual - costo) * cantidad * dias
        diferencia = ganancia_mes - ganancia_actual

        col1, col2 = st.columns(2)

        col1.metric("💸 Ganancia actual", f"S/ {ganancia_actual:.2f}")
        col2.metric("🚀 Ganancia optimizada", f"S/ {ganancia_mes:.2f}", delta=f"S/ {diferencia:.2f}")

        # =========================
        # RESUMEN QUE VENDE 🔥
        # =========================
        st.subheader("📊 Resumen")

        if diferencia > 0:
            st.success(f"🚀 Podrías ganar S/ {diferencia:.2f} MÁS al mes ajustando tu precio.")
        elif diferencia < 0:
            st.warning(f"⚠️ Estás perdiendo S/ {abs(diferencia):.2f} al mes con tu precio actual.")
        else:
            st.info("ℹ️ Tu precio actual ya es óptimo.")

        # =========================
        # GRÁFICA SIMPLE
        # =========================
        st.subheader("📉 Visualización")

        data = pd.DataFrame({
            "Escenario": ["Actual", "Optimizado"],
            "Ganancia": [ganancia_actual, ganancia_mes]
        })

        st.bar_chart(data.set_index("Escenario"))

    # =========================
    # RECOMENDACIÓN FINAL
    # =========================
    st.subheader("🧠 Recomendación")

    if ganancia_dia < 50:
        st.warning("⚠️ Ganancias bajas. Sube precio o vende más.")
    elif 50 <= ganancia_dia <= 200:
        st.info("ℹ️ Ganancias moderadas.")
    else:
        st.success("🚀 Buen nivel de ganancias.")

else:
    st.info("Ingresa datos para ver resultados.")

st.divider()

# Footer
st.markdown("### 🚀 Consejo")
st.markdown("Pequeños cambios en precio o volumen pueden generar grandes diferencias en tus ganancias.")

st.caption("SmartPrecio • Herramienta para negocios locales")