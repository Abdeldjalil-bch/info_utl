import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Configuration de la page
st.set_page_config(
    page_title="App Sécurisée",
    page_icon="🔐",
    layout="wide"
)

# Chargement de la configuration
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Création de l'authenticator
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Interface de connexion
name, authentication_status, username = authenticator.login()

# Gestion des états d'authentification
if authentication_status == False:
    st.error('Nom d\'utilisateur/mot de passe incorrect')
elif authentication_status == None:
    st.warning('Veuillez entrer votre nom d\'utilisateur et mot de passe')
elif authentication_status:
    # Interface pour utilisateur connecté
    st.title(f'🎉 Bienvenue {name}!')
    
    # Sidebar avec logout
    with st.sidebar:
        st.write(f'Connecté en tant que **{name}**')
        authenticator.logout('Se déconnecter', 'sidebar')
    
    # Contenu principal
    st.header('📊 Tableau de bord')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("👥 Utilisateurs", "1,234")
    with col2:
        st.metric("📈 Projets", "42")
    with col3:
        st.metric("⏱️ Temps", "156h")
    
    # Zone protégée
    st.header('🔒 Contenu protégé')
    st.success('Ce contenu n\'est visible que pour les utilisateurs connectés!')
    
    # Exemple de fonctionnalités
    tab1, tab2, tab3 = st.tabs(["📈 Données", "⚙️ Paramètres", "👤 Profil"])
    
    with tab1:
        st.line_chart([1, 3, 2, 4, 5, 3, 6])
        
    with tab2:
        if username == 'admin':
            st.subheader('🔧 Panneau Admin')
            st.info('Interface admin disponible ici')
        else:
            st.info('Paramètres utilisateur')
            
    with tab3:
        st.subheader(f'Profil de {name}')
        st.write(f'**Nom d\'utilisateur:** {username}')
        st.write(f'**Email:** {config["credentials"]["usernames"][username]["email"]}')
