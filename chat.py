from google import genai

client = genai.Client(api_key="AIzaSyCsOe_DpgLW1O7Y9_y7ptXjZw7gk5CL_X8")

user_prompt = input("Prompt: ")
system_prompt = "Limit your answer to one sentence. Pretend you are a cat"
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_prompt + "\n\n" + system_prompt

)

print(response.text)

