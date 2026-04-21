import streamlit as st
import pandas as pd

# CONFIG
st.set_page_config(page_title="SmartPrecio", page_icon="💰", layout="centered")

# HEADER
st.title("💰 SmartPrecio")
st.markdown("### Deja de adivinar precios. Empieza a ganar más.")

st.markdown(
"Optimiza cuánto cobrar y descubre cuánto podrías ganar en segundos."
)

st.divider()

# =========================
# INPUTS
# =========================
st.header("📦 Tu producto")

col1, col2 = st.columns(2)

with col1:
    costo = st.number_input("¿Cuánto te cuesta tu producto? (S/)", min_value=0.0, format="%.2f")

with col2:
    precio_actual = st.number_input("¿A cuánto lo vendes actualmente? (S/)", min_value=0.0, format="%.2f")

margen = st.slider("¿Qué margen de ganancia quieres (%)?", 0, 100, 40)

cantidad = st.number_input("¿Cuántas unidades vendes al día?", min_value=0)

dias = st.slider("Días a simular", 1, 30, 30)

st.divider()

# =========================
# LÓGICA
# =========================
if costo > 0 and cantidad > 0:

    precio_sugerido = costo * (1 + margen / 100)
    ganancia_unitaria = precio_sugerido - costo
    ganancia_dia = ganancia_unitaria * cantidad
    ganancia_mes = ganancia_dia * dias

    # ACTUAL
    if precio_actual > 0:
        ganancia_actual = (precio_actual - costo) * cantidad * dias
    else:
        ganancia_actual = 0

    diferencia = ganancia_mes - ganancia_actual

    # =========================
    # KPIs (TARJETAS)
    # =========================
    st.header("📊 Resultados clave")

    col1, col2, col3 = st.columns(3)

    col1.metric("💵 Precio sugerido", f"S/ {precio_sugerido:.2f}")
    col2.metric("📈 Ganancia mensual", f"S/ {ganancia_mes:.2f}")
    col3.metric("🧾 Ganancia por unidad", f"S/ {ganancia_unitaria:.2f}")

    # =========================
    # ALERTA PRINCIPAL
    # =========================
    st.subheader("🧠 Análisis")

    if precio_actual > 0:
        if diferencia > 0:
            st.success(f"🚀 Podrías ganar S/ {diferencia:.2f} MÁS al mes ajustando tu precio.")
        elif diferencia < 0:
            st.warning(f"⚠️ Estás perdiendo S/ {abs(diferencia):.2f} al mes con tu precio actual.")
        else:
            st.info("Tu precio actual ya es bastante bueno.")

    # =========================
    # SIMULADOR
    # =========================
    st.subheader("🎯 Simulación: ¿y si subes el precio?")

    incremento = st.slider("Subir precio (%)", 0, 100, 10)

    nuevo_precio = precio_actual * (1 + incremento / 100) if precio_actual > 0 else precio_sugerido
    nueva_ganancia = (nuevo_precio - costo) * cantidad * dias

    col1, col2 = st.columns(2)

    col1.metric("Nuevo precio", f"S/ {nuevo_precio:.2f}")
    col2.metric("Nueva ganancia", f"S/ {nueva_ganancia:.2f}")

    # =========================
    # GRÁFICA
    # =========================
    st.subheader("📉 Comparación de ganancias")

    data = pd.DataFrame({
        "Escenario": ["Actual", "Optimizado"],
        "Ganancia": [ganancia_actual, ganancia_mes]
    })

    st.bar_chart(data.set_index("Escenario"))

    # =========================
    # RESUMEN FINAL (VENDEDOR)
    # =========================
    st.subheader("📊 Resumen claro")

    if diferencia > 0:
        st.success(
            f"💰 Si ajustas tu precio, podrías ganar aproximadamente S/ {diferencia:.2f} más al mes.\n\n"
            "👉 Esto significa más ingresos sin necesidad de vender más."
        )
    else:
        st.info("Tu estrategia actual es adecuada, pero siempre puedes probar escenarios.")

else:
    st.info("👆 Ingresa tus datos para ver cuánto podrías ganar.")

st.divider()

# FOOTER
st.markdown("### 🚀 Consejo")
st.markdown("Pequeños cambios en tu precio pueden generar grandes cambios en tus ganancias.")

st.caption("SmartPrecio • Herramienta para emprendedores")
