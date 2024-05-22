from flask import Flask, request, jsonify
import openai
from config import Config
from typing import List
import httpx
import ast
import json


app = Flask(__name__)
app.config.from_object(Config)

openai.api_key = app.config['OPENAI_API_KEY']

API_KEY = app.config['OPENAI_API_KEY']

CATEGORIES = ["sports", "politics", "technology"]
GPT_Model = "gpt-4o"


def classify_text(text: str, categories: List):
    """
    Classify
    :param categories:
    :param text:
    :return:
    """
    try:
        # response = openai.Completion.create(
        #     engine="davinci",
        #     prompt=f"Classify the following text into one of these categories: {', '.join(categories)}.\n\nText: {text}\n\nCategory:",
        #     max_tokens=1,
        #     temperature=0
        # )
        # response = openai.completions.create(
        #     model=GPT_Model,
        #     response_format={"type": "json_object"},
        #     prompt=[
        #         {
        #             "role": "system",
        #             "content": "You are a text classifier. You will summarise the topic of the text passed in a single word. The single word used to summarise the text must come from the the user's list of classes."
        #         }
        #     ]
        # )

        response = httpx.post('https://api.openai.com/v1/chat/completions',
                              headers={'Content-Type': 'application/json', 'Authorization': f"Bearer {API_KEY}"},
                              json={"model": GPT_Model, "messages": [
                                  {
                                      "role": "system",
                                      "content": "The user will supply some text and possible classifications of that "
                                                 "text. Respond with a JSON object containing a single classification "
                                                 "from the list of possible classes. Do not specify that it is json, or"
                                                 " For example:\nUSER:\nTEXT: "
                                                 "'Sailing is an activity loved by the brave, the bold and the insane.'"
                                                 " CLASSES = ['sport',  'leisure', 'technology']\n\n"
                                                 "RESPONSE:\n{'class': 'sport'}. \n\nDo not respond with "
                                                 "```json{'class': 'technology'}```"
                                                 " or anything that is not pure, valid json."
                                  },
                                  {
                                      "role": "user",
                                      "content": f"TEXT: {text}\nCLASSES: {str(categories)}"
                                  },
                              ]})

        print(response.text)
        print(response)

        # category = response.choices[0].text.strip()
        response_json = response.json()
        # print(response_json['choices'][0]['message']['content'])
        category_string = response_json['choices'][0]['message']['content']

        # try:
        category = ast.literal_eval(category_string)
        # except:
        #     return "unknown"

        print("Category:", category)
        if category in CATEGORIES:
            return category
        else:
            return "unknown"
    except Exception as e:
        print(f"Error classifying text: {e}")
        return "error"


@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    if 'classes' not in data:
        return jsonify({'error': 'No classes provided'}), 400

    text = data['text']
    classes = data['classes']
    category = classify_text(text, classes)

    if category == "error":
        return jsonify({'error': 'Internal server error'}), 500

    return jsonify({'category': category})


if __name__ == '__main__':
    app.run(debug=True)
