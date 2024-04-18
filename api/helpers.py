import requests
from django.conf import settings


def call_openai_api(text, prompt_setup):
    """
    Sends requests to the OpenAI API for different tasks.
    Args:
        text (str): Text to be processed.
        prompt_setup (dict): Configuration including the prompt and model settings.

    Returns:
        str: Processed text from the API or an error message.
    """
    OPENAI_ENDPOINT = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.OPENAI_API_KEY}'  # Accessing API key securely
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": prompt_setup["system_message"]},
            {"role": "user", "content": text}
        ],
        "max_tokens": prompt_setup.get("max_tokens", 1500),
        "temperature": prompt_setup.get("temperature", 0.5),
        "top_p": 1,
        "frequency_penalty": prompt_setup.get("frequency_penalty", 0),
        "presence_penalty": prompt_setup.get("presence_penalty", 0)
    }

    response = requests.post(OPENAI_ENDPOINT, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("choices") and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"]
        else:
            return "No response from GPT-3"
    else:
        return f"Error calling GPT-3: {response.status_code}"
