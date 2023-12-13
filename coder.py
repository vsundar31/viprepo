from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

api_key = "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"

openai.api_key = api_key

@app.route('/generate-response', methods=['POST'])
def generate_response():
    data = request.get_json()
    if 'command' not in data:
        return jsonify({'error': 'Command not found'})
    user_command = data['command']
    additional_paragraph = "\nI have a robot with limited commands: \n1) moveF(number of meters\n2) moveB(number of meters)\n3) turnL(number of degrees)\n4) turnR(number of degrees)\n5) pickUp()\n6) drop()\n7) emergencyStop() 8) arucoNav(tagNumber)\nTranslate the following prompt into Python-like pseudocode using ONLY the mentioned commands and NO DEFINITIONS. arucoNav follows the guidelines mentioned in the arucotag with the number. If any distance is not explicitly mentioned, request clarification. Do not make a random distance. In case of 'EMERGENCY STOP' by the user, halt all commands and return only the word 'EMERGENCY.' Use pickUp() and drop() commands only if explicitly instructed. Return only pseudocode and NO comments. Return code as text and not a code box"


   
    user_command_with_additional_text = additional_paragraph + user_command
    
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages = [{"role": "user", "content": user_command_with_additional_text}],
            max_tokens=3000,
        )
        generated_text = response['choices'][0]['message']['content']
        return jsonify({'response' : generated_text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


