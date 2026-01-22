Projet : Assistant IA Métier - (RAG )
Présentation du Projet
Ce projet présente un Proof of Concept (POC) d'un assistant conversationnel basé sur l'architecture RAG (Retrieval-Augmented Generation). L'objectif est de permettre aux collaborateurs d'interroger la base de connaissances interne de l'entreprise (procédures, guides, politiques RH) de manière intuitive et sécurisée.

Fonctionnalités Principales
Recherche Sémantique : Compréhension du langage naturel pour extraire des informations sans correspondance exacte des mots-clés.

Maîtrise de l'Information : Réponses limitées strictement au contexte des documents fournis pour éliminer les risques d'hallucination.

Citations des Sources : Pour chaque réponse, l'assistant indique le document source et le numéro de page correspondant.

Accessibilité : Possibilité de télécharger le document original directement depuis l'interface.

Architecture Technique
Extraction et Découpage : Utilisation de PyPDFLoader et RecursiveCharacterTextSplitter (chunks de 1500 caractères).

Base Vectorielle : ChromaDB pour le stockage des embeddings générés par HuggingFace.

Modèle de Langage (LLM) : Llama 3.1 hébergé sur l'infrastructure Groq pour une génération haute performance.

Structure du Répertoire
Plaintext

#Assistant IA Métier - (RAG)

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/) 
[![Streamlit](https://img.shields.io/badge/Streamlit-True-orange?logo=streamlit)](https://streamlit.io/) 
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

##Présentation du Projet
Ce projet est un **Proof of Concept (POC)** d'un assistant conversationnel basé sur **RAG (Retrieval-Augmented Generation)**.  
Il permet aux collaborateurs d'interroger la base de connaissances interne (procédures, guides, politiques RH) de manière **intuitive, rapide et sécurisée**.

---

##Architecture Technique
- **Extraction & Découpage** : `PyPDFLoader` + `RecursiveCharacterTextSplitter` (chunks de 1500 caractères)  
- **Base Vectorielle** : `ChromaDB` avec embeddings `HuggingFace` (`all-MiniLM-L6-v2`)  
- **Modèle de Langage (LLM)** : `Llama 3.1` via l'API **Groq**  
- **Interface Utilisateur** : `Streamlit` pour un accès simple et interactif  

---

Structure du Répertoire
plaintext
Assistant_IA/
├── app/
│   └── chat.py            # Interface utilisateur (Streamlit)
├── rag/
│   ├── retriever.py       # Moteur de recherche vectorielle
│   └── generator.py       # Logique de génération (Groq API)
├── Data/
│   └── Documents/         # Sources PDF
├── .gitignore/
│   └── .env               # Exclusion des fichiers sensibles
            
├── .env.example           # Modèle de configuration des clés API
└── requirements.txt       # Dépendances Python

Installation

Installation des dépendances :

Bash

pip install -r requirements.txt
Configuration : Créer un fichier .env à la racine avec la variable suivante :

Plaintext

GROQ_API_KEY=votre_cle_api


Exécution :
streamlit run app/chat.py


Cloner le repository :

git clone https://github.com/FIABOE/Assistant_IA.git
cd Assistant_IA
Créer un environnement virtuel :
python -m venv env

# Windows
env\Scripts\activate


