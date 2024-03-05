
# Password Generator for Specific User Profiles

This program is designed to generate a list of passwords tailored to individuals with specific characteristics, utilizing OpenAI's GPT model. It is particularly useful for creating passwords that align with certain languages, political views, age ranges, and occupations.

## Features

- Dynamic password generation based on user-defined criteria.
- Support for multiple languages and specific user demographics.
- Outputs generated passwords to a text file for easy access and use.

## Requirements

- Python 3.x
- OpenAI Python Client
- An active OpenAI API key

## Setup

1. Ensure Python 3.x is installed on your system.
2. Install the OpenAI Python client using pip:
    ```
    pip install openai
    ```
3. Place your OpenAI API key in a `.env` file at the root of the project directory:
    ```
    OPENAI_API_KEY='your_api_key_here'
    ```

## Usage

1. Modify the `user_details` dictionary in the `main` function of the script to reflect the target user profile for which you wish to generate passwords.
2. Run the script:
    ```
    python password_generator.py
    ```
3. Find the generated passwords in the `password_ideas.txt` file in the project directory.

## Customization

You can customize the password generation criteria by editing the `user_details` dictionary in the `main` function to include specific languages, political views, age ranges, and occupations of your target audience.

## Note

This script is a demonstration of utilizing OpenAI's GPT for generating context-specific passwords and requires proper configuration and an active API subscription.


