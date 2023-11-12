import asyncio
import ssl
from flask import Flask, request
from flask_cors import CORS, cross_origin
import os
from vision import encode_image, analyze_image, ITEM_CLASSIFICATION
from hsy import THREADED_HSY_OPTIONS
import json
import base64
import logging


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.getLogger('flask_cors').level = logging.DEBUG

WASTE_STREAMS = {
    x["name"]: x["options"]
    for x in THREADED_HSY_OPTIONS
}
ITEM_CLASSIFICATION_STREAMS = {
    x["name"]: x["options"]
    for x in ITEM_CLASSIFICATION
}

@app.route("/api/waste", methods=["POST", "GET"])
async def get_data():
    base64_image = base64.b64encode(request.files["img"].read()).decode('utf-8')

    data = await analyze_image(base64_image, api_key, mode="waste")
    data = json.loads(data)

    return [
        {
            "stream": d["stream"],
            "options": WASTE_STREAMS[d["stream"]],
            "instructions": d["instructions"]
        } for d in data if d["stream"] in WASTE_STREAMS
    ]


@app.route("/api/donate", methods=["POST", "GET"])
async def get_data_donate():
    base64_image = base64.b64encode(request.files["img"].read()).decode('utf-8')

    data = await analyze_image(base64_image, api_key, mode="donate")
    data = json.loads(data)

    return [
        {
            "stream": d["stream"],
            "options": ITEM_CLASSIFICATION_STREAMS[d["stream"]],
            "instructions": d["instructions"]
        } for d in data if d["stream"] in ITEM_CLASSIFICATION_STREAMS
    ]


if __name__ == "__main__":
    # OpenAI API Key
    with open("api_key.txt") as f:
        api_key = f.read().strip()

    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
