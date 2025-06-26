from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def generate_content(prompt, style):
    full_prompt = f"You are a creative social media expert. Write a {style} post about: {prompt}"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",     # Make sure this model is installed: ollama pull mistral
            "prompt": full_prompt,
            "stream": False         # Get the whole output instantly
        }
    )
    return response.json().get("response", "No response.")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        topic = request.form['topic']
        style = request.form['style']
        result = generate_content(topic, style)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

