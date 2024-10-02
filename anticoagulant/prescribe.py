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

