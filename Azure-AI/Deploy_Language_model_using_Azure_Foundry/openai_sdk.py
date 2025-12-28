from openai import OpenAI

endpoint = "https://rajeshkappoor-3629-resource.openai.azure.com/openai/v1"
deployment_name = "Phi-4-reasoning"
api_key = "YOUR_AZURE_INFERENCE_SDK_KEY"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(completion.choices[0].message)