# Projet Base de Données

## Installation

## Prérequis

- Python 3.12 or later
- uvicorn 0.20.0
- fastapi 0.112.2
- pymongo 4.8.0

## Installation

1. Clone le repertoire
```
https://github.com/TheLuven/FlaskAPI_TP.git
```
2. Mettre le repertoire root (pour Pycharm)

Click droit sur le repertoire `pymongo-fastapi-crud` -> Mark Directory as -> Sources Root

3. Mettre sa base de données Mongo

Aller dans le fichier .env (path: `pymongo-fastapi-crud/.env`) 

Changer la valeur de `ATLAS_URI` par votre propre URI de connexion à votre base de données Mongo 
(Sur altas, cliquer sur cluster. Puis cliquer sur `connect` -> `Driver` et choisir `Python`)

4. Lancer le serveur

```
cd ./pymongo-fastapi-crud
uvicorn main:app --reload
```

5. Aller sur openApi
```
http://127.0.0.1:8000/docs#
```

## Problèmes possibles
1. Erreur lors de la connection à la base de données : `Exception SSL handshake failed`

Solution :

Aller sur atlas, dans la partie `Network Access` et cliquer sur `+Add IP ADDRESS`
Puis cliquer sur `ADD CURRENT IP ADDRESS` et `CONFIRM`

2. OpenApi ne s'affiche pas
Si le lancement du serveur, c'est bien passé mais que la page charge dans le vide :
 - essayer de fermer le navigateur et de le relancer
 - essayer de fermer pycharm et de le relancer
 - et si ça ne marche toujours pas, essayer de redémarrer l'ordinateur

