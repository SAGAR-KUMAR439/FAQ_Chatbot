# CodeAlpha FAQ Chatbot

## Overview

This project is an FAQ Chatbot developed as part of the CodeAlpha Artificial Intelligence Internship — Task 2.

The chatbot is designed to answer Python-related questions by matching a user's question with the most relevant question from a collection of frequently asked questions (FAQs).

The project uses Natural Language Processing (NLP) techniques and similarity-based matching to identify the most relevant FAQ and return its answer.

## Features

* Python-focused FAQ chatbot
* 410 FAQ entries
* Text preprocessing using NLTK
* Stop-word handling
* Word stemming using Porter Stemmer
* TF-IDF vectorization
* Cosine similarity
* Text similarity comparison
* Common-word analysis
* Topic overlap analysis
* Concept/intent matching for important Python concepts
* Handles paraphrased questions
* Handles unrelated questions using a confidence threshold
* Empty-input handling
* `exit` and `quit` commands
* Command-line interaction

## Technologies Used

* Python 3.10
* NLTK
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* Python `difflib`
* Python standard library

## How It Works

The chatbot follows several stages to process a user's question.

### 1. User Input

The user enters a Python-related question through the command-line interface.

### 2. Text Preprocessing

The input text is converted into a normalized form.

The preprocessing process includes:

* Converting text to lowercase
* Removing punctuation
* Removing common English stop words
* Preserving important Python keywords
* Applying stemming using the Porter Stemmer

### 3. TF-IDF Vectorization

The processed FAQ questions are converted into numerical vectors using TF-IDF.

TF-IDF helps represent the importance of words within the FAQ dataset.

### 4. Similarity Matching

The chatbot compares the user's question with the FAQ questions using cosine similarity.

Additional matching signals are also considered, including:

* Text similarity
* Common words
* Topic overlap
* Concept/intent matching

### 5. Concept Matching

For important Python topics, the chatbot identifies concepts such as:

* While loops
* For loops
* Loop comparison
* List iteration
* Iterators
* Iterables
* List mutability
* Exception handling
* Syntax errors
* Decorators
* Functions
* Variables
* Inheritance
* Strings
* Tuples
* Dictionaries
* Sets
* OOP

This helps the chatbot distinguish between questions that may contain similar words but refer to different concepts.

### 6. Best FAQ Selection

The chatbot evaluates the available FAQ entries and selects the most relevant candidate based on the combined matching score.

### 7. Response

If the selected match satisfies the chatbot's confidence conditions, its stored answer is displayed.

If the question does not reach the required confidence level, the chatbot responds that it does not know the answer.

## FAQ Dataset

The chatbot contains 410 Python-related FAQ entries covering topics such as:

* Python basics
* Variables
* Data types
* Type casting
* Strings
* Lists
* Tuples
* Sets
* Dictionaries
* Operators
* Conditional statements
* Loops
* Functions
* Scope
* Modules and packages
* File handling
* Exceptions
* Object-oriented programming
* Comprehensions
* Iterators and generators
* Decorators
* Lambda, map, filter and reduce
* Debugging and testing
* Virtual environments
* APIs
* HTTP
* REST APIs
* JSON
* NumPy
* Pandas
* Artificial Intelligence
* Machine Learning
* Deep Learning

## How to Run

Make sure Python 3.10 or a compatible Python version is installed.

Install the required packages:

```bash
py -m pip install nltk
py -m pip install scikit-learn
```

Then run:

```bash
python faq_chatbot.py
```

On Windows, the following can also be used:

```bash
py faq_chatbot.py
```

## Example Questions

Examples of questions supported by the chatbot include:

```text
What is Python?

What is a variable in Python?

How does a while loop work?

How do I iterate through a list?

Can Python lists be changed after creation?

What is the difference between a for loop and a while loop?

How can I handle errors in Python?

What is a decorator?

What is an iterator in Python?

What is machine learning?
```

## Project Structure

```text
CodeAlpha_FAQ_Chatbot/
¦
+-- faq_chatbot.py
+-- faqs.py
+-- README.md
+-- .gitignore
```

### faq_chatbot.py

Contains the main chatbot logic, preprocessing integration, similarity calculations, concept matching, FAQ selection and user interaction.

### faqs.py

Contains the FAQ dataset and the text preprocessing function.

### README.md

Contains project documentation and instructions.

### .gitignore

Contains files and directories that should not be uploaded to GitHub.

## Limitations

This chatbot is based on a predefined FAQ dataset.

It does not generate completely new answers like a large language model. Its responses depend on the questions and answers available in the FAQ dataset and the matching logic implemented in the project.

Questions outside the supported knowledge base may be rejected when their similarity score is below the required confidence level.

## Future Improvements

Possible future improvements include:

* Adding a graphical chat interface
* Expanding the FAQ dataset
* Using more advanced NLP techniques
* Adding semantic embeddings
* Adding conversation history
* Improving intent classification
* Adding voice input and output
* Deploying the chatbot as a web application

## Internship

This project was developed as part of the CodeAlpha Artificial Intelligence Internship.

**Task:** FAQ Chatbot — Task 2

## Author

Developed by Sagar as part of the CodeAlpha AI Internship.
