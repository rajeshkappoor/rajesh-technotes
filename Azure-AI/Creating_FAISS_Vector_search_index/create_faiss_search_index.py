import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Sample sentences
sentences = [
    "I love machine learning",
    "Artificial intelligence is the future",
    "I enjoy playing football",
    "Python is great for data science",
    "Football is a popular sport",
    "I like AI and data science"
]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(sentences, convert_to_numpy=True)

# Normalize embeddings (important for cosine similarity)
faiss.normalize_L2(embeddings)

# Create FAISS index (cosine similarity via inner product)
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)

# Add vectors to index
index.add(embeddings)

# Save index locally
faiss.write_index(index, "sentence_index.faiss")

print(f"Index created with {index.ntotal} vectors")
