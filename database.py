import faiss
import os
import json
import numpy as np

INDEX_PATH = "index/faiss.index"
META_PATH = "index/meta.json"

def load_index(dim):
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(META_PATH, "r") as f:
            meta = json.load(f)
    else:
        index = faiss.IndexFlatL2(dim)
        meta = []
    return index, meta

def save_index(index, meta):
    os.makedirs("index", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "w") as f:
        json.dump(meta, f)

def add_note(index, meta, embedding, text):
    index.add(np.array([embedding]).astype('float32'))
    meta.append(text)

def search(index, meta, query_embedding, k=5, threshold=0.3):
    D, I = index.search(
        np.array([query_embedding]).astype('float32'), k
    )

    results = []

    for dist, idx in zip(D[0], I[0]):
        if idx < len(meta):
            score = 1 / (1 + dist)
            if score >= threshold:
                results.append((meta[idx], score))

    # fallback: if nothing passes threshold, return best match anyway
    if not results and len(I[0]) > 0:
        best_idx = I[0][0]
        best_dist = D[0][0]
        score = 1 / (1 + best_dist)
        results.append((meta[best_idx], score))

    return results