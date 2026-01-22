import os
import shutil
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# --- CONFIGURATION DES CHEMINS ---
# On pointe directement dans le sous-dossier Documents
PATH_DOCS = r"D:\Bachelor3 DATA IA\Projet IA\Assistant_IA\Data\Documents"
PATH_CHROMA = r"D:\Bachelor3 DATA IA\Projet IA\Assistant_IA\chroma_db"

def run_ingestion():
    # 1. Nettoyage pour éviter les mélanges avec l'ancienne base OpenAI
    if os.path.exists(PATH_CHROMA):
        print("🧹 Nettoyage de l'ancienne base...")
        shutil.rmtree(PATH_CHROMA)

    # 2. Chargement des PDF
    print(f"⏳ Lecture des PDF dans : {PATH_DOCS}")
    loader = DirectoryLoader(
        PATH_DOCS, 
        glob="*.pdf", 
        loader_cls=PyPDFLoader
    )
    docs = loader.load()
    
    # 3. Vérification de sécurité
    if len(docs) == 0:
        print("❌ ERREUR : Toujours 0 page chargée. Vérifie le chemin !")
        return

    print(f"📄 {len(docs)} pages chargées. Découpage...")
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,  # Plus grand pour garder les contextes entiers
    chunk_overlap=300  # On répète 300 caractères du bloc précédent pour la continuité
)
    chunks = text_splitter.split_documents(docs)
    
    # 4. Création des vecteurs (Embeddings gratuits)
    print("🧠 Création des vecteurs Hugging Face...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 5. Sauvegarde dans ChromaDB
    vectorstore = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=PATH_CHROMA
    )
    print(f"✅ Succès ! Base créée avec {len(chunks)} morceaux de texte.")

if __name__ == "__main__":
    run_ingestion()