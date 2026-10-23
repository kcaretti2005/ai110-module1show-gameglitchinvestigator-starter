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
I decided whether a bug was really fixed or not by doing 2 things. The first being logically reasoning. I would make the fix and analyze the code and ask myself did this truly fix the bug or did it just cover up half of it. Because sometimes you are able to fix a problem but it does not debug the entire error itself it is like taping a leak, it'll eventually give. The second thing I do is test it a bunch. I got through and test the bug I just fixed to make sure it is completely patched. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran a pytest that where all 3 tests that I originally had failed with NotImplementedError because the logic was still in app.py. This basically told me my code was unorganized I had forgetten an entire step. Once I fixed this though it passed.
- Did AI help you design or understand any tests? How?
AI did help me here. Claude helped me understand why these errors were happening. I mainly used Claude as a debug assistant and would it explain to me why certain things are happening.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns your entire script from top to bottom every time something changes, like typing a guess or clicking a button. Because everything starts over on each rerun, a normal variable like the secret number would be thrown away and replaced every time, so the game could never remember it. Session state (st.session_state) is where the app stores values that need to survive reruns, like the secret, the number of attempts, the score, and the guess history. I saw this in the Developer Debug Info panel, which showed the old score and was missing my latest guess, because that panel runs above the code that handles my guess, so it shows the state from before the newest guess was processed.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I would say on habit or stategy from this project that I want to reuse is just the entire debugging process. I found myself more focused in on it due to the entire project essentially being that. I would go through a logical thought process and rule out answers. Then I would make a change and test and record my findings until I have fully debugged.
- What is one thing you would do differently next time you work with AI on a coding task?
I would probably use Claude in the side panel rather than just using it as a desktop browser. This would allow for much more efficiecy and time saved.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project has showed me that AI generated code is essentially useless if there is not an educated individual supervising. This code is indeed full and compelte. But it comes with many errors that logically make no sense as to why they would ever be there. Therefore you really need an educated individual to watch over AI generated code.