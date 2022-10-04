from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView, status

from .content_serializer import ContentSerializer
from .models import Content


class ContentView(APIView):
    def post(self, request):

        serializer = ContentSerializer(**request.data)
        
        if serializer.data_validation():
            content = Content.objects.create(**serializer.data)

            contents_dict = model_to_dict(content)

            return Response(contents_dict, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    def get(self, request):
        contents = Content.objects.all()

        return_content = [model_to_dict(content) for content in contents]

        return Response(return_content)


class ContentDetailView(APIView):

    def get(self, request, content_id: int):
        
        try:
            content = Content.objects.get(id=content_id)

        except Content.DoesNotExist:
            return Response({"message": "Content not found"}, status.HTTP_404_NOT_FOUND)

        content_dict = model_to_dict(content)
        return Response(content_dict)

    def patch(self, request, content_id: int):
        try:
            content = Content.objects.get(id=content_id)
            
        except Content.DoesNotExist:
            return Response({"message": "Content not found"}, status.HTTP_404_NOT_FOUND)
        

        for key, value in request.data.items():
            setattr(content, key, value)
        
        content.save()
        content_dict = model_to_dict(content)
        
        return Response(content_dict, status.HTTP_200_OK)


    def delete(self, request, content_id: int):
        try:
            content = Content.objects.get(id=content_id)
            
        except Content.DoesNotExist:
            return Response({"message": "Content not found"}, status.HTTP_404_NOT_FOUND)

        content.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ContentFilterView(APIView):
    def get(self, request):

        content_title = request.query_params.get('title')

        contents = Content.objects.filter(title__iexact=content_title)

        return_contents = [model_to_dict(content) for content in contents]

        return Response(return_contents, status.HTTP_200_OK)
