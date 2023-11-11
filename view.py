import asyncio
import ssl
from flask import Flask, request
import os
from vision import encode_image, analyze_image
from hsy import THREADED_HSY_OPTIONS
import json


app = Flask(__name__)

STREAMS = {
    x["name"]: x["options"]
    for x in THREADED_HSY_OPTIONS
}

@app.route("/api/vision")
async def get_data():
    base64_image = json.loads(request.data.decode())["img"]

    data = """
        [
        "Textiles (reusable)",
        "Plastic packaging",
        "Paper"
        ]
"""

    data = await analyze_image(base64_image, api_key)
    data = json.loads(data)

    return [
        {
            "stream": d["stream"],
            "options": STREAMS[d["stream"]],
            "instructions": d["instructions"]
        } for d in data if d["stream"] in STREAMS
    ]


if __name__ == "__main__":
    # OpenAI API Key
    with open("api_key.txt") as f:
        api_key = f.read().strip()

    port = int(os.environ.get('PORT', 5555))
    app.run(debug=True, host='0.0.0.0', port=port)
