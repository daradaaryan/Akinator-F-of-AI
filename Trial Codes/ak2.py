import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
import random


class QLearningFeatureSelector:
    def __init__(self, features, actions=["Yes", "No", "Maybe"], alpha=0.1, gamma=0.9):
        self.features = features
        self.actions = actions
        self.q_table = pd.DataFrame(0, index=features, columns=actions)  # Initialize Q-table with zeros
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor

    def select_feature(self, asked_features):
        """
        Select the feature with the highest Q-value among unasked features.
        """
        remaining_features = [f for f in self.features if f not in asked_features]
        if not remaining_features:
            return None
        q_values = self.q_table.loc[remaining_features].sum(axis=1)  # Sum Q-values for all actions
        max_q_value = q_values.max()
        best_features = q_values[q_values == max_q_value].index.tolist()
        return random.choice(best_features)

    def update_q_value(self, feature, action, reward, next_feature=None):
        """
        Update the Q-value for a specific feature-action pair.
        """
        current_q = self.q_table.loc[feature, action]
        max_next_q = self.q_table.loc[next_feature].max() if next_feature else 0
        updated_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
        self.q_table.loc[feature, action] = updated_q


class FoodAkinatorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Powered Food Akinator")
        self.root.geometry("600x700")

        # Load Akinator image
        self.image = Image.open("akinator.png")
        self.image = self.image.resize((150, 150), Image.Resampling.LANCZOS)
        self.akinator_img = ImageTk.PhotoImage(self.image)

        # Dataset
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
        }
        self.features = ["Veg", "Spicy", "Vegan", "Solid", "Main", "Hot"]
        self.food_names = list(self.food_items.keys())
        self.data = pd.DataFrame(self.food_items).T.astype(int)

        # Game state
        self.language = "English"
        self.difficulty = "Medium"
        self.asked_features = set()
        self.responses = {}
        self.q_selector = QLearningFeatureSelector(self.features)

        # Load UI
        self.setup_ui()
        self.select_language()
        self.select_difficulty()
        self.update_buttons_text()
        self.show_next_question()

    def setup_ui(self):
        # Display Akinator image
        self.image_label = tk.Label(self.root, image=self.akinator_img)
        self.image_label.pack(pady=10)

        # Question Label
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        # Answer Buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)
        self.yes_button = tk.Button(self.buttons_frame, text="Yes", command=lambda: self.answer("yes"), width=10)
        self.no_button = tk.Button(self.buttons_frame, text="No", command=lambda: self.answer("no"), width=10)
        self.maybe_button = tk.Button(self.buttons_frame, text="Maybe", command=lambda: self.answer("maybe"), width=10)
        self.yes_button.grid(row=0, column=0, padx=5)
        self.no_button.grid(row=0, column=1, padx=5)
        self.maybe_button.grid(row=0, column=2, padx=5)

    def get_response_map(self):
        return {
            "English": {"yes": "Yes", "no": "No", "maybe": "Maybe", "guess": "I guess your food is"},
            "Hindi": {"yes": "हाँ", "no": "नहीं", "maybe": "शायद", "guess": "मुझे लगता है कि आपका खाना है"},
            "Spanish": {"yes": "Sí", "no": "No", "maybe": "Tal vez", "guess": "Creo que tu comida es"},
        }

    def select_language(self):
        supported_languages = {"english": "English", "hindi": "Hindi", "spanish": "Spanish"}
        user_input = simpledialog.askstring("Language Selection", "Choose a language (English, Hindi, Spanish):")
        self.language = supported_languages.get(user_input.lower(), "English")

    def select_difficulty(self):
        supported_difficulties = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}
        user_input = simpledialog.askstring("Difficulty Selection", "Choose difficulty (Easy, Medium, Hard):")
        self.difficulty = supported_difficulties.get(user_input.lower(), "Medium")

    def update_buttons_text(self):
        responses = self.get_response_map()[self.language]
        self.yes_button.config(text=responses["yes"])
        self.no_button.config(text=responses["no"])
        self.maybe_button.config(text=responses["maybe"])

    def select_next_feature(self):
        if self.difficulty == "Hard":
            return self.q_selector.select_feature(self.asked_features)
        else:
            remaining_features = [f for f in self.features if f not in self.asked_features]
            return random.choice(remaining_features) if remaining_features else None

    def show_next_question(self):
        next_feature = self.select_next_feature()
        if next_feature:
            self.current_feature = next_feature
            question_map = {
                "Veg": {"English": "Is it vegetarian?", "Hindi": "क्या यह शाकाहारी है?", "Spanish": "¿Es vegetariano?"},
                "Spicy": {"English": "Is it spicy?", "Hindi": "क्या यह मसालेदार है?", "Spanish": "¿Es picante?"},
                "Vegan": {"English": "Is it vegan?", "Hindi": "क्या यह वेगन है?", "Spanish": "¿Es vegano?"},
                "Solid": {"English": "Is it solid?", "Hindi": "क्या यह ठोस है?", "Spanish": "¿Es sólido?"},
                "Main": {"English": "Is it a main course dish?", "Hindi": "क्या यह मुख्य भोजन है?", "Spanish": "¿Es plato principal?"},
                "Hot": {"English": "Is it served hot?", "Hindi": "क्या यह गरम परोसा जाता है?", "Spanish": "¿Se sirve caliente?"},
            }
            self.question_label.config(text=question_map[next_feature][self.language])
            self.asked_features.add(next_feature)
        else:
            self.make_guess()

    def answer(self, response):
        if response == "yes":
            self.data = self.data[self.data[self.current_feature] == 1]
        elif response == "no":
            self.data = self.data[self.data[self.current_feature] == 0]

        # Update Q-table in Hard mode
        if self.difficulty == "Hard":
            reward = len(self.data)
            self.q_selector.update_q_value(self.current_feature, response.capitalize(), reward)

        self.show_next_question()

    def make_guess(self):
        remaining_items = self.data.index.tolist()
        responses = self.get_response_map()[self.language]
        if len(remaining_items) == 1:
            guessed_food = remaining_items[0]
            messagebox.showinfo("Guess", f"{responses['guess']} {guessed_food}.")
        elif len(remaining_items) > 1:
            messagebox.showinfo("Guess", f"Multiple possibilities: {', '.join(remaining_items)}.")
        else:
            messagebox.showinfo("Guess", "Food not found in dataset.")
        self.root.quit()


# Run the game
root = tk.Tk()
game = FoodAkinatorGame(root)
root.mainloop()
