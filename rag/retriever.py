import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def get_relevant_chunks(query):
    # Chemin vers la base de données locale
    chemin_chroma = r"D:\Bachelor3 DATA IA\Projet IA\Assistant_IA\chroma_db"
    
    # Configuration du modèle de recherche 
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    try:
        # On se connecte à la base ChromaDB
        vectorstore = Chroma(
            persist_directory=chemin_chroma, 
            embedding_function=embeddings
        )
        
        # k=5  valeurs proches de la question posée
        search_results = vectorstore.similarity_search(query, k=5)
        
        return search_results
        
    except Exception as e:
        print(f"Erreur lors de la récupération dans la base : {e}")
        return []