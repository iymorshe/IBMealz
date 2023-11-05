from dotenv import load_dotenv
import os
import openai


load_dotenv()
openai.api_key = os.getenv('API_KEY')

def generate_recipe(location, cuisine):
    """
    This function takes a list of ingredients and generates a recipe using OpenAI's GPT-4 API.
    
    :param ingredients: A list of ingredient names as strings.
    :return: A string containing the generated recipe.
    """
    
    prompt = f"I am a college student in {location} who prefers {cuisine} cuisine. Generate a list of 21 recipes that I can follow, keeping the location in mind."

    try:
        # Call the OpenAI API
        response = openai.Completion.create(
            model="text-davinci-003",  # Use an appropriate model; "text-davinci-003" is an example
            prompt=prompt,
            max_tokens=300  # You can adjust the number of max_tokens as needed
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
cuisine = "Meditterranean"
recipe = generate_recipe(location, cuisine)
print(recipe)
