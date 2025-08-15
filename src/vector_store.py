from sentence_transformers import SentenceTransformer
import chromadb

def create_vector_store():
    client = chromadb.Client()
    collection = client.create_collection("finance_data")
    return collection

if __name__ == "__main__":
    model = SentenceTransformer("all-MiniLM-L6-v2")
    print("Embedding model loaded.")
