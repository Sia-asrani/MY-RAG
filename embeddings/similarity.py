"""finding cosine similarity - 
how similar/geometrically closer query and chunk vector are in latent space"""

import numpy as np

def cosine_similarity(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.dot(v1,v2)
    
    