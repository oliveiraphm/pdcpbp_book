import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')


text = "The quick brown fox jumps over teh lazy dog. It's unaffordable!"

word_tokens = word_tokenize(text)

print("Word tokens:")
print(word_tokens)