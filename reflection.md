# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
When I first started and played for the first time, the answers were backwards. I guessed 50, 25, 10, and 1 and was told to guess lower on every single one of those attempts for the hint even though the secret told me the number was 65. Then I guessed 80 and the hint said I needed to guess higher. I also tried to start a new game and that did not work until I spam clicked the button multiple times. I also found that the same guess could get different hints on different attempts, because on even-numbered attempts the game turned the secret number into a string, so Python compared the two values as text instead of as numbers.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50    |"Go Higher"        | "Go Lower"      |none                    |
|80     |"Go Lower"         | "Go Higher"     |none |
|clicked new game |start new game | had to click repeatedly| none      |
|Start Game | Attempts: 0   | Attempts: 1     |none                    |
| 120 (secret 4), guessed twice | Same hint both times | "Go HIGHER" once, "Go LOWER" once | none |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
A suggestion that Claude made that ended up being correct was fixing the swapped hint messages and leaving the comparison alone. This was because the outcome labels feed the score. I verified this by starting a new game, reading the secret in the debug panel, then guessing above and below it.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
Claude suggested that I go to logic_utils.py to find the hint bug, but that file only held stubs. The real logic was in app.py. I opened logic_utils.py, saw that every function raised NotImplementedError, and searched app.py instead.
--- 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
