import base64
import argparse
import requests

KIERRATYS_MATERIAL_TYPES = {
  "count": 20,
  "next": None,
  "previous": None,
  "results": [
    {
      "code": 120,
      "name": "End-of-life textiles"
    },
    {
      "code": 119,
      "name": "Construction Waste"
    },
    {
      "code": 118,
      "name": "Impregnated Wood"
    },
    {
      "code": 117,
      "name": "Wood"
    },
    {
      "code": 116,
      "name": "Lamps"
    },
    {
      "code": 115,
      "name": "Car Batteries"
    },
    {
      "code": 114,
      "name": "Other Waste"
    },
    {
      "code": 113,
      "name": "Textiles"
    },
    {
      "code": 111,
      "name": "Plastic"
    },
    {
      "code": 110,
      "name": "Portable accumulators and batteries"
    },
    {
      "code": 109,
      "name": "Electronic Devices"
    },
    {
      "code": 108,
      "name": "Dangerous Waste"
    },
    {
      "code": 107,
      "name": "Glass"
    },
    {
      "code": 106,
      "name": "Metal"
    },
    {
      "code": 105,
      "name": "Cardboard Packaging"
    },
    {
      "code": 104,
      "name": "Cardboard"
    },
    {
      "code": 103,
      "name": "Paper"
    },
    {
      "code": 102,
      "name": "Energy Waste"
    },
    {
      "code": 101,
      "name": "Garden Waste"
    },
    {
      "code": 100,
      "name": "Mixed waste"
    }
  ]
}

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


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image")
    args = parser.parse_args()

    # OpenAI API Key
    with open("api_key.txt") as f:
        api_key = f.read().strip()

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