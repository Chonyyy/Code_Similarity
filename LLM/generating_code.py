import os
import openai

# Configure your OpenAI API key
openai.api_key = 'your-api-key'

def get_description(code):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Please describe the following C# code in detail:\n{code}",
        max_tokens=150
    )
    description = response.choices[0].text.strip()
    return description

def generate_code(description):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Please generate C# code based on the following description:\n{description}",
        max_tokens=150
    )
    new_code = response.choices[0].text.strip()
    return new_code

def process_files(root, new_root):
    for folder, _, files in os.walk(root):
        for file in files:
            if file.endswith('.cs'):
                original_path = os.path.join(folder, file)
                
                # Read the content of the original file
                with open(original_path, 'r') as f:
                    code = f.read()
                
                # Get description and generate new code
                description = get_description(code)
                new_code = generate_code(description)
                
                # Create the new path to save the generated file
                relative_path = os.path.relpath(folder, root)
                new_folder = os.path.join(new_root, relative_path)
                os.makedirs(new_folder, exist_ok=True)
                new_path = os.path.join(new_folder, file)
                
                # Save the new code in the new location
                with open(new_path, 'w') as file:
                    file.write(new_code)
                print(f"Processed: {original_path} -> {new_path}")

# Set the paths of the folders
root = f'{os.getcwd()}\\Projects\\All\\'
new_root = f'{os.getcwd()}\\Projects\\Copy\\' 

# Process the C# files
process_files(root, new_root)
