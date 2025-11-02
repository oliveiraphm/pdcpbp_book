import torch
import pandas as pd
from transformers import WhisperProcessor, WhisperForConditionalGeneration, AutoModelForSequenceClassification, AutoTokenizer
import librosa
import numpy as np

whisper_processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
whisper_model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")

emotion_model_name = "j-hartmann/emotion-english-distilroberta-base"
emotion_tokenizer = AutoTokenizer.from_pretrained(emotion_model_name)
emotion_model = AutoModelForSequenceClassification.from_pretrained(emotion_model_name)


audio_path = "chapter13/audio/3.chain orchestrator.mp3"  # Replace with your actual audio file path

audio, rate = librosa.load(audio_path, sr=16000)


def split_audio(audio, rate, chunk_duration=30):
    chunk_length = int(rate * chunk_duration)
    num_chunks = int(np.ceil(len(audio) / chunk_length))
    return [audio[i*chunk_length:(i+1)*chunk_length] for i in range(num_chunks)]

def transcribe_audio(audio_chunk, rate):

    input_features = whisper_processor(audio_chunk, sampling_rate=rate, return_tensors="pt").input_features

    with torch.no_grad():
        predicted_ids = whisper_model.generate(input_features)

    transcription = whisper_processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription

def detect_emotion(text):
    inputs = emotion_tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = emotion_model(**inputs)
    predicted_class_id = torch.argmax(outputs.logits, dim=-1).item()
    emotions = emotion_model.config.id2label
    return emotions[predicted_class_id]

audio_chunks = split_audio(audio, rate, chunk_duration=30)  # 30-second chunks

df = pd.DataFrame(columns=['Chunk Index', 'Transcription', 'Emotion'])

for i, audio_chunk in enumerate(audio_chunks):
    transcription = transcribe_audio(audio_chunk, rate)
    emotion = detect_emotion(transcription)
    
    df.loc[i] = [i, transcription, emotion]
    print(f"Processed Chunk {i+1}/{len(audio_chunks)}")

print(df)


df.to_csv('transcriptions_with_emotions.csv', index=False)