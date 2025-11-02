from langchain_community.embeddings import HuggingFaceBgeEmbeddings

model_name = 'BAAI/bge-small-en'
model_kwargs = {"device": "cpu"}
encode_kwargs = {"normalize_embeddings": True}

bge_embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "I love machine learning and natural language processing."
]

embeddings = [bge_embeddings.embed_query(sentence) for sentence in sentences]

for i, embedding in enumerate(embeddings):
    print(f"Embedding for sentence {i+1}: {embedding[:5]}...")
    print(f"Length of embedding: {len(embedding)}")