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

