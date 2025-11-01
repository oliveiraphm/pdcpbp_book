from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

text = "The quokka, a rare marsuapial,"

indexed_tokens = tokenizer.encode(text, return_tensors='pt')

output_text = model.generate(indexed_tokens, max_length=50, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
output_text_decoded = tokenizer.decode(output_text[0], skip_special_tokens=True)
print(output_text_decoded)