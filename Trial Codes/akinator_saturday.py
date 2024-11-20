import tkinter as tk
from tkinter import messagebox
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import numpy as np
import pandas as pd

class FoodAkinatorGame:
    def __init__(self, root, data_path):
        self.root = root
        self.root.title("Akinator - Guess the Food!")
        self.root.geometry("800x600")

        # Load and preprocess data
        self.data = pd.read_csv(data_path)
        self.features = self.data.columns[1:]
        self.target = "Food Item"

        self.one_hot_encoder = OneHotEncoder()
        self.label_encoder = LabelEncoder()
        self.X = self.one_hot_encoder.fit_transform(self.data[self.features]).toarray()
        self.y = self.label_encoder.fit_transform(self.data[self.target])

        self.feature_names = self.one_hot_encoder.get_feature_names_out(self.features)
        self.food_items = self.label_encoder.classes_

        # Train Decision Tree model
        self.model = DecisionTreeClassifier(random_state=42)
        self.model.fit(self.X, self.y)

        # Game state
        self.remaining_probabilities = np.ones(len(self.food_items)) / len(self.food_items)
        self.remaining_questions = list(self.feature_names)
        self.asked_questions = []
        self.current_question = None

        # UI Components
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=700)
        self.question_label.pack(pady=20)

        self.yes_button = tk.Button(root, text="Yes", command=lambda: self.answer("yes"), width=10)
        self.yes_button.pack(side="left", padx=10, pady=20)

        self.no_button = tk.Button(root, text="No", command=lambda: self.answer("no"), width=10)
        self.no_button.pack(side="left", padx=10, pady=20)

        self.maybe_button = tk.Button(root, text="Maybe", command=lambda: self.answer("maybe"), width=10)
        self.maybe_button.pack(side="left", padx=10, pady=20)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
        self.feedback_label.pack(pady=10)

        self.show_question()

    def show_question(self):
        """Displays the next best question based on feature importance."""
        if len(self.remaining_questions) == 0 or np.max(self.remaining_probabilities) > 0.8:
            self.make_guess()
            return

        # Choose the next best question based on model's feature importance
        feature_importances = self.model.feature_importances_
        valid_importances = [feature_importances[i] if name in self.remaining_questions else 0 for i, name in enumerate(self.feature_names)]
        question_idx = np.argmax(valid_importances)

        self.current_question = self.feature_names[question_idx]
        self.remaining_questions.remove(self.current_question)
        self.question_label.config(text=f"Does the food have the feature '{self.current_question}'?")

    def answer(self, response):
        """Updates probabilities based on user response."""
        response_mapping = {"yes": 1, "no": 0, "maybe": 0.5}
        response_value = response_mapping[response]

        # Update probabilities based on response
        feature_idx = list(self.feature_names).index(self.current_question)
        for i in range(len(self.remaining_probabilities)):
            if self.X[i, feature_idx] == response_value:
                self.remaining_probabilities[i] *= 1
            else:
                self.remaining_probabilities[i] *= 0.1

        # Normalize probabilities
        self.remaining_probabilities /= np.sum(self.remaining_probabilities)
        self.show_question()

    def make_guess(self):
        """Makes a guess based on the highest probability."""
        best_guess_idx = np.argmax(self.remaining_probabilities)
        best_guess = self.food_items[best_guess_idx]

        # Handle multiple possibilities
        if np.max(self.remaining_probabilities) <= 0.8:
            possible_items = [self.food_items[i] for i in np.argsort(self.remaining_probabilities)[-5:][::-1]]
            messagebox.showinfo("Akinator's Possibilities", f"I couldn't decide. Possible answers are: {', '.join(possible_items)}.")
            self.ask_feedback(possible_items)
        else:
            messagebox.showinfo("Akinator's Guess", f"I guess your food item is {best_guess}!")
            self.reset_game()

    def ask_feedback(self, possible_items):
        """Ask for feedback to update the dataset."""
        correct_answer = messagebox.askstring("Feedback", f"Out of these, which one is correct?\n{', '.join(possible_items)}")
        if correct_answer and correct_answer in self.food_items:
            self.update_dataset(correct_answer)
        self.reset_game()

    def update_dataset(self, correct_answer):
        """Update dataset with the feedback."""
        correct_idx = list(self.food_items).index(correct_answer)
        new_row = self.X[correct_idx].tolist() + [correct_answer]
        self.data.loc[len(self.data)] = new_row
        self.X = self.one_hot_encoder.fit_transform(self.data[self.features]).toarray()
        self.y = self.label_encoder.fit_transform(self.data[self.target])
        self.model.fit(self.X, self.y)
        self.feedback_label.config(text="Thank you for the feedback! I've learned something new.")

    def reset_game(self):
        """Resets the game state for a new round."""
        self.remaining_probabilities = np.ones(len(self.food_items)) / len(self.food_items)
        self.remaining_questions = list(self.feature_names)
        self.asked_questions = []
        self.current_question = None
        self.show_question()


# Main Application
root = tk.Tk()
game = FoodAkinatorGame(root, 'akinator.csv')
root.mainloop()
