from flask import Flask, request, jsonify
from model.qa_model import ProductQAModel

app = Flask(__name__)
qa_model = ProductQAModel()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    answer = qa_model.find_answer(question)
    return jsonify(answer=answer)

if __name__ == "__main__":
    app.run(port=5005)
