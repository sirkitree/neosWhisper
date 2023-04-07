import os
import pyaudio
import wave
import openai
import asyncio
import websockets

# set OpenAI API key, getting it from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# capture audio from microphone using pyaudio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# loop until "stop" is detected
while True:
    # when there is silence, write to file
    frames = []
    for i in range(0, int(44100 / 1024 * 5)):
        data = stream.read(1024)
        frames.append(data)

    # write to file
    wf = wave.open('audio.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

    # open file
    f = open("audio.wav", "rb")

    # send request to OpenAI API
    transcript = openai.Audio.transcribe("whisper-1", f)

    # print transcription
    transcription = transcript.text
    print(transcription)

    # put the transcription in the clipboard
    os.system(f'echo {transcription} | clip')

    # check for the presence of the stop phrase
    if "stop" in transcription.lower():
        break

# close stream
stream.stop_stream()
stream.close()
audio.terminate()
