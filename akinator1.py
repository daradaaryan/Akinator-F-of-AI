import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np

class FoodAkinatorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Powered Food Akinator")
        self.root.geometry("600x700")

        # Load Akinator image
        self.image = Image.open("akinator.png")
        self.image = self.image.resize((150, 150), Image.Resampling.LANCZOS)
        self.akinator_img = ImageTk.PhotoImage(self.image)

        # Dataset with features
        self.food_items = {
    "pizza": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "sushi": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": False},
    "ice cream": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "biryani": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "salad": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": False, "Hot": False},
    "burger": {"Veg": True, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "pasta": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "ramen": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "tacos": {"Veg": True, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "sandwich": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": False, "Hot": False},
    "falafel": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": False, "Hot": True},
    "paneer tikka": {"Veg": True, "Spicy": True, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "chicken curry": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "noodles": {"Veg": True, "Spicy": True, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "spring rolls": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": False, "Hot": True},
    "dumplings": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "fried rice": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "paella": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "lasagna": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "cheesecake": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "gazpacho": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": False, "Main": False, "Hot": False},
    "quiche": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "hummus": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": False, "Main": False, "Hot": False},
    "steak": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "apple pie": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "brownie": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "fish and chips": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "shawarma": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "tortilla": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": False, "Hot": True},
    "samosa": {"Veg": True, "Spicy": True, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "guacamole": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": False, "Main": False, "Hot": False},
    "beef stew": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "moussaka": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "ratatouille": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": False, "Main": True, "Hot": True},
    "currywurst": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "churros": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "tiramisu": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "pho": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "frittata": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "risotto": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "pancakes": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "couscous": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": True, "Hot": True},
    "gnocchi": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "baklava": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "poutine": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "mac and cheese": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "lobster bisque": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "clam chowder": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "creme brulee": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "tempura": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "ceviche": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": False, "Main": True, "Hot": False},
    "gazelle horns": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "banh mi": {"Veg": True, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "bbq ribs": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "fajitas": {"Veg": True, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "pad thai": {"Veg": True, "Spicy": True, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "schnitzel": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "bruschetta": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": False, "Hot": False},
    "gelato": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "spaghetti": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "kebab": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "miso soup": {"Veg": False, "Spicy": False, "Vegan": True, "Solid": False, "Main": False, "Hot": True},
    "onion rings": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "panna cotta": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "naan": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "tandoori chicken": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "chana masala": {"Veg": True, "Spicy": True, "Vegan": True, "Solid": False, "Main": True, "Hot": True},
    "poached eggs": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "fish tacos": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "pavlova": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "beetroot salad": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": False, "Hot": False},
    "goulash": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "chocolate mousse": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "okra fries": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": False, "Hot": True},
    "stuffed peppers": {"Veg": True, "Spicy": True, "Vegan": True, "Solid": True, "Main": True, "Hot": True},
    "pho ga": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "lemon tart": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "ratatouille gratin": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": True, "Hot": True},
    "butter chicken": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "tom kha gai": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": False, "Main": True, "Hot": True},
    "aloo gobi": {"Veg": True, "Spicy": True, "Vegan": True, "Solid": True, "Main": True, "Hot": True},
    "bratwurst": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "apple strudel": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "kung pao chicken": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "vindaloo": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "falooda": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": False, "Main": False, "Hot": False},
    "potato wedges": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": False, "Hot": True},
    "lobster thermidor": {"Veg": False, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "ravioli": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "cornbread": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": True},
    "bbq pulled pork": {"Veg": False, "Spicy": True, "Vegan": False, "Solid": True, "Main": True, "Hot": True},
    "caramel custard": {"Veg": True, "Spicy": False, "Vegan": False, "Solid": True, "Main": False, "Hot": False},
    "roasted veggies": {"Veg": True, "Spicy": False, "Vegan": True, "Solid": True, "Main": False, "Hot": True}
}


        self.features = ["Veg", "Spicy", "Vegan", "Solid", "Main", "Hot"]
        self.reset_probabilities()

        # Display Akinator image
        self.image_label = tk.Label(root, image=self.akinator_img)
        self.image_label.pack(pady=10)

        # Display question
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        # Answer Buttons
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)
        self.yes_button = tk.Button(self.buttons_frame, text="Yes", command=lambda: self.answer("yes"), width=10)
        self.yes_button.grid(row=0, column=0, padx=5)
        self.no_button = tk.Button(self.buttons_frame, text="No", command=lambda: self.answer("no"), width=10)
        self.no_button.grid(row=0, column=1, padx=5)
        self.maybe_button = tk.Button(self.buttons_frame, text="Maybe", command=lambda: self.answer("maybe"), width=10)
        self.maybe_button.grid(row=0, column=2, padx=5)

        self.progress_label = tk.Label(root, text="", font=("Arial", 12))
        self.progress_label.pack(pady=5)

        self.current_feature = None
        self.show_next_question()

    def reset_probabilities(self):
        self.probabilities = {food: 1 / len(self.food_items) for food in self.food_items}
        self.asked_features = set()

    def calculate_entropy(self, probabilities):
        return -sum(p * np.log2(p) for p in probabilities if p > 0)

    def calculate_expected_information_gain(self, feature):
        yes_prob = sum(
            self.probabilities[food] for food, attrs in self.food_items.items() if attrs[feature]
        )
        no_prob = 1 - yes_prob

        if yes_prob == 0 or no_prob == 0:
            return 0

        # Simulate entropy after asking the question
        yes_entropy = self.calculate_entropy([
            self.probabilities[food] / yes_prob
            for food, attrs in self.food_items.items()
            if attrs[feature]
        ])
        no_entropy = self.calculate_entropy([
            self.probabilities[food] / no_prob
            for food, attrs in self.food_items.items()
            if not attrs[feature]
        ])

        # Weighted average of entropies
        return self.calculate_entropy(self.probabilities.values()) - (yes_prob * yes_entropy + no_prob * no_entropy)

    def select_question(self):
        remaining_features = [f for f in self.features if f not in self.asked_features]
        if not remaining_features:
            return None

        # Calculate information gain for each feature
        feature_gains = {
            feature: self.calculate_expected_information_gain(feature) for feature in remaining_features
        }

        # Select the feature with the highest information gain
        best_feature = max(feature_gains, key=feature_gains.get)
        return best_feature

    def show_next_question(self):
        if max(self.probabilities.values()) < 0.9:
            self.current_feature = self.select_question()
            if self.current_feature:
                question = self.generate_question(self.current_feature)
                self.question_label.config(text=question)
                self.asked_features.add(self.current_feature)
            else:
                self.make_guess()
        else:
            self.make_guess()

    def generate_question(self, feature):
        question_map = {
            "Veg": "Is it vegetarian?",
            "Spicy": "Is it spicy?",
            "Vegan": "Is it vegan?",
            "Solid": "Is it solid in form?",
            "Main": "Is it a main course dish?",
            "Hot": "Is it served hot?",
        }
        return question_map.get(feature, f"Does it have the feature {feature}?")

    def update_probabilities(self, response):
        for food, attrs in self.food_items.items():
            value = attrs.get(self.current_feature)

            if response == "yes":
                match = value
                self.probabilities[food] *= 1.0 if match else 0.0
            elif response == "no":
                match = not value
                self.probabilities[food] *= 1.0 if match else 0.0
            elif response == "maybe":
                self.probabilities[food] *= 0.5  # Reduce probability slightly for "maybe"

        total_prob = sum(self.probabilities.values())
        if total_prob == 0:
            self.reset_probabilities()
        else:
            for food in self.probabilities:
                self.probabilities[food] /= total_prob

    def make_guess(self):
        best_guess = max(self.probabilities, key=self.probabilities.get)
        probability = self.probabilities[best_guess]

        if probability > 0.9:
            messagebox.showinfo("AI Guess", f"I guess your food is {best_guess}!")
            self.root.quit()
        else:
            possible_items = [item for item, prob in self.probabilities.items() if prob > 0.1]
            possible_guesses = ", ".join(possible_items)
            self.question_label.config(text=f"I'm not sure. It could be one of these: {possible_guesses}.")
            most_likely = max(possible_items, key=lambda item: self.probabilities[item])
            self.progress_label.config(text=f"Most likely: {most_likely}")

    def answer(self, response):
        self.update_probabilities(response)
        self.show_next_question()

# Main application
root = tk.Tk()
game = FoodAkinatorGame(root)
root.mainloop()
