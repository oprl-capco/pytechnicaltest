# Python Technical Test
Contains technical exercises and snippets for Python technical interviews.
## Setup
1. Ensure that you have Python 3 and pip installed.
2. Once done, go to terminal and `pip install fastapi`
3. Then `pip install pytest`
## Guidance
### Content
The `problems` contain technical challenges that the candidate can answer independently, as well as their corresponding unit tests. `snippets1.py` contains code that can be runnable on command line, which the interviewer can ask the candidate about. `snippets2.py` contains refactoring exercises with corresponding unit tests that the interviewer can ask the candidate about.
### Conditions
Candidate should ideally not be using any external Python libraries except the ones specified in this README. Candidate should also ensure that unit tests in this repository are not modified.
### Unit testing
For all exercises unit tests have been developed so that the candidate can check their answers are correct using terminal or cmd. <br/><br/>
To test the answers, cd to the root of the repository and then run the command `python3 -m pytest problems/tests` for the problem exercises and `python3 -m pytest snippets` for the refactoring exercises in snippets2.py. <br/><br/>Specific tests can be run by specifying the test class you want to run for example `python3 -m pytest problems/tests/{testclass.py}`
