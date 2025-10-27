# helper_functions.py
from openai import OpenAI
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv('.env', override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
claude_api_key = os.getenv('ClAUDE_API_KEY')

# clientOpenAI = OpenAI(
#    # This is the default and can be omitted
#    api_key=openai_api_key
# )

clientClaude = Anthropic(
    api_key=claude_api_key
)


#def get_llm_response_gpt(prompt, model="gpt-3.5-turbo", max_tokens=150):
#    try:
#        response = clientOpenAI.responses.create(
#            model="gpt-3.5-turbo",
#            # instructions=prompt,
#            input=prompt
#        )
#        return response.output_text
#    except Exception as e:
#        return f"Error: {e}"


def get_llm_response_claude(messages):
    try:
        response = clientClaude.messages.create(
            model="claude-3-haiku-20240307",
            system="You name is Smarty and you are an useful assistant and respond at any question.",
            temperature=1.0,
            max_tokens=1000,
            messages=messages
        )
        return response.content[0].text
    except Exception as e:
        return f"Error: {e}"


def chat_with_claude():
    messages = []
    #prompt = input("Ask Smarty anything (or type 'exit' to quit):")
    messages.append({"role": "user", "content": 'Hi'})
    response = get_llm_response_claude(messages)
    messages.append({"role": "assistant", "content": response})
    print("Smarty:", response)
    print("-" * 40)  # separator for readability
    while True:
        prompt = input("You:")
        messages.append({"role": "user", "content": prompt})
        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        # Call your Claude function
        response = get_llm_response_claude(messages)
        messages.append({"role": "assistant", "content": response})
        print("Smarty:", response)
        print("-" * 40)  # separator for readability

