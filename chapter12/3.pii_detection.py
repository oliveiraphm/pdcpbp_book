import pandas as pd
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

data = {
    'text': [
        "Hello, my name is John Doe. My email is john.doe@example.com",
        "Contact Jane Smith at jane.smith@work.com",
        "Call her at 987-654-3210.",
        "This is a test message without PII."
    ]
}

df = pd.DataFrame(data)

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def anonymize_text(text):
    analyzer_results = analyzer.analyze(text=text, entities=["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER"], language="en")

    operators = {
        "PERSON": OperatorConfig("mask", {"masking_char": "*", "chars_to_mask": 4, "from_end": True}),
        "EMAIL_ADDRESS": OperatorConfig("mask", {"masking_char": "*", "chars_to_mask": 5, "from_end": True}),
        "PHONE_NUMBER": OperatorConfig("mask", {"masking_char": "*", "chars_to_mask": 6, "from_end": True})

    }

    anonymized_result = anonymizer.anonymize(text=text, analyzer_results=analyzer_results, operators=operators)

    return anonymized_result.text

df['anonymized_text'] = df['text'].apply(anonymize_text)