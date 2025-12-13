# Emotional Chatbot Using Python

In India, where mental health care can be expensive and limited, **emotional support chatbots** offer a practical, affordable, and accessible solution.  
This project demonstrates how a Python-based chatbot can use **regular expressions** to understand user input and provide empathetic, relevant responses — bridging the gap in mental health resources.

---

## 📚 About the Project
This chatbot is designed to:
- Engage users in supportive conversations.
- Provide predefined, empathetic responses based on detected input patterns.
- Allow users to start and end a conversation easily (type `goodbye` to exit).

By using **pattern matching** through Python’s `re` module, it analyses messages and responds in a way that feels personal and emotionally supportive.

---

## 🛠 Features
- 💬 **Text-based interaction** — Simply type and chat in the terminal.
- 🧠 **Pattern recognition** — Matches user input to emotional triggers using regex.
- ❤️ **Empathetic responses** — Tailored to provide emotional comfort.
- 🚪 **Easy exit** — End the conversation by typing `goodbye`.

---

## 📦 Requirements
- Python 3.x  
- No external libraries required (uses built-in Python modules).

---

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Emotional-Chatbot-Using-Python.git
````

### 2. Navigate to the project folder

```bash
cd Emotional-Chatbot-Using-Python
```

### 3. Run the chatbot

```bash
python chatbot.py
```

### 4. Start chatting

Type your messages, and receive supportive replies.
To exit, simply type:

```text
goodbye
```

---

## 🗂 How It Works

1. The chatbot uses **regular expressions** to detect keywords or patterns in user messages.
2. Each pattern has a **predefined response** stored in a dictionary or list.
3. When a match is found, the chatbot replies with the corresponding supportive message.
4. If no match is found, it gives a default empathetic response.

---

## 🔗 Applications

* Mental health awareness campaigns.
* Emotional first-aid for individuals without access to therapy.
* Educational tools for demonstrating chatbot logic.

---

## 📌 Example Interaction

```
You: I feel lonely
Bot: I’m sorry you’re feeling this way. Remember, you’re not alone — I’m here to listen.

You: goodbye
Bot: Take care of yourself. Remember, you matter.
```

---

## 🤝 Contributing

Contributions are welcome! You can:

* Add new emotional patterns and responses.
* Improve regex matching for better accuracy.
* Enhance the conversation flow.

---

## 💡 Acknowledgements

* Inspired by the need for affordable mental health solutions in India.
* Uses Python's `re` module for pattern-based chatbot interactions.
