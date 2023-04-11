# neosWhisper Audio Transcription Service Specification

## Overview

neosWhisper is a real-time audio transcription service that utilizes the OpenAI API to transcribe audio input into text. The service listens for audio input via a websocket connection, and when triggered, it records audio from the microphone and sends the audio data to the OpenAI API for transcription. The resulting transcription is returned to the client via the websocket connection.

## User Stories

- As a user, I want to be able to start and stop audio recording from my microphone via a websocket connection.
- As a user, I want to receive real-time audio transcription via the websocket connection while the recording is ongoing.
- As a user, I want to receive the final transcription once the recording has been stopped.

## System Architecture

### Technologies Used

- Python 3.8 or above
- PyAudio library for audio input/output
- OpenAI API for audio transcription
- Websockets library for the websocket connection

### System Components

1. Server: The server component of the system listens for incoming websocket connections and handles the audio recording and transcription tasks.
2. Client: The client component of the system sends commands to the server via the websocket connection and receives real-time transcription updates and the final transcription result.

### Communication Protocol

The system utilizes a websocket connection for communication between the server and client. The following messages can be sent between the client and server:

- `start`: Triggers the server to start recording audio from the microphone and sending the audio data to the OpenAI API for transcription.
- `stop`: Triggers the server to stop recording audio and return the final transcription result to the client.

### Data Flow

1. Client sends `start` message to the server via the websocket connection.
2. Server receives `start` message and begins recording audio from the microphone.
3. Server sends real-time audio transcription updates to the client via the websocket connection.
4. Client sends `stop` message to the server via the websocket connection.
5. Server stops recording audio and sends the final transcription result to the client via the websocket connection.

## Technical Details

### Server Component

The server component of the system is responsible for receiving incoming websocket connections, recording audio, sending audio data to the OpenAI API for transcription, and sending transcription updates and final results to the client via the websocket connection.

#### Server Workflow

1. The server starts and listens for incoming websocket connections.
2. When a websocket connection is established, the server waits for a `start` message from the client.
3. When a `start` message is received, the server begins recording audio from the microphone using PyAudio.
4. The recorded audio is written to a temporary file on disk.
5. The server sends real-time transcription updates to the client by streaming the audio data to the OpenAI API and returning the transcription as it is generated.
6. When a `stop` message is received from the client, the server stops recording audio and sends the final transcription result to the client.
7. The server waits for a new `start` message from the client and repeats the process.

#### Server Implementation Details

The server component of the system is implemented in Python using the asyncio library for managing the websocket connection and the PyAudio library for recording audio.

The following libraries are required:

- Python 3.8 or above
- PyAudio
- OpenAI API
- Websockets

The following functions and classes are implemented:

- `start_recording`: Begins recording audio from the microphone and writing the recorded audio data to a temporary file on disk.
- `transcribe_audio`: Sends the recorded audio data to the OpenAI API for transcription and returns the transcription results as they are generated.
- `stop_recording`: Stops recording audio and returns the final transcription result.