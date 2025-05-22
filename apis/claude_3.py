import os
import json
import anthropic


class Claude3:
    def __init__(self):
        self.api_key = os.environ.get("CLAUDE_API_KEY")
        with open("apis/config.json") as f:
            self.config = json.load(f)["CLAUDE_MODELS"]

    def process_claude_model(self, model_name, temperature, system_prompt, refined_input, max_tokens):
        client = anthropic.Anthropic(api_key=self.api_key)

        response = client.messages.create(
            model=self.config[model_name]["name"],
            temperature=temperature,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": refined_input}]
        )

        return response.content[0].text