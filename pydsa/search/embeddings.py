"""
pydsa.search.embeddings
~~~~~~~~~~~~~~~~~~~~~~~~
Vector-embedding search layer.
"""
from __future__ import annotations
import logging
from pathlib import Path
from pydsa.core.models import Problem
from pydsa.core import registry

log = logging.getLogger(__name__)

_model = None
_vectors = None
_is_ready = False

def is_available() -> bool:
    """Check if the optional search dependencies and index are installed."""
    global _is_ready, _model, _vectors
    if _is_ready:
        return True
        
    try:
        import numpy as np
        from sentence_transformers import SentenceTransformer
        
        vector_path = Path(__file__).parent / "vectors.npy"
        if not vector_path.exists():
            return False
            
        # Lazy load the model and matrix only when the user actually performs a search
        _vectors = np.load(vector_path)
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        _is_ready = True
        return True
    except ImportError:
        return False

def search(query: str, top_k: int = 5) -> list[tuple[Problem, float]]:
    """
    Search via pre-computed embeddings using cosine similarity.
    """
    if not is_available():
        return []
        
    import numpy as np
    
    # 1. Embed the user's query
    query_vec = _model.encode([query], normalize_embeddings=True)[0]
    
    # 2. Fast matrix multiplication (dot product for cosine similarity)
    scores = np.dot(_vectors, query_vec)
    
    # 3. Get the indices of the highest scoring problems
    top_indices = np.argsort(scores)[::-1][:top_k]
    
    problems = registry.all_problems()
    
    # Map indices back to actual Problem objects and return
    return [(problems[idx], float(scores[idx])) for idx in top_indices]