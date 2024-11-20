# Akinator-F-of-AI
We are making an Akinator using concepts of the course Foundations of AI - CS 329 by Prof. Neeldhara Misra and Prof. Manisha Padala.  
  
  
# Food Akinator Game

An AI-powered food guessing game built using Python, tkinter, and Q-Learning. This project lets you interact with a friendly "Food Akinator" that guesses your food choice based on your answers to questions.

## Features
- Multi-language support (English, Hindi, Spanish)
- Multiple difficulty levels
- Uses Q-Learning to enhance guessing accuracy

---

## How to Set Up and Run

### Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone <repo-url>
cd <repo-name>
```
---

### Add the Image File
Make sure the image file `akinator.png` is placed in the same directory as the script. This image will be used in the game's UI.

> **Note:** You can use any image, but ensure the filename is `akinator.png`. If using a different file name, update the script accordingly.

---

### Run the Game

Execute the script in your terminal:
```bash
python akinator1.py
```
or
```bash
python akinator2.py
```

---

### How to Play

1. **Start the Game**:
   - After running the script, a dialog box will prompt you to choose a language (English, Hindi, or Spanish).
   - Select the difficulty level (Easy, Medium, or Hard) in the next dialog box.

2. **Answer Questions**:
   - The game will display questions about your food preferences.
   - Use the buttons (`Yes`, `No`, `Maybe`) to answer.

3. **Food Guessing**:
   - Based on your answers, the game will try to guess your food.
   - If multiple options match, it will display all possible choices.

4. **Exit the Game**:
   - After the game guesses your food, it will close automatically.

---

### Requirements

- Python 3.10 or above
- The following Python libraries:
  - `tkinter` (usually included with Python)
  - `Pillow`
  - `pandas`
  - `numpy`

You can install these using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

### Troubleshooting

1. **tkinter Not Installed**:
   On some Linux systems, tkinter may not be included. Install it using:
   ```bash
   sudo apt-get install python3-tk
   ```

2. **Image File Issues**:
   Ensure `akinator.png` is in the same directory as the script and is accessible. Resize it appropriately if it's too large.

3. **Missing Dependencies**:
   Ensure all required libraries are installed by running:
   ```bash
   pip install -r requirements.txt
   ```

---

### Contributing

Feel free to contribute to this project by:
- Improving the UI
- Adding more food items
- Enhancing the Q-Learning algorithm


