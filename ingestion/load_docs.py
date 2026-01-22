import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

def load_professional_docs(directory_path):
    # L'IA ne lit pas des fichiers, elle lit du texte [cite: 29]
    loader = DirectoryLoader(directory_path, glob="./*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()
    
    # Nettoyage pour supprimer le bruit (en-têtes/pieds de page) [cite: 34]
    for doc in docs:
        doc.page_content = doc.page_content.replace('\n', ' ').strip()
        
    print(f"✅ {len(docs)} pages chargées.")
    return docs