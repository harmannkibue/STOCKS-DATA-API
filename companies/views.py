# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializers

#lists all the stocks or create a new one
class StockList(APIView):

    def get(self,request):
        stocks = Stock.objects.all()
        serializer = StockSerializers(stocks, many=True)
        return Response(serializer.data)

    def post(self):
        pass



