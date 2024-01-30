import whisper

model = whisper.load_model("medium")
result = model.transcribe("s.mp4")
print(result["text"])