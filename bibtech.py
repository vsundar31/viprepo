import requests

while True:
    user_input = input("Enter your command (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    
    response = requests.post('http://127.0.0.1:5000/generate-response', json={'command': user_input})
    
    if response.status_code == 200:
        result = response.json()
        if 'response' in result:
            print("Generated Response:", result['response'])
        elif 'error' in result:
            print("Error:", result['error'])
    else:
        print("Failed to connect to the server.")