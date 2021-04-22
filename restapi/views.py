from django.http import HttpResponse
from rest_framework.utils import json
from rest_framework.views import APIView
from .models import Quizdata,Questions
from .decoraters import controller_api



def index(request):
    return HttpResponse("Server running")
    
class Quizes(APIView):

    def get(self, request):
        quizes = Quizdata.objects.all()
        quizlist = [{"id":quiz.id, "name":quiz.name, "description":quiz.description} for quiz in quizes]
        return HttpResponse(json.dumps(quizlist), content_type="application/json",status=200)

    @controller_api
    def post(self, request):
        postdata = json.loads(request.body)
        name = postdata.get("name")
        description = postdata.get("description")
        quiz = Quizdata.objects.create(name=name, description=description)
        data = {"id":quiz.id, "name":quiz.name, "description":quiz.description}
        return HttpResponse(json.dumps(data), content_type="application/json", status=201)

class Quiz(APIView):

    @controller_api
    def get(self,request,pk):
        quiz = Quizdata.objects.filter(pk=pk)
        if not quiz:
            return HttpResponse(json.dumps({}), content_type="application/json",status=404)
        data = {"id":quiz[0].id, "name":quiz[0].name, "description":quiz[0].description}
        return HttpResponse(json.dumps(data), content_type="application/json",status=200)


class QuestionsAll(APIView):

      @controller_api
      def get(self,request,quiz_id):
          quiz = Quizdata.objects.filter(pk=quiz_id).first()
          if not quiz:
              return HttpResponse(json.dumps({}), content_type="application/json", status=404)
          questions = Questions.objects.filter(quiz=quiz_id)
          ques_list = [{"id": question.id,
                        "name": question.name,
                        "options": question.options,
                        "correct_option":question.correct_option,
                        "quiz":question.quiz.id,
                        "points":question.points} for question in questions]
          data = {"name": quiz.name,"description": quiz.description,"questions" :ques_list}
          return HttpResponse(json.dumps(data), content_type="application/json", status=200)


      @controller_api
      def post(self,request):
          postdata = json.loads(request.body)
          name = postdata.get("name")
          options = postdata.get("options")
          correctOption = postdata.get("correct_option")
          quiz = Quizdata.objects.filter(pk=postdata.get("quiz")).first()
          points = postdata.get("points")
          question = Questions.objects.create(name=name, options=options, correct_option= correctOption, quiz=quiz,points= points)
          data = {"id": question.id,
                  "name": question.name,
                  "options": question.options,
                  "correct_option": question.correct_option,
                  "quiz":quiz.id ,
                  "points":question.points}
          return HttpResponse(json.dumps(data), content_type="application/json", status=201)

class Question(APIView):

    @controller_api
    def get(self,request,question_id):
        question = Questions.objects.filter(pk=question_id).first()
        if not question:
            return HttpResponse(json.dumps({}), content_type="application/json",status=404)
        data = {"id": question.id,
                  "name": question.name,
                  "options": question.options,
                  "correct_option": question.correct_option,
                  "quiz":question.quiz.id ,
                  "points":question.points}
        return HttpResponse(json.dumps(data), content_type="application/json",status=200)