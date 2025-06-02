from sentence_transformers import SentenceTransformer, util

# Load pre-trained model (first time will take time to download)
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(resume_text, job_description):
    # Convert both texts to embeddings
    embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)
    
    # Compute cosine similarity
    similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    
    return float(similarity_score)
