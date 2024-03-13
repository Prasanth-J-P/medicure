from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import UserCreationForm
from storeroom.forms import DetailsForm
from .serializers import ProductSerializer
from storeroom.models import Medicinedetails


@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny],)
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("Account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def create_product(request):
    print(request.data)
    form = DetailsForm(request.data)
    if form.is_valid():
        product = form.save()
        return Response({'id': product.id}, status=status.HTTP_201_CREATED)
    print(form.errors)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny,])
def list_products(request):
    products = Medicinedetails.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny,])
def list_Medicine(request,pk):
    selected = get_object_or_404(Medicinedetails, pk=pk)
    serializer = ProductSerializer(selected)
    return Response(serializer.data)

@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated,])
def update_product(request, pk):
    product = get_object_or_404(Medicinedetails, pk=pk)
    form = DetailsForm(request.data, instance=product)
    if form.is_valid():
        form.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=HTTP_200_OK)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,])
def delete_product(request, pk):
    try:
        product = Medicinedetails.objects.get(pk=pk)
    except Medicinedetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response("Deleted successfully")

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def search_med(request, search):
  if search=='':
      return Response({'error':'Medicine not found'},status=status.HTTP_404_NOT_FOUND)
  product = Medicinedetails.objects.filter(name__icontains = search)
  if not product:
      return Response(status=status.HTTP_404_NOT_FOUND)
  serializer = ProductSerializer(product, many=True)
  return  Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def logoutapi(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)


