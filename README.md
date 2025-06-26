🧠 Social Media Content Generator using Ollama + Mistral
A fast and private local Flask app that generates emotional, funny, sexy, or savage social media captions using the Mistral model via Ollama.

🚀 Features
Generate captions for any topic in 4 styles: emotional, funny, sexy, savage
Uses Mistral model through Ollama
Beautiful, mobile-responsive UI
Local-only: No internet or API key required
Copy-to-clipboard feature

### 🏠 Home Page

<img src="Screenshot%202025-06-26%20234933.png" width="600"/>

### ✍️ Output Page

<img src="Screenshot%202025-06-26%20235441.png" width="600"/>




🛠 Requirements
Python 3.7+
Ollama installed and running locally
Mistral model pulled via Ollama:
ollama pull mistral



📦 Installation Clone this repo: git clone https://github.com/VanshikaDubey1/llm-content-creater.git cd Social-Content-Generator-using-LLM cd llama-content-gen

Install Python dependencies: pip install -r requirements.txt

Make sure Ollama is running: ollama serve Run the Flask app: python app.py

Visit in browser: http://localhost:5000

structure 

llm-content-creater/
├── app.py
├── static/
├── templates/
├── requirements.txt
├── README.md
├── Screenshot 2025-06-26 234933.png
├── Screenshot 2025-06-26 235441.png





💡 Example Prompt Topic: Coffee Style: Savage 📝 Output:

"Without coffee, I’m basically a WiFi router with no signal."


⚡ Tips If it's slow: you're running on CPU. For faster results, use a GPU.

Try other models too: ollama pull llama2 ollama pull codellama

🧠 Powered By Flask Mistral Model Ollama

HTML + CSS (with Google Fonts)


🙌 Credits Built by Vanshika 🦋
