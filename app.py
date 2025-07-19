from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend access

@app.route("/scan/code", methods=["POST"])
def scan_code():
    code = request.json.get("code", "")
    # Call your model or regex scanner here
    result = {
        "scanType": "code",
        "language": "python",  # or detect from code
        "issues": [
            {
                "id": "1",
                "severity": "high",
                "description": "Example hardcoded credential",
                "line": 12,
                "snippet": "password = 'admin123'",
                "mitigation": "Use environment variables."
            }
        ],
        "stats": {"total": 1, "high": 1, "medium": 0, "low": 0},
        "hasVulnerabilities": True
    }
    return jsonify(result)

@app.route("/scan/url", methods=["POST"])
def scan_url():
    url = request.json.get("url", "")
    result = {
        "scanType": "url",
        "url": url,
        "isMalicious": False,
        "threats": [],
        "stats": {"total": 0, "high": 0, "medium": 0, "low": 0}
    }
    return jsonify(result)

@app.route("/scan/sms", methods=["POST"])
def scan_sms():
    sms = request.json.get("sms", "")
    result = {
        "scanType": "sms",
        "isScam": True,
        "threats": [
            {
                "id": "1",
                "severity": "medium",
                "type": "Scam",
                "description": "Suspicious banking message",
                "mitigation": "Do not click links."
            }
        ],
        "stats": {"total": 1, "high": 0, "medium": 1, "low": 0}
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
