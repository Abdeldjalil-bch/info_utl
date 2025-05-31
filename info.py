import streamlit as st

# Vérification si l'utilisateur n'est pas connecté
if not st.experimental_user.is_logged_in:
    # Affichage du bouton de connexion
    if st.button("Log in :material/login:"):
        st.login()
else:
    # L'utilisateur est connecté - affichage du bouton de déconnexion
    if st.button("Log out :material/logout:"):
        st.logout()

# Affichage du contenu principal après connexion
st.markdown(
    f"""<p style='font-size: 20pt;'>Hello <img src='{st.experimental_user.picture}' style='height: 40px; width: 40px; vertical-align: middle;'> <b>{st.experimental_user.name}</b>,</p>
    <p style='font-size: 20pt;'>You have successfully logged in with <b>{st.experimental_user.email}</b>.</p>""",
    unsafe_allow_html=True
)

# Exemple d'utilisation des informations utilisateur
st.write("## Informations utilisateur disponibles :")
if st.experimental_user.is_logged_in:
    st.write(f"**Nom :** {st.experimental_user.name}")
    st.write(f"**Email :** {st.experimental_user.email}")
    st.write(f"**Photo de profil :** {st.experimental_user.picture}")
    st.write(f"**Connecté :** {st.experimental_user.is_logged_in}")
else:
    st.write("Veuillez vous connecter pour voir vos informations.")

# Exemple de contenu protégé
if st.experimental_user.is_logged_in:
    st.write("## Contenu protégé")
    st.success("Vous avez accès à cette section car vous êtes connecté !")
    
    # Ici vous pouvez ajouter du contenu réservé aux utilisateurs connectés
    st.write("### Tableau de bord personnel")
    st.info(f"Bienvenue {st.experimental_user.name} ! Voici votre espace personnel.")
    
    # Exemple de données personnalisées
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Visites", "42")
    with col2:
        st.metric("Projets", "7")
    with col3:
        st.metric("Dernière connexion", "Aujourd'hui")
else:
    st.warning("Connectez-vous pour accéder au contenu personnalisé.")
