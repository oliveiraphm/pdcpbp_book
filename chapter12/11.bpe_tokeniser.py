from tokenizers import Tokenizer

tokenizer = Tokenizer.from_pretrained("gpt2")

text = "Tokenization in medical texts can include words like hyperlipidemia.."

encoding = tokenizer.encode(text)

print("Tokens:", encoding.tokens)

print("Token IDs:", encoding.ids)

decoded_text = tokenizer.decode(encoding.ids)
print("Decoded Text:", decoded_text)