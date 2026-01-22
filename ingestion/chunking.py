# REMPLACE : from langchain.text_splitter import RecursiveCharacterTextSplitter
# PAR :
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    # Ton code reste le même à l'intérieur
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"✅ {len(chunks)} morceaux créés.")
    return chunks