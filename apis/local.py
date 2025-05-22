import json
from openai import OpenAI


class LocalModel:
    def __init__(self):
        with open("apis/config.json") as f:
            self.config = json.load(f)["LOCAL_MODELS"]

    def process_local_model(self, model_name, messages, temperature, max_tokens):
        base_url = f"http://localhost:{self.config[model_name]['port']}/v1"
        client = OpenAI(api_key="NONE", base_url=base_url)

        response = client.chat.completions.create(
            model=self.config[model_name]["name"],
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
