import asyncio
import ssl
from flask import Flask, request
import os
from vision import RECYCLING_STREAMS, KIERRATYS_MATERIAL_TYPES, encode_image

app = Flask(__name__)


async def async_get_data():
    await asyncio.sleep(1)
    return 'Done!'


@app.route("/api/vision")
async def get_data():
    data = await async_get_data()
    return data


if __name__ == "__main__":
    # OpenAI API Key
    with open("api_key.txt") as f:
        api_key = f.read().strip()

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)