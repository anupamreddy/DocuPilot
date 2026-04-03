import uuid
import chromadb
from chromadb.config import Settings, DEFAULT_TENANT, DEFAULT_DATABASE
from sentence_transformers import SentenceTransformer

# Use PersistentClient instead of Client(Settings(...))

def store_in_chroma(text: str) -> None:
    """ This tool takes a text and stores it in vector db/ knowledge base for future usage. """
    client = chromadb.PersistentClient(
    path="api_store",             # Directory to store your DB
    settings=Settings(),             # Use default settings
    tenant=DEFAULT_TENANT,
    database=DEFAULT_DATABASE
        )
    collection = client.get_or_create_collection(name="my_collection")

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode([text])[0]
    doc_id = str(uuid.uuid4())
    collection.add(
        documents=[text],
        embeddings=[embedding.tolist()],
        ids=[doc_id]
    )
    print(f"Stored with ID: {doc_id}")

def search_in_chroma(query: str) -> str:
    """ This tool searches in the knowledge base and returns if relevant information. If you dont have information first check here before asking help from the user."""
    client = chromadb.PersistentClient(
    path="api_store",             # Directory to store your DB
    settings=Settings(),             # Use default settings
    tenant=DEFAULT_TENANT,
    database=DEFAULT_DATABASE
        )
    collection = client.get_or_create_collection(name="my_collection")

    model = SentenceTransformer('all-MiniLM-L6-v2')

    embedding = model.encode([query])[0]
    result = collection.query(
        query_embeddings=[embedding.tolist()],
        n_results=1
    )
    docs = result.get("documents", [])
    if docs and docs[0]:
        return docs[0][0]
    return None


#store_in_chroma("password to ssh into local is root")
print(search_in_chroma("anupam favourite folder?"))
