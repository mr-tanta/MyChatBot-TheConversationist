# MyChatBot-TheConversationist

## Intelligent Chatbot

### Update

In this code, I have set up the chatbot using ChatterBot and trained it using the Cornell Movie
Dialogs Corpus. To make the chatbot more sophisticated and intelligent, I have integrated it with the OpenAI API, which
generates more complex and human-like responses. Additionally, I have included a sentiment analysis feature that
evaluates the user's message and prompts them for feedback on each response. This feedback is used to further train and
improve the chatbot's performance. Finally, the code includes a loop that enables the chatbot to continue interacting
with the user until the program is terminated.

### Installation

To run this project, you will need to install the following Python libraries:

- ChatterBot
- TextBlob
- OpenAI

#### You can install these libraries using pip:

- `pip install chatterbot textblob openai`

#### You will also need to set up an OpenAI API key in order to use the OpenAI GPT-3 API. You can sign up for an API key on the OpenAI website.

### Usage

To start the chatbot, run the following command:

`python chatbot.py`

The chatbot will prompt you for a user ID and a message. After each message, the chatbot will generate a response and
prompt the user for feedback on the response. The feedback is used to improve the chatbot's training.

### Configuration

The chatbot can be configured by modifying the `chatbot.py` script. You can change the training data by modifying the
`trainer.train()` function call. You can also change the OpenAI API key and parameters by modifying the openai.api_key and
`openai.Completion.create()` function calls, respectively.

## Contributing

If you would like to contribute to this project, please open a pull request on GitHub. All contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more information.