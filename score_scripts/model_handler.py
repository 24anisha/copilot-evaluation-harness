import os
import anthropic
import openai
import google.generativeai as genai
from openai import AzureOpenAI

class ModelHandler:
    def __init__(self, model_endpoint, model_name, deployment_name, token_count=8000):
        self.model_endpoint = model_endpoint.lower()
        self.model_name = model_name
        self.deployment_name = deployment_name
        self.token_count = token_count
        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API_KEY environment variable not set.")
        
        if self.model_endpoint == "anthropic":
            return self._init_anthropic()
        elif self.model_endpoint == "openai":
            return self._init_openai()
        elif self.model_endpoint == "gemini":
            return self._init_gemini()
        elif self.model_endpoint == "azure":
            return self._init_azure()
        else:
            raise ValueError(f"Unsupported model: {self.model_name}")
    
    def _init_anthropic(self):
        self.model = anthropic.Anthropic(api_key=self.api_key)
    
    def _init_openai(self):
        openai.api_key = self.api_key
    
    def _init_gemini(self):
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)
    
    def _init_azure(self):
        self.model = AzureOpenAI(api_version="2024-12-01-preview", azure_endpoint=self.model_name, api_key=self.api_key)
    
    def call_model(self, prompt):
        if self.model_endpoint == "anthropic":
            return self._call_anthropic(prompt)
        elif self.model_endpoint == "openai":
            return self._call_openai(prompt)
        elif self.model_endpoint == "gemini":
            return self._call_gemini(prompt)
        elif self.model_endpoint == "azure":
            return self._call_azure(prompt)
        else:
            raise ValueError(f"Unsupported model: {self.model_name}")
        
    def _call_anthropic(self, prompt):
        message = self.model.messages.create(
            model=self.model_name,
            max_tokens=self.token_count,
            messages=[
                {"role": "user", "content":  prompt} 
            ]
        )
        return message.content[0].text

    def _call_openai(self, prompt):
        response = openai.Completion.create(
            model=self.model_name,
            prompt=prompt,
            max_tokens=self.token_count
        )

        return response.choices[0].text.strip()

    def _call_gemini(self, prompt):
        response = self.model.generate_content(prompt, max_tokens=self.token_count)
        return response.text
    
    def _call_azure(self, prompt):
        response = self.model.chat.completions.create(messages=[{"role": "user", "content": prompt}], model=self.deployment_name, max_completion_tokens=self.token_count)
        return response.choices[0].message.content