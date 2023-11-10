import base64
import argparse
import requests

RECYCLING_STREAMS = """
Automotive batteries (lead acid)
Carton packaging
Construction waste
Electrical equipments
End-of-life textiles
Energy waste
Garden waste
Glass packaging
Hazardous waste
Impregnated wood
Lamps
Metals
Mixed waste
Other waste
Paper
Plastic packaging
Portable accumulators and batteries
Textiles (reusable)
Wood
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image")
    args = parser.parse_args()

    # OpenAI API Key
    with open("api_key.txt") as f:
        api_key = f.read().strip()

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
    image_path = args.image

    # Getting the base64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "You are a helpful assistant that helps to identify what can be recycled in an image. "
                            f"Here are a list of available recycling streams: {RECYCLING_STREAMS}"
                            "\n"
                            "You will tell what is in the image. Tell me what pieces it can be separated into."
                        )
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": ""
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    print(response.json())


if __name__ == "__main__":
    main()