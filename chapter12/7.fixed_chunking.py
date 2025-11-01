reviews = [
    "This smartphone has an excellent camera. The photos are sharp and the colors are vibrant. Overall, very satisfied with my purchase.",
    "I was disappointed with the laptop's performance. It frequently lags and the battery life is shorter than expected.",
    "The blender works great for making smoothies. It's powerful and easy to clean. Definitely worth the price.",
    "Customer support was unresponsive. I had to wait a long time for a reply, and my issue was not resolved satisfactorily.",
    "The book is a fascinating read. The storyline is engaging and the characters are well-developed. Highly recommend to all readers."
]

from langchain_text_splitters import TokenTextSplitter

text_splitter = TokenTextSplitter(chunk_size=50, chunk_overlap=0)

text_block = " ".join(reviews)

chunks = text_splitter.split_text(text_block)

print("Chunks woth 50 tokens each:")
for i, chunk in enumerate(chunks):
   print(f"Chunk {i + 1}:")
   print(chunk)
   print("\n")

chunk_sizes = [20, 70, 150]

for size in chunk_sizes:
   print(f"Chunk Size: {size}")
   text_splitter = TokenTextSplitter(chunk_size=size, chunk_overlap=0)
   chunks = text_splitter.split_text(text_block)

   for i, chuck in enumerate(chunks):
      print(f"Chunk {i + 1}:")
      print(chunk)
      print("\n")