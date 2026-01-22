from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

def create_and_save_store(chunks):
    # Transformer chaque chunk en vecteur [cite: 53]
    embeddings = OpenAIEmbeddings()
    
    # Stocker le texte, le vecteur et la source [cite: 60, 61, 62, 63]
    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    # Sauvegarde locale pour rendre chaque réponse traçable [cite: 67]
    vectorstore.save_local("faiss_index")
    print("✅ Mémoire (Base vectorielle) sauvegardée dans 'faiss_index'.")
    return vectorstore