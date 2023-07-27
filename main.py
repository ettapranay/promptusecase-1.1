import requests

# Function to prompt the user for input
def prompt(question):
    return input(question)

# Function to write content to a file
def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Function to read content from a file
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Function to send data to OpenAI API
def send_to_openai(input_data):
    api_key = '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' # Replace with your OpenAI API key
    api_url = 'https://api.openai.com/v1/engines/text-davinci-002/completions' # Or any other API endpoint you want to use

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        'prompt': input_data,
        'max_tokens': 150 # Adjust as needed
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.ok:
        return response.json()['choices'][0]['text']
    else:
        print('Error while sending data to OpenAI:', response.text)
        return ''

# Main function to run the script
def main():
    user_input = prompt('Enter your input: ')

    # Write user input to input.txt file
    write_file('input.txt', user_input)

    # Read the input from input.txt file
    input_from_file = read_file('input.txt')

    # Process the input (You can perform any processing you need here)

    # Send the processed input to OpenAI API
    output = send_to_openai(input_from_file)

    # Write the output to output.txt file
    write_file('output.txt', output)

    print('Processing complete! Check output.txt for the result.')

# Call the main function to start the process
if __name__ == "__main__":
    main()
