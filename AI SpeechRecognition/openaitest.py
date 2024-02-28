import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an application to my cc for leave?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\n\nSubject: Leave\n\nDear [Name],\n\nI am writing to inform you of my intention to leave from college at [College name]. My last day in college will be [date].\n\nI have enjoyed my time at [college], and I am grateful for the studying here. I have learned so many skills during my time in the college, and I am grateful for the support.\n\nIf you need any query, please do not hesitate to ask.\n\nThank you for your understanding.\n\nSincerely,\n[Your Name]"
    }
  ],
  "created": 1683815400,
  "id": "cmpl-7F1aqg7BkzIY8vBnCxYQh8Xp4wO85",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 125,
    "prompt_tokens": 9,
    "total_tokens": 134
  }
}
'''