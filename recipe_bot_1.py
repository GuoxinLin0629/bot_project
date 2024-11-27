from openai import AzureOpenAI
import os
import requests
import json

client = AzureOpenAI(
	api_key = os.getenv("AZURE_KEY"),
	azure_endpoint = os.getenv("AZURE_ENDPOINT"),
	api_version = "2023-10-01-preview"
)

def load_api_key():
    with open("spoonacularAPI_Key.txt", 'r') as file:
        return file.read()

def get_recipe(ingredients):
    api_key = load_api_key()
    response = requests.get(
        "https://api.spoonacular.com/recipes/findByIngredients",
        params={"ingredients": ingredients, "number": 3, "apiKey": api_key}
    )
    if response.status_code == 200:
        return [
            f"Recipe: {recipe['title']} | URL: https://spoonacular.com/recipes/{recipe['id']}"
            for recipe in response.json()
        ]
def get_recipe_by_ingredients(ingredients):
    api_key = load_api_key()
    response = requests.get(
        "https://api.spoonacular.com/recipes/findByIngredients",
        params={"ingredients": ingredients, "number": 3, "apiKey": api_key}
    )
    if response.status_code == 200:
        return [
            f"Recipe: {recipe['title']} | URL: https://spoonacular.com/recipes/{recipe['id']}"
            for recipe in response.json()
        ]
    else:
        return [f"Error fetching recipes: {response.status_code} - {response.text}"]

functions = [
    {
        "type": "function",
        "function": {
            "name": "get_recipe",
            "description": "Gets recipes based on cuisine or ingredients",
            "parameters": {
                "type": "object",
                "properties": {
                    "cuisine": {
                        "type": "string",
                        "description": "The type of cuisine, e.g., Italian, Spanish, Mexican",
                        "nullable": True
                    },
                    "ingredients": {
                        "type": "string",
                        "description": "Comma-separated list of ingredients",
                        "nullable": True
                    }
                },
                "required": [], 
            }
        }
    }
]

messages = [
    {"role": "system", "content": "You are a recipe bot that helps users find recipes based on their requests."},
    {"role": "user", "content": "I want a Spanish recipe,Find me a recipe with apple and beef."}
]
response = client.chat.completions.create(model="GPT-4", messages=messages)
tool_calls = response.choices[0].message.tool_calls

if tool_calls:
    ingredients = json.loads(tool_calls[0].function.arguments).get('ingredients', '')
    recipes = get_recipe(ingredients)
    print("\n".join(recipes))
else:
    print(response.choices[0].message.content)