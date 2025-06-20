# app.py

from flask import Flask, request, jsonify
from riot_api import get_summoner_data

app = Flask(__name__)

@app.route("/summoner", methods=["GET"])
def summoner():
    summoner_name = request.args.get("name")
    if not summoner_name:
        return jsonify({"error": "Summoner name is required"}), 400

    data = get_summoner_data(summoner_name)

    if "status" in data:
        return jsonify({"error": data["status"]["message"]}), data["status"]["status_code"]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
