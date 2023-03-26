from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        genre = request.form['genre']
        prompt = request.form['prompt']
        max_length = int(request.form['max_length'])
        num_stories = int(request.form['num_stories'])
        if genre == 'action' or genre == 'adventure' or genre == 'comedy' or genre == 'fantasy':
            model_name = 'afshaan/AIstoryGenerator-v2'
        elif genre == 'horror':
            model_name = 'text-attack/gpt2-horror'
        else:
            return "Invalid genre entered. Please choose from action, adventure, comedy, or fantasy."

        generator = pipeline('text-generation', model=model_name)

        generated_text = generator(prompt, max_length=max_length, num_return_sequences=num_stories)

        stories = []
        for i, text in enumerate(generated_text):
            story = text['generated_text']
            stories.append(story)
        
        return render_template('story.html', stories=stories)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)