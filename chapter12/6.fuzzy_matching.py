from transformers import pipeline
from thefuzz import process, fuzz

def fix_spelling(text, threshold=80):

    spell_check = pipeline("text2text-generation", model="oliverguhr/spelling-correction-english-base")
    corrected = spell_check(text, max_length=2048)[0]['generated_text']

    original_words = text.split()
    corrected_words = corrected.split()

    common_words = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at'])

    final_words = []
    for orig, corr in zip(original_words, corrected_words):
        if orig.lower() in common_words:
            final_words.append(orig)
        else:
            matches = process.extractOne(orig, [corr], scorer=fuzz.ratio)
            if matches[1] >= threshold:
                final_words.append(matches[0])
            else:
                final_words.append(orig)
    
    return ' '.join(final_words)

sample_text = "Lets do a copmarsion of speling mistaks in this sentense."
corrected_text = fix_spelling(sample_text)

print("Original Text:", sample_text)
print("Corrected text:", corrected_text)