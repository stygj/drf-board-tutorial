# 데이터 처리
from .models import Blog
from .serializers import BlogSerializer

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class BlogList(APIView):
    
    # Blog의 목록을 보기
    # response sample : [{"title": "안녕","body": "반가워"}]
    def get(self,request):
        blogs = Blog.objects.all() # 쿼리 작성 부
        serializer = BlogSerializer(blogs, many=True) # 쿼리 결과 json
        return Response(serializer.data)
    
    # Blog 글 작성
    # request sample : {"title":"안녕", "body":"반가워"}
    # response sample : [{"title": "안녕","body": "반가워"}]
    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetail(APIView):

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk) 
        except Blog.DoesNotExist:
            raise Http404

    # Blog 글 상세보기
    # http://localhost:5050/blog/1
    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    # Blog 글 수정하기
    # request sample : {"title":"안녕", "body":"반가워용"}
    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Blog 글 삭제하기
    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

