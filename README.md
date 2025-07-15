# 💬 LangChain Chatbot using OpenAI (Paid) and Ollama (Gemma - Free)

This project is a dual chatbot implementation built using **LangChain** and **Streamlit**. It supports both:

- 🔹 **ChatGPT via OpenAI API (Paid)**
- 🔹 **Gemma 2B via Ollama (Free and offline)**

---Add your keys to .env:

LANGCHAIN_API_KEY=your_key
OPENAI_API_KEY=your_key
LANGCHAIN_PROJECT=your_project

▶️ Run
**For OpenAI version**
streamlit run chatgpt_chatbot.py

**For Ollama version**
ollama pull gemma:2b
streamlit run gemma_chatbot.py

**📁 Files**

chatgpt_chatbot.py – uses OpenAI
gemma_chatbot.py – uses Ollama
.env – store your keys
requirements.txt

## 📦 Tech Stack

- [LangChain Core](https://python.langchain.com/)
- [LangChain OpenAI](https://python.langchain.com/docs/integrations/llms/openai/)
- [LangChain Community](https://docs.langchain.com/)
- [Streamlit](https://streamlit.io/) – for building the user interface
- [Ollama](https://ollama.com/) – for running local LLMs
- [python-dotenv](https://pypi.org/project/python-dotenv/) – for loading environment variables

---

