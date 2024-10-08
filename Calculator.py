import torch
import torchvision
import whisper

model = whisper.load_model("base")
result = model.transcribe("06 - Paid.mp3")
    
with open("transcription.txt", "w") as f:
    f.write(result["text"])