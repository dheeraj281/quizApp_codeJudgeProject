from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="home"),
    path("api/quiz/", views.Quizes.as_view(), name="quizall"),
    path("api/quiz/<int:pk>",views.Quiz.as_view(),name="quiz"),
    path("api/questions/",views.QuestionsAll.as_view(), name="questions" ),
    path("api/quiz-questions/<int:quiz_id>",views.QuestionsAll.as_view(), name="questionsperquiz" ),
    path("api/questions/<int:question_id>", views.Question.as_view(), name="questionbyID")
]
