import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa


processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")


audio_path = "chapter13/audio/3.chain orchestrator.mp3"  # Replace with your actual audio file path

audio, rate = librosa.load(audio_path, sr=16000)

input_features = processor(audio, sampling_rate=rate, return_tensors="pt").input_features

with torch.no_grad():
    predicted_ids = model.generate(input_features)

transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

print("Transcribed Text:")
print(transcription)