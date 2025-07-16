from sentence_transformers import SentenceTransformer
import faiss, pickle

text = open("data/mhgap_bangla.txt", encoding="utf-8").read()
chunks = text.split("\n\n")
#model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
embeddings = model.encode(chunks)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
pickle.dump((index, chunks), open("data/faiss_index.pkl", "wb"))