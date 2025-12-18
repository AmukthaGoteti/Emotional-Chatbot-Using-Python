# 🧠 Emotional Support Chatbot (Python)

A simple yet thoughtfully designed **rule-based Emotional Support Chatbot** built using Python.
This chatbot uses **regular expressions** and **randomized responses** to simulate empathetic, conversational interactions across emotional, motivational, and everyday topics.

It is ideal for beginners learning **Python**, **regex**, and **basic conversational AI logic**, while also demonstrating how software can be used to provide supportive human-like interactions.

## ✨ Features

* Responds to **greetings, farewells, and casual conversation**
* Detects and reacts to **emotional states** such as:

  * Sadness, anxiety, stress, loneliness, anger, fear
* Provides **motivation and encouragement**
* Covers common topics:

  * Career, interviews, studies, coding, AI, health, hobbies, travel, food, music
* Uses **randomized replies** to avoid repetitive responses
* Clean, readable, and easily extensible code structure

## 🛠️ Technologies Used

* **Python 3**
* `re` — for pattern matching using regular expressions
* `random` — for selecting varied responses

No external libraries are required.

## 📂 Project Structure

```text
├── chatbot.py        # Main chatbot implementation
└── README.md         # Project documentation
```

## 🚀 How It Works

1. User input is taken from the command line.
2. Input is converted to lowercase and matched against predefined **regex patterns**.
3. If a pattern matches, a **random response** from the corresponding list is returned.
4. If no pattern matches, a default supportive response is shown.
5. The conversation continues until the user types **bye** or **goodbye**.

## ▶️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/emotional-support-chatbot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd emotional-support-chatbot
   ```

3. Run the chatbot:

   ```bash
   python chatbot.py
   ```

## 💬 Sample Interaction

```text
You: I feel stressed
Chatbot: Burnout is a sign you’ve been pushing hard. Rest matters too.

You: I am studying for exams
Chatbot: Exams can be stressful. Preparation and calm thinking help a lot.

You: goodbye
Chatbot: Goodbye! Take care.
```

## 🎯 Learning Outcomes

By working with this project, you will:

* Understand **regex-based intent matching**
* Learn how rule-based chatbots function
* Improve Python control flow and string handling
* Design empathetic response logic
* Build a foundation for advanced NLP or AI chatbots

## 🔮 Possible Enhancements

* Add sentiment analysis using NLP libraries
* Store conversation history
* Convert to a GUI or web-based chatbot
* Integrate speech-to-text and text-to-speech
* Use machine learning for intent classification

## 🤝 Contribution

Contributions are welcome. Feel free to:

* Add new conversation patterns
* Improve response quality
* Refactor or optimize the logic
