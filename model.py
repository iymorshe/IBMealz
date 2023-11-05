from dotenv import load_dotenv
import os
import openai


load_dotenv()
openai.api_key = os.getenv('API_KEY')

def generate_recipe(location):
    """
    This function takes a list of ingredients and generates a recipe using OpenAI's GPT-4 API.
    
    :param ingredients: A list of ingredient names as strings.
    :return: A string containing the generated recipe.
    """
    
    prompt = f"I live in {location}. Can you create a recipe for me?"

    try:
        # Call the OpenAI API
        response = openai.Completion.create(
            model="text-davinci-003",  # Use an appropriate model; "text-davinci-003" is an example
            prompt=prompt,
            max_tokens=150  # You can adjust the number of max_tokens as needed
        )
        # Extract the recipe from the response
        recipe = response.choices[0].text.strip()

        return recipe

    except openai.error.OpenAIError as e:
        # Handle API errors
        print(f"An error occurred: {e}")
        return None

# Example usage:
location = "Davis, CA"

recipe = generate_recipe("Davis, CA")
print(recipe)
