from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

import subprocess
from utils.constants import status_options, vulnerable_ports
from utils.terminal.nmap import parse_nmap_output, nmap_scan
from utils.terminal.zap import zap_scan, zap_results


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
        # Get URL from request data
        url = request.data.get("url")

        # Check if URL is provided
        if not url:
            return Response(
                {"error": "URL is required"},
                status=HTTP_400_BAD_REQUEST
            )

        # Perform scans
        nmap_result = nmap_scan(url)
        zap_scan(url)
        zap_result = zap_results()

        # Check if nmap scan was successful
        if nmap_result is None:
            return Response(
                {"error": "Failed to execute nmap scan"},
                status=HTTP_400_BAD_REQUEST
            )

        # Check if Zap scan was successful
        if zap_result is None:
            return Response(
                {"error": "Failed to execute zap scan"},
                status=HTTP_400_BAD_REQUEST
            )

        # Combine results into a single dictionary
        data = {
            "nmap": nmap_result.data if hasattr(nmap_result, 'data') else None,
            "zap": zap_result.data if hasattr(zap_result, 'data') else None
        }

        return Response(data, status=HTTP_200_OK)

    