import string

text = "I love this product!!! It's amazing!!!"

replaced_text = text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
print("Replaced Text:", replaced_text)

removed_text = "".join(char for char in text if char.isalnum() or char.isspace())
print("Removed Text:", removed_text)