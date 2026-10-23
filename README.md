# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
  A Streamlit number guessing game where you guess a secret number and get higher/lower hints.
- [X] Detail which bugs you found.
  The hints were swapped, the secret became a string on even attempts.
- [X] Explain what fixes you applied.
I swapped the hint messages back in check_guess so “Too High” tells the player to go lower and “Too Low” tells them to go higher, removed the code that turned the secret into a string on even attempts so every guess is compared as a number, moved the game logic into logic_utils.py, and added pytest tests that confirm the outcomes and hint messages.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `python -m streamlit run app.py` from the project folder to open the game in your browser.
2. Open "Developer Debug Info" to see the secret number.
3. Guess a number below the secret. The hint now says "Go HIGHER."
4. Guess a number above the secret. The hint now says "Go LOWER," including on even-numbered attempts.
5. Guess the secret to win and see the "You won!" message with your score.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
collected 4 items                                                                                                 

tests\test_game_logic.py ....                                                                               [100%]

=============================================== 4 passed in 0.03s ================================================
```
