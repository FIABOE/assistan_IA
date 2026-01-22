Projet : Assistant IA Métier - TechCorp (RAG System)
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

Assistant_IA/
├── app/
│   └── chat.py             # Interface utilisateur (Streamlit)
├── rag/
│   ├── __init__.py         # Initialisation du package
│   ├── retriever.py        # Moteur de recherche vectorielle
│   └── generator.py        # Logique de génération de réponses
├── Data/
│   └── Documents/          # Répertoire des sources PDF
├── chroma_db/              # Base de données vectorielle locale
├── .env                    # Configuration des clés API (non versionné)
└── requirements.txt        # Dépendances du projet
Installation
Installation des dépendances :

Bash

pip install -r requirements.txt
Configuration : Créer un fichier .env à la racine avec la variable suivante :

Plaintext

GROQ_API_KEY=votre_cle_api
Exécution :

Bash

streamlit run app/chat.py





