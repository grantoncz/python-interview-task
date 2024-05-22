from flask import Flask, request, jsonify
import openai
from config import Config
from typing import List
import httpx

# ---------- Global Variables ----------

app = Flask(__name__)
app.config.from_object(Config)

openai.api_key = app.config['OPENAI_API_KEY']

API_KEY = app.config['OPENAI_API_KEY']

CATEGORIES = ["sports", "politics", "technology"]
GPT_Model = "gpt-4o"

# ---------- Functions ----------


def classify_text(text: str, categories: List[str]) -> str:
    """
    Find a single word from the string of possible catagories that describes the content of the text
    :param categories: List[str], contains the possible categories
    :param text: contains the text to classify
    :return: single word from the categories as the classification, or "unknown" if the Ai misbehaves.
    """
    # try to send data to AI to classify
    try:
        response = httpx.post('https://api.openai.com/v1/chat/completions',
                              headers={'Content-Type': 'application/json', 'Authorization': f"Bearer {API_KEY}"},
                              json={"model": GPT_Model, "messages": [
                                  {
                                      "role": "system",
                                      "content": "The user will supply some text and possible classifications of that "
                                                 "text. Respond with a single word  classification "
                                                 "from the list of possible classes. Only return a single word."
                                                 " Do not return anything more than a single word classification."
                                                 " For example:\nUSER:\nTEXT: "
                                                 "'Sailing is an activity loved by the brave, the bold and the insane.'"
                                                 " CLASSES = ['sport',  'leisure', 'technology']\n\n"
                                                 "RESPONSE:\nsport\n\nDo not respond with "
                                                 " 'It is sport' or anything that is not a single word from the list of"
                                                 " classes."
                                  },
                                  {
                                      "role": "user",
                                      "content": f"TEXT: {text}\nCLASSES: {str(categories)}"
                                  },
                              ]})

        # process response to get the single word category it returned
        response_json = response.json()
        category = response_json['choices'][0]['message']['content']

        # do some error checking to ensure it didn't misbehave.
        if category in CATEGORIES:
            return category
        else:
            return "unknown"

    # currently this only catches the error, but it is intended to be extended to log it.
    except Exception as e:
        print(f"Error classifying text: {e}")
        return "error"


# ---------- Routes ----------


@app.route('/classify', methods=['POST'])
def classify():
    """
    Route that takes in a json object with str text and list of classes
    :return: which of the classes the text can be classified as, or "unknown"
    """
    data = request.get_json()

    # extract the variables we want
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    if 'classes' not in data:
        return jsonify({'error': 'No classes provided'}), 400

    text = data['text']
    classes = data['classes']

    category = classify_text(text, classes)

    # ensure nothing went wrong and give feedback to the client
    if category == "error":
        return jsonify({'error': 'Internal server error'}), 500

    return jsonify({'category': category})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
