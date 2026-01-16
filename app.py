from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "API RUNNING OK"

@app.route("/join")
def join():
    tc = request.args.get("tc")
    uid = request.args.get("uid1")
    emote = request.args.get("emote_id")

    if not tc or not uid or not emote:
        return jsonify({"error": "missing params"}), 400

    return jsonify({
        "status": "success",
        "tc": tc,
        "uid": uid,
        "emote": emote
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
