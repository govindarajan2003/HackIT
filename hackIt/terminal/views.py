from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED



class TerminalView(APIView):

    def get(self, request):
        command_id = request.data.get("id", None)
        
        data = None
        status = HTTP_400_BAD_REQUEST
        if command_id:
            data = {
                "zap": "zap.sh -quickout",
                "nmap": "nmap ",
            }
            status = HTTP_200_OK
        
        else:
            status = HTTP_400_BAD_REQUEST
        
        return Response(
            data = data,
            content_type = "application/json",
            status = status
        )
    def post(self, request):
        url = request.data.get("url", None)
        
        data = None
        status = HTTP_400_BAD_REQUEST
        if url:
            data = {
                "zap": "zap.sh -quickout",
                "nmap": "nmap ",
            }
            status = HTTP_200_OK
        
        else:
            status = HTTP_400_BAD_REQUEST
        
        return Response(
            data = data,
            content_type = "application/json",
            status = status
        )
