import os
import anthropic
import openai
import google.generativeai as genai

class ModelHandler:
    def __init__(self, model_endpoint, model_name, token_count=8000):
        self.model_endpoint = model_endpoint.lower()
        self.model_name = model_name
        self.token_count = token_count
        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API_KEY environment variable not set.")
    
    def call_model(self, prompt):
        if self.model_endpoint == "anthropic":
            return self._call_anthropic(prompt)
        elif self.model_endpoint == "openai":
            return self._call_openai(prompt)
        elif self.model_endpoint == "gemini":
            return self._call_gemini(prompt)
        else:
            raise ValueError(f"Unsupported model: {self.model_name}")
        
    def _call_anthropic(self, prompt):
        model_endpoint = anthropic.Anthropic(api_key=self.api_key)
        message = model_endpoint.messages.create(
            model=self.model_name,
            max_tokens=self.token_count,
            messages=[
                {"role": "user", "content":  prompt} 
            ]
        )
        return message.content[0].text

    def _call_openai(self, prompt):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            model=self.model_name,
            prompt=prompt,
            max_tokens=self.token_count
        )

        return response.choices[0].text.strip()

    def _call_gemini(self, prompt):
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(self.model_name)
        response = model.generate_content(prompt, max_tokens=self.token_count)
        return response.text