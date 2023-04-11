# Neos Whisper
Implements a websocket server which records microphone audio through PyAudio and transcribes the recording through the OpenAI API the returns the transcription as a string over the websocket.

## Installation
`pip install -r requirements.txt`

## Usage
1. Set your OpenAI API key in your environment variables as `OPENAI_API_KEY`
  * more info: 
    * https://www.perplexity.ai/search/7442538c-2a75-44dd-aeec-ab3634a969e5?s=u
    * https://openai.com/blog/openai-api/
    * https://openai.com/docs/api-reference/authentication/
2. Run `python main.py`

### Within Neos
1. Create a new websocket component
2. Set the websocket URL to `ws://localhost:8765`
3. Utilize the Websocket with LogiX
 ![logix screenshot](./2023-04-10%2018.55.42.jpg)

It's also bundled with a tool tip in Neos. Here's the shared directory link:
- neosrec:///U-sirkitree/R-0a530750-4176-464a-86c8-0cf0bf00c9d9

Tip: For ease of use, after installation, you can run the .bat file (I like having a shortcut on my desktop to it) and then utilize the tool tip in Neos.

[![video](https://img.youtube.com/vi/ORFDu8uGiIQ/0.jpg)](https://www.youtube.com/watch?v=ORFDu8uGiIQ)

## License
MIT

## Credits
- [OpenAI](https://openai.com/)
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
- [sirkitree](https://sirkitree.net/)

## Disclaimer
This is not an official OpenAI product.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

