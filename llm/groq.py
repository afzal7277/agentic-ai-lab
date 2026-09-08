from groq import Groq

from config import GROQ_API_KEY
from . import LLMProvider


class GroqProvider(LLMProvider):

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, prompt: str, tools=None) -> str:

        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]

        groq_tools = []

        if tools:
            for tool in tools:
                groq_tools.append(
                    {
                        "type": "function",
                        "function": {
                            "name": tool.__name__,
                            "description": tool.__doc__ or "",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "expression": {
                                        "type": "string",
                                        "description": "Mathematical expression to calculate.",
                                    }
                                },
                                "required": ["expression"],
                            },
                        },
                    }
                )

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            tools=groq_tools if groq_tools else None,
            tool_choice="auto" if groq_tools else "none",
        )

        message = response.choices[0].message

        if not message.tool_calls:
            return message.content

        for tool_call in message.tool_calls:

            if tool_call.function.name == "calculate":

                import json

                arguments = json.loads(tool_call.function.arguments)

                expression = arguments["expression"]

                result = tools[0](expression)

                messages.append(message)

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result),
                    }
                )

        final_response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
        )

        return final_response.choices[0].message.content