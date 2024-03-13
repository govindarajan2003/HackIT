from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

class UserView(APIView):
    def get(self, request):
        command_id = request.get("id", None)
        if command_id: 
            return Response({
            "zap":"zap.sh -quickout",
            "nmap":"nmap ",
            "status":HTTP_200_OK,

        })
        else:
            return Response({
                "status":HTTP_400_BAD_REQUEST,
            })
        
        return Response({
            "zap":"zap.sh -quickout",
            "nmap":"nmap "
        })
    