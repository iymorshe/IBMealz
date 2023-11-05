from dotenv import load_dotenv
import os
import openai

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


load_dotenv()
openai.api_key = os.getenv('API_KEY')

def generate_recipe(location, cuisine):
    """
    This function generates a list of 21 meals for a given location and cuisine using OpenAI's GPT-4 API and returns them as a pandas DataFrame.
    
    :param location: A string specifying the location.
    :param cuisine: A string specifying the preferred cuisine.
    :return: A pandas DataFrame containing the generated recipes.
    """

    prompt = f"I am a college student in {location} who prefers {cuisine} cuisine. Generate a list of 21 meals, keeping the location in mind. Along with the meal name, list the type of the meal."

    try:
        # Call the OpenAI API
        response = openai.Completion.create(
            model="text-davinci-003",  # Use an appropriate model; adjust accordingly if GPT-4 or newer models are available
            prompt=prompt,
            max_tokens=300  # You can adjust the number of max_tokens as needed
        )

        # Extract the recipe text from the response
        recipe_text = response.choices[0].text.strip()

        # Split the response into individual meals (assuming that each meal is separated by a newline)
        meals = recipe_text.split('\n')

        # Filter out any empty lines
        meals = [meal for meal in meals if meal]

        # Create a pandas DataFrame
        df = pd.DataFrame(meals, columns=['title'])

        return df

    except openai.error.OpenAIError as e:
        # Handle API errors
        print(f"An error occurred: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error

# Example usage:
# location = "Davis, CA"
# cuisine = "Meditterranean"
# recipe = generate_recipe(location, cuisine)
# print(recipe)


# Load and preprocess data
def preprocess_data(csv_file_path):
    # Read the CSV file containing the meals
    df = pd.read_csv(csv_file_path)
    # Normalize the meal names (e.g., lowercase)
    df['title'] = df['title'].str.lower().str.replace('[^\w\s]', '', regex=True)
    return df

# Train model (In this case, we will use TF-IDF to transform the meal names)
def train_model(meals):
    # Initialize the vectorizer
    vectorizer = TfidfVectorizer()
    # Fit the vectorizer to the meals
    tfidf_matrix = vectorizer.fit_transform(meals['title'])
    return vectorizer, tfidf_matrix

# Ranking function
def rank_meals(user_preferences, vectorizer, tfidf_matrix, meals):
    # Transform user preferences using the same vectorizer
    user_pref_vector = vectorizer.transform([' '.join(user_preferences)])
    # Calculate the cosine similarity between user preferences and all meals
    cosine_similarities = cosine_similarity(user_pref_vector, tfidf_matrix)
    # Get similarity scores for all meals
    similarity_scores = list(enumerate(cosine_similarities[0]))
    # Sort the meals based on the similarity scores
    sorted_meals = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    # Get the ranked meal names
    ranked_meals = [(meals.iloc[i]['title'], score) for i, score in sorted_meals]
    return ranked_meals

# Main function to use
def main(user_input_preferences, csv_file_path, recipes):
    # Load and preprocess the data
    # meals = preprocess_data(csv_file_path)
    # return meals

    meals = recipes

    # Train the model
    vectorizer, tfidf_matrix = train_model(meals)
    # Rank the meals based on user preferences
    ranked_meal_list = rank_meals(user_input_preferences, vectorizer, tfidf_matrix, meals)
    return ranked_meal_list

# Example usage
if __name__ == "__main__":
    location = "Davis, CA"
    cuisine = "Meditterranean"
    recipe = generate_recipe(location, cuisine)

    user_preferences = ["salad", "soup"]
    csv_file_path = 'archive/epi_r.csv'  # replace with your actual CSV file path
    ranked_meals = main(user_preferences, csv_file_path, recipe)
    # print(ranked_meals['title'])
    for meal, score in ranked_meals:
        print(f"Meal: {meal}, Score: {score}")
