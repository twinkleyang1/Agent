#### main.py
# from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.deepseek import DeepSeekProvider
from pydantic_ai.settings import ModelSettings
from pydantic_ai import Agent

from dotenv import load_dotenv
import tools
import os
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "https://127.0.0.1:7890"

load_dotenv()

# model = GeminiModel("gemini-2.5-flash-preview-04-17")
# model = GeminiModel("gemini-2.0-flash")
model = OpenAIModel(
    'deepseek-chat',
    provider=DeepSeekProvider(api_key=''),
)

agent = Agent(model,
              model_settings=ModelSettings(timeout=300),
              system_prompt="You are an experienced programmer",
              tools=[tools.read_file, tools.list_files, tools.rename_file])

def main():
    history = []
    while True:
        user_input = input("Input: ")
        resp = agent.run_sync(user_input,
                              message_history=history)
        history = list(resp.all_messages())
        print(resp.output)


if __name__ == "__main__":
    main()
