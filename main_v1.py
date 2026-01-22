import os
import shutil
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# --- CONFIGURATION DES CHEMINS RELATIFS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_DOCS = os.path.join(BASE_DIR, "Data", "Documents")
PATH_CHROMA = os.path.join(BASE_DIR, "chroma_db")

def run_ingestion():
    # 1. Nettoyage automatique
    if os.path.exists(PATH_CHROMA):
        print(f"Nettoyage de l'ancienne base dans : {PATH_CHROMA}")
        shutil.rmtree(PATH_CHROMA)

    # 2. Chargement des PDF
    print(f"Lecture des PDF dans : {PATH_DOCS}")
    
    # Sécurité : vérifier si le dossier existe
    if not os.path.exists(PATH_DOCS):
        print(f"ERREUR : Le dossier {PATH_DOCS} est introuvable.")
        return

    loader = DirectoryLoader(
        PATH_DOCS, 
        glob="*.pdf", 
        loader_cls=PyPDFLoader
    )
    docs = loader.load()
    
    if len(docs) == 0:
        print("ERREUR : 0 page chargée. Vérifiez que vos PDF sont bien dans Data/Documents.")
        return

    print(f" {len(docs)} pages chargées. Découpage...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
    )
    chunks = text_splitter.split_documents(docs)
    
    # 4. Création des vecteurs
    print(" Création des vecteurs Hugging Face...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 5. Sauvegarde
    vectorstore = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=PATH_CHROMA
    )
    print(f"Succès ! Base créée avec {len(chunks)} morceaux de texte.")

if __name__ == "__main__":
    run_ingestion()