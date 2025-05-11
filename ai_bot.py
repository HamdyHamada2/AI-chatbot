from flask import Flask, request, jsonify
import difflib

app = Flask(__name__)

# قاعدة بيانات منتجات بسيطة (كمثال)
products = {
    "battery": {
        "name": "Battery",
        "description": "A power source for electronic circuits.",
        "usage": "Used to power devices.",
        "installation": "Connect the positive and negative terminals correctly."
    },
    "transistor": {
        "name": "Transistor",
        "description": "A semiconductor device for amplification or switching.",
        "usage": "Used in amplification and digital logic circuits.",
        "installation": "Place it according to circuit diagram (E-B-C)."
    },
    "IC": {
        "name": "IC (Integrated Circuit)",
        "description": "A miniaturized electronic circuit.",
        "usage": "Used in all kinds of electronics from computers to calculators.",
        "installation": "Fit it properly in the socket with correct orientation."
    }
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("question", "").lower()

    # البحث عن المنتج الأقرب من السؤال
    best_match = None
    best_ratio = 0

    for key in products:
        ratio = difflib.SequenceMatcher(None, key, question).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = key

    if best_ratio > 0.4:
        product = products[best_match]
        reply = (
            f"Product: {product['name']}\n"
            f"Description: {product['description']}\n"
            f"Usage: {product['usage']}\n"
            f"Installation: {product['installation']}"
        )
    else:
        reply = "Sorry, I couldn't find relevant information about your question."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(port=5001)