from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serilalizers import RegisterSerializer
from rest_framework.authtoken.models import Token

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token,created =Token.objects.get_or_create(user=user)
            return Response({'token':token.key},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


