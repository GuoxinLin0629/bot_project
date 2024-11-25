# **Recipe Bot**

## **Overview**

Recipe Bot is a Python-based application that integrates with OpenAI's GPT model and the Spoonacular API to help users find recipes. Users can specify their preferences, such as a cuisine type or ingredients, and the bot will return relevant recipes.

- **Dish Name**
- **Ingredients**
- **Instructions**

------

## **Features**

- Fetch recipes by **cuisine type** (e.g., Spanish, Italian, Mexican).
- Fetch recipes by **ingredients** (e.g., apple, beef).
- Combine filters for more specific results (e.g., Spanish cuisine with beef).
- Intuitive and dynamic responses powered by GPT-4.

------

## **Requirements**

- Python 3.8 or higher
- Azure OpenAI API credentials
- Spoonacular API Key

------

## **Installation**

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   vituralenv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install requests openai
   ```

4. **Set up API keys:**

   - Create a file named `spoonacularAPI_Key.txt` in the project folder and paste your Spoonacular API key inside.

   - Set your Azure OpenAI credentials as environment variables:

     ```bash
     set AZURE_KEY="your_azure_api_key"
     set AZURE_ENDPOINT="your_azure_endpoint"
     ```

------

## **Usage**

1. Run the bot:

   ```bash
   python recipe_bot_1.py
   ```

2. Follow the instructions:

   - Input ingredients separated by commas (e.g., `apple, beef`).
   - The bot will use Azure OpenAI to process your input and fetch recipes via the Spoonacular API.

------

## **Example Output**

**Input:**

```text
Give me a Spanish recipe with beef and apple.
```

**Output:**

```text
Sure, one popular Spanish dish that combines both apples and beef is "Beef Estofado With Apples". Here is a simple recipe for you:

Ingredients:

1) 2 lbs of stewing beef, cut into chunks
2) 2 large apples, peeled and chopped
...

Instructions:

1) Heat the olive oil in a large pot over medium heat. Add the beef chunks, season with salt, pepper, and paprika, and cook until they are browned on all sides (around 6-7 minutes).

...

Note: For additional flavor, you can add a splash of cider vinegar or a hand full of green olives to the pot before simmering. Enjoy your meal!
```

------

## **Code Structure**

- **Azure OpenAI Integration:** Processes natural language inputs to determine the required tool or function.

- **Spoonacular API Integration:** Fetches recipes, ingredients, and instructions based on the user input.

- Functionality Flow:

  ```text
  User Input → Azure OpenAI Model → Tool Call → Spoonacular API → Recipe Output
  ```

------

## **API Documentation**

- **Azure OpenAI:**
   [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)
- **Spoonacular API:**
   [Spoonacular API Documentation](https://spoonacular.com/food-api)

------

## **Future Improvements**

- Add dietary preference filtering (e.g., vegetarian, gluten-free).
- Allow users to input specific serving sizes or preferred cuisines.
- Provide nutritional information for each recipe.
- Enhance the bot with more advanced multi-step interactions.

------

## **Troubleshooting**

1. **Spoonacular API Key Issues:**

   - Ensure `spoonacularAPI_Key.txt` contains a valid API key.
   - Verify the file is in the same directory as the script.

2. **Azure OpenAI Errors:**

   - Check that the Azure API key and endpoint are correctly set as environment variables.
   - Ensure your Azure OpenAI subscription includes access to the GPT-4 model.

3. **Missing Dependencies:**

   - Run the following command to install missing libraries:

     ```bash
     pip install requests openai
     ```

4. **No Recipes Found:**

   - Check the format of your input ingredients (comma-separated).
   - Verify the Spoonacular API key has not exceeded its rate limit.

------

## **Acknowledgments**

- **Spoonacular API:** For providing access to a vast database of recipes.
- **Azure OpenAI:** For enabling natural language processing capabilities to enhance user interactions.

------

## **License**

This project is licensed under the MIT License. See the LICENSE file for more details.

