from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

sentence = "BERT embeddings are very useful for natural language processing tasks."

inputs = tokenizer(sentence, return_tensors='pt')

with torch.no_grad():
    outputs = model(**inputs)

last_hidden_states = outputs.last_hidden_state

print("Shape of the embeddings tensor:", last_hidden_states.shape)

cls_embedding = last_hidden_states[0, 0, :].numpy()
print("CLS token embedding:", cls_embedding)

first_word_embedding = last_hidden_states[0, 1, :].numpy()
print("First word embedding:", first_word_embedding)