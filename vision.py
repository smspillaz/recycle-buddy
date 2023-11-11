import base64
import argparse
import requests
import json
import aiohttp
import re
import os

from hsy import THREADED_HSY_OPTIONS, HSY_MAIN_TYPES

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


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


async def analyze_image(base64_image, api_key):
    client = aiohttp.ClientSession()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    streams = '\n'.join(list(map(lambda x: x['name'], THREADED_HSY_OPTIONS)))

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
                            f"Here are a list of available recycling streams: {streams}"
                            "\n"
                            "You will tell what is in the image. Tell me what streams it can be separated into.\n"
                            "Output the likely streams as a JSON list of objects, "
                            "where each object has the stream name and instructions for how to separate the part that goes in the stream from the object."
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

    if os.environ.get("DEBUG", "0") != "1":
        async with client.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload) as resp:
            response = await resp.json()
            text_response = response["choices"][0]["message"]["content"].replace("\n", " ")
    else:
        text_response = """
    The image shows what appears to be a lanyard, typically made of fabric or synthetic materials, with a plastic buckle and possibly a metal clasp attached to a card (likely paper or plastic) with printed information, year "2023", and possibly a QR code. Based on the materials observable, here are the potential recycling streams:\n\n```json\n[\n  {\n    "stream": "Plastic",\n    "instructions": "Separate the plastic buckle from the fabric strap if possible. Recycle as hard plastic if your local facility accepts this type of plastic."\n  },\n  {\n    "stream": "Metal",\n    "instructions": "Detach any metal parts such as clasps from the lanyard and recycle as scrap metal."\n  },\n  {\n    "stream": "Clothes, in poor condition",\n    "instructions": "If the fabric strap is not reusable and is considered in poor condition, it can be discarded as specified by local regulations for textiles."\n  },\n  {\n    "stream": "Paper",\n    "instructions": "If the card is made of paper, recycle it with paper materials."\n  },\n  {\n    "stream": "Plastic box, compartment",\n    "instructions": "If the card is made of plastic and is similar to a plastic box or compartment, follow local guidelines for recycling such plastic items."\n  }\n]\n```\n\nPlease note that recycling policies and facilities may have specific sorting rules, and it\'s best to check with your local recycling
    """.replace("\n", " ")

    json_response = re.match(".*(?:json)?```(?:json)?(?P<content>.*)```.*", text_response).group("content")
    return json_response


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
                            "You will tell what is in the image. Tell me what pieces from the available streams it can be separated into."
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

    return response.json()


if __name__ == "__main__":
    main()