from langchain.text_splitter import RecursiveCharacterTextSplitter

reviews = [
    "This smartphone has an excellent camera. The photos are sharp and the colors are vibrant. Overall, very satisfied with my purchase.",
    "I was disappointed with the laptop's performance. It frequently lags and the battery life is shorter than expected.",
    "The blender works great for making smoothies. It's powerful and easy to clean. Definitely worth the price.",
    "Customer support was unresponsive. I had to wait a long time for a reply, and my issue was not resolved satisfactorily.",
    "The book is a fascinating read. The storyline is engaging and the characters are well-developed. Highly recommend to all readers."
]


text_block = " ".join(reviews)


text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=200,
    chunk_overlap=0,
    length_function=len
)

chunks = text_splitter.split_text(text_block)

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}:")
    print(chunk.strip())
    print("-" * 50)