
import streamlit as st


def login():
    st.title("Sistema de Gestión")
    st.subheader("Inicio de sesión")

    usuario = st.text_input("Usuario")

    contrasena = st.text_input(
        "Contraseña",
        type="password"
    )

    if st.button("Iniciar sesión"):

        if usuario == "" or contrasena == "":
            st.warning("Debe completar todos los campos.")

        elif usuario == "admin" and contrasena == "1234":

            st.session_state["sesion_iniciada"] = True
            st.session_state["usuario"] = usuario

            st.success("Inicio de sesión exitoso.")
            st.rerun()

        else:
            st.error("Usuario o contraseña incorrectos.")
