import json
import difflib

class ProductQAModel:
    def __init__(self, data_path="data/products.json"):
        with open(data_path, "r", encoding="utf-8") as f:
            self.products = json.load(f)

    def find_answer(self, question):
        question = question.lower()
        for product in self.products:
            keywords = [product["name"], product["category"]]
            for kw in keywords:
                if kw.lower() in question:
                    return f"{product['name']} - {product['description']}. Usage: {product['usage']}. Price: {product['price']} EGP"
        product_names = [p["name"] for p in self.products]
        closest = difflib.get_close_matches(question, product_names, n=1)
        if closest:
            matched = next((p for p in self.products if p["name"] == closest[0]), None)
            return f"Did you mean: {matched['name']}? {matched['description']} (Usage: {matched['usage']})"
        return "Sorry, I couldn't find an answer for that."
