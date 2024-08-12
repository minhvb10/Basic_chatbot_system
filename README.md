# Basic Chatbot System

This is a basic chatbot implemented in Python that can interact with users through predefined responses. It's a simple example to demonstrate how a chatbot can handle basic user inputs and provide corresponding replies.

## Features

- **Predefined Responses**: The chatbot can respond to a set of predefined inputs.
- **Case Insensitive Matching**: User inputs are matched against responses in a case-insensitive manner.
- **Exit Command**: The chatbot can be exited by typing `"quit"`.

## Requirements

- Python 3.x


## Usage

1. **Run the Chatbot Script**:  
   Execute the Python script to start the chatbot.

   ```bash
   python chatbot.py
   ```

2. **Interact with the Chatbot**:  
   Type a message to the chatbot and receive a predefined response. For example:
   
   - Typing `"hi"` will result in: `Hello!`
   - Typing `"what is your name"` will result in: `I'm just a chatbot`
   - Typing `"quit"` will exit the chatbot with: `Goodbye, see you later`

3. **Exit the Chatbot**:  
   Type `"quit"` to end the chatbot session.

## Example

Here’s an example interaction with the chatbot:

```
Hi! I'm your chatbot. Type 'quit' to exit.
> hello
Hi there!
> how are you
I'm good
> thanks
No problem
> quit
Goodbye, see you later
```

## Code Explanation

- **Dictionary of Responses**: `responses` contains a mapping of user inputs to the chatbot's responses.
- **Chatbot Function**: The `chatbot()` function handles the user input, matches it with the dictionary, and prints the appropriate response.
- **Exit Condition**: The chatbot continues to run until the user types `"quit"`, which exits the program.


---
