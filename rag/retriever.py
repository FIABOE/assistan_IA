import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def get_relevant_chunks(query):
    # Chemin vers ta base de données locale
    chemin_chroma = r"D:\Bachelor3 DATA IA\Projet IA\Assistant_IA\chroma_db"
    
    # Configuration du modèle de recherche (doit être le même que dans main_v1.py)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    try:
        # On se connecte à la base ChromaDB
        vectorstore = Chroma(
            persist_directory=chemin_chroma, 
            embedding_function=embeddings
        )
        
        # --- OPTIMISATION POUR TON BACHELOR ---
        # On passe k=5 au lieu de 3. 
        # Cela donne plus de texte à l'IA pour qu'elle trouve les 1500€ du budget.
        search_results = vectorstore.similarity_search(query, k=5)
        
        return search_results
        
    except Exception as e:
        print(f"❌ Erreur lors de la récupération dans la base : {e}")
        return []