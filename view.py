import asyncio
import ssl
from flask import Flask, request
from flask_cors import CORS
import os
from vision import encode_image, analyze_image
from hsy import THREADED_HSY_OPTIONS
import json
import base64


app = Flask(__name__)
CORS(app)

STREAMS = {
    x["name"]: x["options"]
    for x in THREADED_HSY_OPTIONS
}

@app.route("/api/vision", methods=["POST", "GET"])
async def get_data():
    print(request.files)
    base64_image = base64.b64encode(request.files["img"].read()).decode('utf-8')

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

    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
