from dotenv import load_dotenv
import os
from openai import OpenAI
from openai.types import Completion, CompletionChoice, CompletionUsage

load_dotenv()
# Initialize OpenAI client with API key from .env file

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),)

def generate_password_ideas(prompt, num_passwords=1):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",  # Use an appropriate model
            max_tokens=1000,  # Adjust based on needs
            n=num_passwords,  
        )

        
        message_content = chat_completion.choices[0].message.content
        return message_content.strip().split('\n')
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    # Dynamic prompt structure
    prompt_template = """
    You are a password generator. Generate a list of passwords suitable for a person with the following characteristics:
    - Languages: {languages}
    - Political views: {political_views}
    - Age: {age_range}
    - Occupation: {occupation}
    Output only the passwords, nothing else don't number them. Use special characters and numbers, and be the best password generator you can be.
    Make up to 500 passwords. """
    
    # Example user inputs; these can be dynamically changed based on actual user input
    user_details = {
        "languages": "Germ",
        "political_views": "--",
        "age_range": "between 18-30",
        "occupation": "--",
    }
    
    # Fill the prompt template with the user's details
    prompt = prompt_template.format(**user_details)

    num_passwords = 1# Number of passwords to generate

    password_ideas = generate_password_ideas(prompt, num_passwords)

    # Write the generated passwords to a file
    with open('password_ideas.txt', 'a') as f:
        for idea in password_ideas:
            f.write(f"{idea}\n")

    print("Password ideas generated and written to password_ideas.txt")

if __name__ == "__main__":
    main()
