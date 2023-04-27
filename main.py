import os
import wave
import asyncio
import pkg_resources
import audioop
import pyaudio
import websockets
import openai
import whisper

# check for lib installation
libs = ['pyaudio', 'websockets', 'openai', 'whisper', 'asyncio']
while libs:
    try:
        lib = libs.pop()
        pkg_resources.get_distribution(lib)
    except pkg_resources.DistributionNotFound:
        print(f'{lib} is not installed. Please run "pip install {lib}"')
    else:
        print(f'{lib} is installed')

# set OpenAI API key, getting it from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
if openai.api_key is None:
    print("OPENAI_API_KEY environment variable is not set. Please see README for more information.")
    exit()

# capture audio from microphone using pyaudio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

async def record_and_transcribe(websocket, path):
    # loop until websocket connection is closed
    while True:
        # wait for a message from the client
        message = await websocket.recv()
        print("Listening...")

        # check if message is 'start'
        if message == 'start':
            print("Start received. Recording...")

            # capture audio
            max_duration = 10  # maximum recording duration in seconds
            frames = []
            for i in range(0, int(44100 / 1024 * max_duration)):
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
            print("Sending to OpenAI...")
            transcription = transcript.text

            # print transcription
            print("Transcript received: " + transcription)

            # put the transcription in the clipboard
            os.system(f'echo {transcription} | clip')
            print("Pasted to clipboard.")

            # send transcription back to client
            await websocket.send(transcription)

        # check if message is 'stop'
        elif message == 'stop':
            break

async def main():
    async with websockets.serve(record_and_transcribe, "localhost", 8765):
        await asyncio.Future()  # run forever

# start the websocket server
asyncio.run(main())

# close stream
stream.stop_stream()
stream.close()
audio.terminate()
