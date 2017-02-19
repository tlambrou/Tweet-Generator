# Tweet Generator: Data Structures & Probability with Python

## Course Schedule

**Course Dates:** Monday, January 23 – Friday, March 3, 2017 (6 weeks)

**Class Times:** Tuesday & Thursday 1–3pm (12 class sessions)


### Class 1: Tuesday, January 24

**Activity:**
- Discuss course goals and project focus
- Compare Python to other programming languages

**Tutorial:**
- Page 1: Let’s Get Started
- Page 2: Random Dictionary Words

**Objectives:**
- Create Python scripts and modules
- Access command-line arguments
- Read files and extract lines of text
- Strip whitespace from strings


### Class 2: Thursday, January 26

**Activity:**
- Compare code quality for list shuffling function
- Interactive code quiz on Python scripts and modules

**Tutorial:**
- Page 3: Analyze Word Frequency in Text

**Objectives:**
- Split strings into components to find words
- Build a histogram to count word occurrences


### Class 3: Tuesday, January 31

**Activity:**
- Compare code quality for getting random dictionary words

**Tutorial:**
- Page 4: Stochastic Sampling

**Objectives:**
- Sample words according to their observed frequencies
- Compare tradeoffs with different sampling techniques


### Class 4: Thursday, February 2

**Activity:**
- Compare tradeoffs of different histogram implementations
- Probability lecture and discussion

**Tutorial:**
- Page 5: Flask Web App

**Objectives:**
- Build Flask web app on your computer
- Deploy Flask app to Heroku server


### Class 5: Tuesday, February 7

**Activity:**
- Compare implementations for sampling words based on observed frequency

**Tutorial:**
- Page 6: Application Architecture (part 1)

**Objectives:**
- Plan application architecture to prepare for future expansion


### Class 6: Thursday, February 9

**Activity:**
- Compare code quality of functions based on length and responsibility
- Unpack list comprehensions into equivalent code and compare trade offs

**Tutorial:**
- Page 6: Application Architecture (part 2)

**Objectives:**
- Refactor histogram functions as class instance methods


### Class 7: Tuesday, February 14

**Activity:**
- Markov chains and random walks lecture and discussion

**Tutorial:**
- Page 7: Generating Sentences

**Objectives:**
- Build Markov chain based on observed frequency of adjacent words
- Generate sentence by sampling words using random walk through Markov chain


### Class 8: Thursday, February 16

**Activity:**
- Act out how dynamic arrays and linked lists work
- Review slides on [arrays and linked lists](ArraysLinkedLists.pdf)

**Tutorial:**
- Page 8: Linked List

**Objectives:**
- Implement LinkedList class using [starter code](templates/linkedlist.py) and [unit tests](templates/test_linkedlist.py)


## Working with this GitHub repository

This repository (located at `https://github.com/MakeSchool-18/Tweet-Generator`) is the course's _origin_ repository which will contain course materials including links, slides, and challenges.
Note that you cannot commit or push to the origin repository.
However, you can _fork_ it to maintain your own version of it and push your code there. Here's an overview of what your repository setup should look like:

![Repository Overview](repository-overview.png "Repository Overview")

Follow these steps to set up your own course repository:

1. Clone this repository on your computer:
`git clone git@github.com:MakeSchool-18/Tweet-Generator.git`

2. Fork this repository on GitHub to create your own version of this repo on your GitHub account, which should also be named `Tweet-Generator`

3. Add your GitHub repository as a _remote_ to the local one on your computer (note: you need to give a name to the remote, e.g. your first name):
`git remote add <first-name> git@github.com:<github-user>/Tweet-Generator.git`

4. Link the local repo to your remote GitHub repo:
`git push -u <first-name> master`

5. When you want to access new course materials, just pull from the origin remote repo:
`git pull origin master`

6. When you've completed a challenge and want to share it for code review, commit your work and push it to your own remote repo with:
`git push`
