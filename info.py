# app.py
import streamlit as st

st.title("Mon App avec Authentification")

if not st.user.is_logged_in:
    if st.button("Se connecter 🔐"):
        st.login()
    st.info("Veuillez vous connecter pour accéder à l'application")
else:
    st.success(f"Bienvenue {st.user.name}!")
    st.write(f"Email: {st.user.email}")
    
    if st.button("Se déconnecter"):
        st.logout()
