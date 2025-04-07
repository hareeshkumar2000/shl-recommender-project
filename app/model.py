from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np

class SHLRecommender:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        with open("data/shl_data.json") as f:
            self.data = json.load(f)
        self.index = self.build_index()

    def build_index(self):
        embeddings = [self.model.encode(item["name"]) for item in self.data]
        self.embedding_matrix = np.array(embeddings).astype("float32")
        index = faiss.IndexFlatL2(self.embedding_matrix.shape[1])
        index.add(self.embedding_matrix)
        return index

    def recommend(self, query, k=10):
        query_vec = self.model.encode([query]).astype("float32")
        _, indices = self.index.search(query_vec, k)
        return [self.data[i] for i in indices[0]]