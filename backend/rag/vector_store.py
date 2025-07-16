from sentence_transformers import SentenceTransformer
import faiss, pickle

# Load saved index + chunks
#model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
index, chunks = pickle.load(open("data/faiss_index.pkl", "rb"))

def retrieve_context(query: str) -> str:
    vec = model.encode([query])
    D, I = index.search(vec, k=2)
    return "\n".join([chunks[i] for i in I[0]])
