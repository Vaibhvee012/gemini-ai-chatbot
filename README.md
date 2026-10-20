# Ask Buddy – AI QnA Chatbot

An end-to-end Generative AI project that allows users to ask questions and receive AI-generated responses through an interactive chat interface. Built using Python, LangChain, Google Gemini, and Streamlit.

##  Project Overview

Ask Buddy is an LLM-powered chatbot that demonstrates how to integrate Google's Gemini model with LangChain and create a web-based conversational interface using Streamlit.

Users can enter questions, view AI-generated answers, and access previous messages during the current application session.

##  Features

- **AI-Powered QnA:** Generates answers using Google Gemini.
- **Interactive Chat Interface:** Simple conversational UI built with Streamlit.
- **Chat History:** Displays previous messages during the current session.
- **LangChain Integration:** Uses LangChain to invoke the Gemini model.
- **Secure Configuration:** Loads API credentials from environment variables.
- **Lightweight Application:** Simple setup with Python and a few dependencies.

##  Tech Stack

- **Programming Language:** Python
- **LLM:** Google Gemini
- **LLM Framework:** LangChain
- **Frontend:** Streamlit
- **Environment Variables:** python-dotenv

##  Project Structure

```text
apps/
├── 1_qna_bot.py    # Main chatbot application
├── .env            # Gemini API key (not committed)
├── .gitignore      # Excludes secrets and unnecessary files
└── README.md       # Project documentation
```

##  Getting Started

Follow these steps to install the dependencies and run Ask Buddy locally.

### Prerequisites

Make sure you have installed:

- Python 3.10 or later
- pip (Python package installer)
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the placeholders with your GitHub username and repository name.

### Step 2: Create a Virtual Environment

```bash
python -m venv env
```

Activate the environment on Windows:

```bash
env\Scripts\activate
```

On macOS or Linux:

```bash
source env/bin/activate
```

### Step 3: Install Required Packages

Run this command in your activated virtual environment:

```bash
python -m pip install streamlit langchain-google-genai python-dotenv
```

**Packages used:**

| Package | Purpose |
|---|---|
| `streamlit` | Creates the interactive web interface |
| `langchain-google-genai` | Integrates Google Gemini with LangChain |
| `python-dotenv` | Loads environment variables from the `.env` file |

### Step 4: Configure the Gemini API Key

Create a file named `.env` in the project directory, alongside `1_qna_bot.py`.

Add your API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Get your key from [Google AI Studio](https://aistudio.google.com/).

**Important:** Never share your API key or commit your `.env` file to GitHub.

### Step 5: Start the Project

From the directory containing `1_qna_bot.py`, run:

```bash
streamlit run 1_qna_bot.py
```

After the application starts, Streamlit will display a local URL. Open it in your browser:

```text
http://localhost:8501
```

You can now enter a question in the chat input and receive a response from Gemini.

### Step 6: Stop the Application

To stop the Streamlit server, press:

```text
Ctrl + C
```

##  How It Works

1. The user submits a question through the Streamlit chat input.
2. LangChain sends the question to the configured Google Gemini model.
3. Gemini generates a response.
4. The application displays the response in the chat interface.
5. Streamlit session state stores the conversation messages for display during the current session.

**Current limitation:** Previous messages are displayed, but the model receives only the latest question. Passing chat history to Gemini can be added to support contextual follow-up questions.

##  Future Enhancements

- Add conversational memory so the model can use previous messages as context.
- Implement streaming responses.
- Add a clear-chat button.
- Improve API error handling.
- Deploy the chatbot using Streamlit Community Cloud.

##  Learning Outcomes

- Integrating Google Gemini with LangChain.
- Invoking an LLM and handling its response.
- Building chat interfaces using Streamlit.
- Managing environment variables securely.
- Maintaining UI state with `st.session_state`.

##  Author

**Vaibhvee Prakash**

- GitHub: [Vaibhvee012](https://github.com/Vaibhvee012)
- LinkedIn: [Vaibhvee Prakash](https://www.linkedin.com/in/vaibhvee-prakash-901ba7289/)
- Portfolio: [Visit Portfolio](https://vaibhvee-portfolio.vercel.app/)

---

If you find this project useful, consider giving the repository a .
