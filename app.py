# ************************************************************************
# Ashlin Darius Govindasamy - ADGSTUDIOS 2021
# All rights reserved.
# FoodRecipeGenerator
# ************************************************************************

# Import Modules
from flask import Flask, render_template, jsonify, request, abort
import openai
import ast
import os

# our supersecrets shhhhhhhhhhh
os.environ["OPENAI_API_KEY"] = "mysupersecret"

# App Config
app = Flask(__name__, template_folder='pages')

# Our Website Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route("/apps/foodapp/api/v1/generateinstructions", methods=["GET", "POST"])
def generateinstructions():
    if request.method == "POST":
        items = ast.literal_eval(request.data.decode("utf-8"))
        prompt = "Write a recipe based on these ingredients and instructions:\nIngredients:\n"
        ingredients = ''
        for item in items:
            ingredients += '\n'+item
        ingredients += '\nDirections'
        ingredients += prompt
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            engine="davinci-instruct-beta",
            prompt=ingredients,
            temperature=0,
            max_tokens=120,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        dictResponse = dict(response)
        words = dictResponse['choices'][0].text.split()
        output1 = " ".join(sorted(set(words), key=words.index)).replace(
            "Ingredients:", "").replace("  ", "\n")
        output2 = "Ingredients: "+output1
        return output2
    else:
        return jsonify({"message": "Please use POST method"})


# Initialization of applications and run
if __name__ == "__main__":
    app.run('localhost', debug=False)
