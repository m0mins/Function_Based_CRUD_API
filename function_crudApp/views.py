# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer



@api_view(['POST'])
def createfunc(request):
    obj=TodoSerializer(data=request.data)
    if obj.is_valid():
        obj.save()
        return Response(obj.data,status=status.HTTP_201_CREATED)
    return Response(obj.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getStudents(request):
    obj=Todo.objects.all()
    seobj=TodoSerializer(obj,many=True)
    return Response(seobj.data)
@api_view(['GET'])
def getStudent(request,pk):
    tt=Todo.objects.get(pk=pk)
    ttt=TodoSerializer(tt)
    return Response(ttt.data)

@api_view(['PUT'])
def update_todo(request,pk):
    tt=Todo.objects.get(pk=pk)
    ttt=TodoSerializer(tt,data=request.data)
    if ttt.is_valid():
        ttt.save()
        return Response({"Message":"Updated Successfully","Updated Data":ttt.data})
    return Response({"Error":ttt.errors,"Status":status.HTTP_400_BAD_REQUEST})

@api_view(['DELETE'])
def delete_todo(request,pk):
    tt=Todo.objects.get(pk=pk)
    tt.delete()
    return Response({"Message":"Delete Successfully"})



#Same task in organized way

@api_view(['GET'])
def get_all_objects(request):
    objects = Todo.objects.all()
    serializer = TodoSerializer(objects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_object(request, pk):
    try:
        obj = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(obj)
    return Response(serializer.data)

@api_view(['POST'])
def create_object(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_object(request, pk):
    try:
        obj = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_object(request, pk):
    try:
        obj = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

