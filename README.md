# Instructions for Use

## Local Run
You can run this program locally using `local_app.py`. Before running it, you need to create a virtual environment. You can use `pipenv` or `venv`. The following steps use `venv`, which is a more general method and requires less configuration.

1. Create a virtual environment:
    ```sh
    python3.10 -m venv scholar_control
    ```

2. Activate the virtual environment:
    - On Unix or MacOS:
      ```sh
      source scholar_control/bin/activate
      ```
    - On Windows:
      ```sh
      scholar_control\Scripts\activate
      ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python3.10 local_app.py
    ```

## Docker Run
1. Build the Docker image:
    ```sh
    docker build -t fastapi-app .
    ```

2. Run the Docker container:
    ```sh
    docker run -d -p 8000:8000 fastapi-app
    ```

## How to Use

Visit the following link to see the documentation: [API Docs](http://127.0.0.1:8000/api/v1/scholar_control/docs)
```

This is the requirement for the project

E-Learning API
You are required to develop an API for e-learning courses. The purpose of the tool is:
- For the Professors: to manage the courses configuration and performance reviews
- For the Students, to take courses using our frontend.

Our PM is a very busy person. We don't have detailed tasks, but only business rules to work with, which are:

- We have courses that contain lessons, and lessons that contain questions
- The courses are correlative with previous ones
- The lessons are correlative with previous ones
- The questions for each lesson have no correlation
- All questions for a lesson are mandatory
- Each question has a score
- Each lesson has an approval threshold to be considered "Approved".
- The threshold is calculated using the sum of correctly answered questions for that lesson.
- A course is approved when all lessons are passed.
- There's no restriction on accessing approved courses
- Only professors can create and manage courses, lessons and questions
- Any student can take a course

Initially, we'll need to support these types of questions:
- Boolean
- Multiple choice when only one answer is correct
- Multiple choice when more than one answer is correct
- Multiple choice when more than one answer is correct and all of them must be answered correctly

Our Frontend dev specifically asked for these endpoints for the students to use:
- Get a list of all courses, telling which ones the student can access
- Get lessons for a course, telling which ones the student can access
- Get lesson details for answering its questions Take a lesson (to avoid several requests, they asked to send all answers in one go)
- Basic CRUD for courses, lessons and questions

Codebase rules:
- There must be a readme file documenting installation and usage.
- You can use any frameworks and libraries you want, but they must be included in the readme file documenting its purpose and a brief explanation with the reasoning for your choice.
