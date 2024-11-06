"""
#NOM : Mehdi Benayed / Cheick GUEYE / Bastien EBELY
GROUPE : 34


# Import des bibliothèques nécessaires
import pymongo
import pandas as pd

# Connexion à la base de données MongoDB
URI = 'mongodb+srv://mango_user:udBOzFPmsR3bsZq6@cluster-but-sd.swl74.mongodb.net/?retryWrites=true&w=majority&appName=cluster-but-sd'
client = pymongo.MongoClient(URI)
db = client.tp

# Fonction pour affiché les collections disponibles
def afficher_collections():
    print("Collections disponibles: ", db.list_collection_names())

# Fonction pour le - comptage du nombre de logements
def compter_logements():
    print("Nombre de logement AIRBNB: ", db.airbnb.count_documents({}))

# Calcul du prix moyen par ville (1), trié par ordre décroissant (2)
def prix_moyen_ville():
    prix_moyen = pd.DataFrame(list(db.airbnb.aggregate([
        {"$group": {"_id": "$address.market", "prix_moyen": {"$avg": "$price"}}},
        {"$sort": {"prix_moyen": -1}}
    ])))
    print("Prix moyen par ville:")
    print(prix_moyen)

# On affiche les équipements différents
def liste_equipements():
    equipements = db.airbnb.distinct("amenities")
    print("Liste des équipements disponibles:", equipements)

# Comptage des propriétés ayant le Wifi
def compter_wifi():
    nb_wifi = db.airbnb.count_documents({"amenities": "Wifi"})
    print(f"Nombre de propriétés avec Wifi: {nb_wifi}")

# Affichage du nom, le nombre de chambres et de lits pour chaque logement
def details_logements():
    logements = pd.DataFrame(list(db.airbnb.find({}, {"_id": 0, "name": 1, "bedrooms": 1, "beds": 1})))
    print("Détails des logements:")
    print(logements)

# Affichage du nom et le prix des logements à Porto
def logements_a_porto():
    logements_porto = pd.DataFrame(list(db.airbnb.find({"address.market": "Porto"}, {"name": 1, "price": 1, "_id": 0})))
    print("Logements situés à Porto:")
    print(logements_porto)

# on chercher à trouverr les 5 hôtes les plus populaires (avec le plus de commentaires)
def top_5_hotes():
    hotes_populaires = db.airbnb.aggregate([
        {"$unwind": "$reviews"},
        {"$group": {"_id": "$name", "total_reviews": {"$sum": 1}}},
        {"$sort": {"total_reviews": -1}},
        {"$limit": 5}
    ])
    print("Top 5 des hôtes les plus populaires:")
    print(pd.DataFrame(list(hotes_populaires)))

# On veut les 6 villes avec le plus de logements disponibles
def top_6_villes():
    villes = db.airbnb.aggregate([
        {"$sortByCount": "$address.market"},
        {"$limit": 6}
    ])
    print("Top 6 des villes avec le plus de logements:")
    print(pd.DataFrame(list(villes)))

# On veut les propriétés acceptant :
# plus de 4 invités et 
# avec caution < 300€
def logements_caution():
    logements = db.airbnb.aggregate([
        {"$match": {"accommodates": {"$gt": 4}, "security_deposit": {"$lt": 300}}},
        {"$project": {"Index": "$_id", "name": 1, "security_deposit": 1, "accommodates": 1}}
    ])
    print("Logements pour plus de 4 invités avec caution < 300€:")
    print(pd.DataFrame(list(logements)))

# On veut les 20 utilisateurs qui ont mis le plus de commentaires
def top_20_commentaires():
    utilisateurs = db.airbnb.aggregate([
        {"$unwind": "$reviews"},
        {"$group": {"_id": "$reviews.reviewer_id", "name": {"$addToSet": "$reviews.reviewer_name"}, "commentaires": {"$sum": 1}}},
        {"$sort": {"commentaires": -1}},
        {"$limit": 20},
        {"$project": {"commentaires": 0}}
    ])
    print("Top 20 des utilisateurs les plus actifs:")
    print(pd.DataFrame(list(utilisateurs)))

# Note moyenne des logements à Sydney
def note_moyenne_sydney():
    note_sydney = db.airbnb.aggregate([
        {"$match": {"address.market": "Sydney"}},
        {"$group": {"_id": None, "note_moyenne": {"$avg": "$review_scores.rating"}}}
    ])
    resultat = list(note_sydney)
    if resultat:
        print(f"Note moyenne des logements à Sydney: {resultat[0]['note_moyenne']:.2f}")
    else:
        print("Aucune donnée de note disponible pour Sydney.")

# Logements contenant "park" dans le nom
def logements_avec_park():
    logements = db.airbnb.find({"name": {"$regex": "park", "$options": "i"}}, {"name": 1, "_id": 0})
    print("Logements contenant 'park' dans le nom:")
    print(pd.DataFrame(list(logements)))

# Logements avec latitude et prix spécifiés
def logements_latitude_prix():
    logements = db.airbnb.find({
        "address.location.latitude": {"$gte": 36.1, "$lte": 40.6},
        "price": {"$gte": 100, "$lte": 200}
    }, {"name": 1, "_id": 0})
    print("Logements avec latitude entre 36.1 et 40.6 et prix entre 100 et 200 euros:")
    print(pd.DataFrame(list(logements)))

# Appel des fonctions pour obtenir les réponses aux questions
if __name__ == "__main__":
    afficher_collections()
    compter_logements()
    prix_moyen_ville()
    liste_equipements()
    compter_wifi()
    details_logements()
    logements_a_porto()
    top_5_hotes()
    top_6_villes()
    logements_caution()
    top_20_commentaires()
    note_moyenne_sydney()
    logements_avec_park()
    logements_latitude_prix()

"""
