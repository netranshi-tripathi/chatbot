# 💬 LangChain Chatbot using OpenAI (Paid) and Ollama (Gemma - Free)

This project is a dual chatbot implementation built using **LangChain** and **Streamlit**. It supports both:

- 🔹 **ChatGPT via OpenAI API (Paid)**
- 🔹 **Gemma 2B via Ollama (Free and offline)**


**🔑 Add your keys to .env:**

LANGCHAIN_API_KEY=your_key<br>
OPENAI_API_KEY=your_key<br>
LANGCHAIN_PROJECT=your_project<br>


**▶️ Run**
**For OpenAI version**<br>
streamlit run chatgpt_chatbot.py<br>

**For Ollama version**<br>
ollama pull gemma:2b<br>
streamlit run gemma_chatbot.py<br>


**📁 Files**

chatgpt_chatbot.py – uses OpenAI<br
gemma_chatbot.py – uses Ollama<br>
.env – store your keys<br>
requirements.txt<br>

## 📦 Tech Stack

- [LangChain Core](https://python.langchain.com/)
- [LangChain OpenAI](https://python.langchain.com/docs/integrations/llms/openai/)
- [LangChain Community](https://docs.langchain.com/)
- [Streamlit](https://streamlit.io/) – for building the user interface
- [Ollama](https://ollama.com/) – for running local LLMs
- [python-dotenv](https://pypi.org/project/python-dotenv/) – for loading environment variables



