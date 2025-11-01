import openai
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "lm-studio"

response = openai.ChatCompletion.create(
    model = "llama-3-8b-instruct",
    mesages= [{"role":"user","content":"Scrie un rezumat despre energie solara"}]
)
print(response.choices[0].message["content"])