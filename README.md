# PERHYPER
PerfHyper est un projet qui s’inscrit dans la lignée du projet ObsHyper de l’année dernière (FISE 2022). Lors de ce dernier, nos prédécesseurs ont pris en main le radar allant jusqu’à la création d’acquisitions pour valider le bon fonctionnement du radar. Du côté post-traitement ils ont réussi à concevoir un algorithme de suivi de cible en 1D suivant l’axe principal d’émission. Cependant, le RADAR n’est pas caractérisé. Nous ne connaissons pas ses limites. L’enjeu du projet PerfHyper est de déterminer ces limites et donc potentiellement d’élargir le cadre d’application du travail de nos prédécesseurs. Pour cela, nous devons donc appréhender la théorie relative aux RADAR (Ondes Électromagnétiques, Traitement du Signal etc.). À partir de cette bibliographie, il s’agit de déterminer les limites pertinentes à étudier et d’établir les protocoles des expérimentations. Nous avons aussi déterminé les limites à
étudier : à savoir la portée, l’angle d’ouverture, la résolution et la précision en termes de distance et de vitesse. Cette interface rassemble la globalité de notre travail et une méthodologie pour appréhender le système correctement. Notre volonté est qu'il devienne un outil pour les futurs utilisateurs du RADAR.

## Usage

Placez vous à la racine du projet et lancez la commande suivante pour lancer l'interface :
```bash
/perfhyper >> python3 qtdemo/qtdemo.py
```
![Image Text](https://github.com/bento7/perfhyper/blob/main/Documents-utiles/interface.png)

Pour seulement traiter les données :
```bash
/perfhyper >> python3 Post-Traitements/Chirp.py
```
## MANIM
[Manim](https://github.com/3b1b/manim) est une librairie servant à créer des images qui seront présentes au sein de l'interface. Elles seront nécessaires à l'affichage du résultat des mesures faites en temps réel lors de la démonstration de l'utilisation du RADAR. 

## Data
Tous les fichiers de mesures sont des fichiers .txt à deux colonnes. La première représente le signal émis et la seconde le signal reçu après réflexion sur une cible. Ils sont tous regroupés dans le dossier /data. La fréquence dans le nom de fichier représente la bande passante du chirp utilisé dans la forme d'ondes.

## Documents
Vous trouverez dans la rubrique/Documents-utiles les diagrammes de gantt ainsi que notre rapport de projet au format pdf.

## Tests Unitaires
Ils s'intéressent aux algorithmes de post-traitement des données. Unittest est utilisé afin de mener à bien la varification de bon fonctionnement des fonctions.

