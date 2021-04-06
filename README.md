# Penguin-Classification-webApp-Streamlit

![penguins image](image/image.jpeg?raw=True "Penguins image")
<br>
Cette application prédit les espèces de ***manchots palmer!***
Grace a differents criteres il permet de determiner le type de pengouin(manchot) parmi 3 especes a savoir:
+ Adelie
+ Chinstrap
+ Gentoo
Le dataset a ete obtenu par [Allison Horst](https://github.com/allisonhorst/palmerpenguins)
Le dataset nettoyer est disponible [ici](https://github.com/dataprofessor/data/blob/master/penguins_cleaned.csv)

Le fichier `create_model.py` permet de creer un model de classification par foret aleatoire grace au dataset contenu dans le fichier `penguins_cleaned.csv`

<br>

### Ce qui doit etre installer sur la machine
***
+ Python
+ Streamlit
+ numpy
+ Pandas
+ base64
+ sklearn
<br>

### Pour executer l'application
***
`streamlit run penguins-app.py`

<br>

### Navigation dans l'application
***
Une fois lancer vous pouvez deroller la fleche a votre gauche afin de voir tous les parametres qu'on peut changer en fonction du type de pengouin dont on veut connaitre le type

Si vous avez deja les parametres dans un fichier csv vous pouvez l'uploader directement
_**Attention!!!**_: votre fichier csv doit respecter la structure defini dans le fichier `penguins_example_test.csv`

<br>

Source
***
Ce travail a vu le cour grace a cette [video](https://www.youtube.com/watch?v=Eai1jaZrRDs&t=103s&ab_channel=DataProfessor) 
