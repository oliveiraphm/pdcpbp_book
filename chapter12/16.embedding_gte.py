from sentence_transformers import SentenceTransformer

model = SentenceTransformer('thenlper/gte-base')

texts = [
    "The quick brown fox jumps over the lazy dog.",
    "I love machine learning and natural language processing.",
    "Embeddings are useful for many NLP tasks."
]

embeddings = model.encode(texts)

print(f"Shape of embeddings: {embeddings.shape}")

print(f"First few values of the first embedding: {embeddings[0][:5]}")