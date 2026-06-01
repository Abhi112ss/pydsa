import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from pydsa.core import registry

# Load the registry to access all 3944 problems
registry._ensure_loaded()
problems = registry.all_problems()

def build_vector_index():
    print(f"Loading embedding model...")
    # all-MiniLM-L6-v2 is the industry standard for fast, offline semantic search
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    print(f"Extracting corpus for {len(problems)} problems...")
    # We use the search_corpus() method you already built in models.py
    corpora = [p.search_corpus() for p in problems]
    
    print("Generating embeddings (this will be extremely fast on GPU)...")
    # Normalize the embeddings to length 1 so we can use simple dot product later
    vectors = model.encode(corpora, normalize_embeddings=True, show_progress_bar=True)
    
    # Save the output to the search package directory
    out_path = Path("pydsa/search/vectors.npy")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    np.save(out_path, vectors)
    print(f"Success! Vector matrix saved to {out_path} ({out_path.stat().st_size / 1024 / 1024:.1f} MB)")

if __name__ == "__main__":
    build_vector_index()