# Ask Buddy – AI QnA Chatbot

An end-to-end Generative AI project that lets users ask questions and receive AI-generated responses through an interactive chat interface. Built using Python, LangChain, Google Gemini, and Streamlit.

## Overview

Ask Buddy is a simple Large Language Model (LLM) powered chatbot designed to demonstrate how to integrate Google's Gemini models with LangChain and build an interactive web application using Streamlit.

Users can enter questions, view AI-generated answers, and continue conversations through a clean chat interface. The application maintains chat history during the current Streamlit session.

## Features

- **AI-Powered QnA:** Generates responses using Google's Gemini model.
- **Interactive Chat Interface:** Provides a conversational UI using Streamlit.
- **Chat History:** Displays previous user messages and AI responses during the session.
- **LangChain Integration:** Uses LangChain's Google Generative AI integration to invoke the LLM.
- **Environment Variable Management:** Loads API credentials from a `.env` file.
- **Simple and Lightweight:** Easy to set up and extend with additional GenAI features.

## Tech Stack

- **Language:** Python
- **LLM:** Google Gemini
- **LLM Framework:** LangChain
- **Frontend:** Streamlit
- **Environment Management:** python-dotenv

## Project Structure

```text
apps/
├── 1_qna_bot.py       # Main Streamlit chatbot application
├── .env               # API credentials (not committed)
├── .gitignore         # Excludes secrets and unnecessary files
└── README.md          # Project documentation
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Y