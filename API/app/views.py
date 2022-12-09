from django.shortcuts import render
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import EmDetailsSer

# Create your views here.
class Emp(APIView):
    def get(self,request):
        Emp_Details= Employee.objects.all()
        serobj = EmDetailsSer(Emp_Details,many=True)
        return Response(serobj.data)

    def post(self,request):
        serobj=EmDetailsSer(data=request.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.data,status=status.HTTP_400_BAD_REQUEST)



class EmpUpdateDelete(APIView):
    def put(self,request,pk):
        emp=Employee.objects.get(pk=pk)
        print(emp)
        serobj=EmDetailsSer(emp,data=request.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        empobj=Employee.objects.get(pk=pk)
        empobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
