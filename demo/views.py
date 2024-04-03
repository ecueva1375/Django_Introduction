from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer, BookMiniSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

# class Another(View):
#
#     #books = Book.objects.all()
#     #books = Book.objects.filter(is_published=True)
#     book = Book.objects.get(id=1)
#     # output = f"We have {len(books)} books in DB"
#     #output = ''
#     output = f"We have {book.title} book with ID {book.id} <br>"
#
#     #for book in books:
#         #output += f"We have {book.title} book with ID {book.id} <br>"
#
#
#     def get(self, request):
#         return HttpResponse(self.output)


# def first(request):
#     #  return HttpResponse('First message from views')
#     #return HttpResponse('First message from views')
#     books = Book.objects.all()
#     return render(request, 'first_temp.html', {'books': books})

class BookVieSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)