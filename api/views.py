from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from .models import stock_market as StockData
from .serializers import DataSerializer
import os
# Create your views here.
def index(request):
    return HttpResponse("Welcome to the stock market API!")

@csrf_exempt
def stockData(request, id=None):
    
    if request.method == "GET":
        # Retrieve single data by ID
        
        if id is not None:
            try:
                data = StockData.objects.get(id=id)
                serializer = DataSerializer(data)
                return JsonResponse(serializer.data)
            except StockData.DoesNotExist:
                return JsonResponse({"error": "Data not found"}, status=404)

        # Retrieve all data
        data = StockData.objects.all()
        serializer = DataSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        request_data =JSONParser().parse(request)
        serializer = DataSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Data added successfully"}, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "PATCH":
        if id is not None:
            try:
                instance = StockData.objects.get(id=id)
            except StockData.DoesNotExist:
                return JsonResponse({"error": "Data not found"}, status=404)
            request_data =JSONParser().parse(request)
            serializer = DataSerializer(instance, data=request_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Data update successfully"},status=200)
            return JsonResponse(serializer.errors, status=404)
        else:
            return JsonResponse({"error": "ID parameter is missing"}, status=400)

    elif request.method == "PUT":
        if id is not None:
            try:
                instance = StockData.objects.get(id=id)
            except StockData.DoesNotExist:
                return JsonResponse({"error": "Data not found"}, status=404)
            request_data =JSONParser().parse(request)
            serializer = DataSerializer(instance, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Data update successfully"},status=200)
            return JsonResponse(serializer.errors, status=404)
        else:
            return JsonResponse({"error": "ID parameter is missing"}, status=400)
        

    elif request.method == "DELETE":
        # Delete data by ID
        if id is not None:
            try:
                data = StockData.objects.get(id=id)
                data.delete()
                return JsonResponse({"message": "Data deleted successfully"}, status=204)
            except StockData.DoesNotExist:
                return JsonResponse({"error": "Data not found"}, status=404)
        else:
            return JsonResponse({"error": "ID parameter is missing"}, status=400)
