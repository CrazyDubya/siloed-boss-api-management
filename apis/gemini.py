import os
import json
import google.generativeai as genai

class GeminiModel:
    def __init__(self):
        self.api_key = os.environ.get("GOOGLE_API_KEY")
        with open("apis/config.json") as f:
            self.config = json.load(f)["GEMINI_MODELS"]

        genai.configure(api_key=self.api_key)

    def process_gemini_model(self, model_name, prompt, temperature, max_tokens):
        model = genai.GenerativeModel(self.config[model_name]["name"])

        generation_config = genai.types.GenerationConfig(
            candidate_count=1,
            max_output_tokens=max_tokens,
            temperature=temperature
        )

        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )

        return response.text