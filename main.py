import streamlit as st
import pandas as pd

facteurs = pd.read_csv("data/facteurs.csv")
facteurs = facteurs[[elt for elt in facteurs.columns if not elt.startswith("Unn")]]

def get_prescription(type_cesar, facteurs):
    if len(facteurs[facteurs["is_majeur"]])!=0:
        return "Anti coagulation 6 semaines + BAT"

    if len(facteurs[~facteurs["is_majeur"]])>=2:
        if type_cesar=="programmee":
            return "BAT + anticoagulation 7 jours"
        if type_cesar=="urgence":
            return "Anticoagulation 6 semaines"

    if len(facteurs[~facteurs["is_majeur"]])<=1 and type_cesar=="programmee":
            return "Pas anticoagulation + BAT 7 jours"

    if len(facteurs[~facteurs["is_majeur"]])==0 and type_cesar=="urgence":
        return "Pas anticoagulation + BAT 7 jours"

    if len(facteurs[~facteurs["is_majeur"]])==1 and type_cesar=="urgence":
        return "Anticoagulation 7 jours  + BAT"

    return "Pas de diagnostic"




if "is_urgence" not in st.session_state:
    st.session_state.is_urgence = False


def on_change():
    st.session_state.is_urgence = not st.session_state.is_urgence

col1, col2  = st.columns([3,2], gap="large")

with col1:
    st.header("Paramètres", divider="violet")
    st.toggle(
        label="Césarienne en urgence" if st.session_state.is_urgence else "Césarienne programmée",
        value=st.session_state.is_urgence,
        on_change=on_change,
    )
    options = st.multiselect(
        "Facteurs de risque présents",
        facteurs["nom"],
    )
    
    type_cesar = "urgence" if st.session_state.is_urgence else "programmee"
    ticked_facteurs = facteurs[facteurs["nom"].isin(options)]

with col2:
    st.header("Recommandation", divider="violet")
    st.write(get_prescription(type_cesar, ticked_facteurs))
