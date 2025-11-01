import ollama

def chat_local(prompt):
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    return response['message']['content']
while True:
    user_input = input("You: ")
    if user_input.lower() in ["pa" ,"exit", "quit"]:
        break
    print("Ai:", chat_local(user_input))