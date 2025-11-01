from transformers import pipeline

def fix_spelling(text):

    spell_check = pipeline("text2text-generation", model="oliveirguhr/spelling-correction-english-base")

    corrected = spell_check(text, max_length=2048)[0]['generated_text']

    return corrected

sample_text = "y name si from Grece."
corrected_text = fix_spelling(sample_text)

print("Original text:", sample_text)
print("Corrected text:", corrected_text)