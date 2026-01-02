import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Same sentences (order must match index)
sentences = [
    "I love machine learning",
    "Artificial intelligence is the future",
    "I enjoy playing football",
    "Python is great for data science",
    "Football is a popular sport",
    "I like AI and data science"
]

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("sentence_index.faiss")

# Query sentence
query = "I like AI and data science"

# Create query embedding
query_embedding = model.encode([query], convert_to_numpy=True)
faiss.normalize_L2(query_embedding)

# Search top-k
k = 3
scores, indices = index.search(query_embedding, k)

# Display ranked results
print(f"\nQuery: {query}\n")
for rank, (idx, score) in enumerate(zip(indices[0], scores[0]), start=1):
    print(f"{rank}. {sentences[idx]} (score={score:.4f})")
