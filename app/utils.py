from typing import List
from app.api.lessons.models import Lesson
from app.api.questions.models import QuestionType

def calculate_lesson_score(lesson: Lesson, answers: List[str]) -> int:
    score = 0
    for question, answer in zip(lesson.questions, answers):
        if question.type == QuestionType.BOOLEAN or question.type == QuestionType.MULTIPLE_CHOICE_ONE:
            if answer in question.correct_answers:
                score += question.score
        elif question.type == QuestionType.MULTIPLE_CHOICE_MULTIPLE:
            if set(answer) & set(question.correct_answers):
                score += question.score
        elif question.type == QuestionType.MULTIPLE_CHOICE_ALL_CORRECT:
            if set(answer) == set(question.correct_answers):
                score += question.score
    return score
