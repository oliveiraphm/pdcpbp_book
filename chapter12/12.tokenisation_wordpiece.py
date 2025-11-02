from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

text = "Tokenization in medical texts can include words like hyperlipidemia."

tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)

input_ids = tokenizer.convert_tokens_to_ids(tokens)
print("Input IDs:", input_ids)