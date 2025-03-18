from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FirstnameSerializer
from modelApp.models import Firstname

# @api_view (['GET'])
# def getData (request):
#     person = {
#         'firstname' : 'Dr Manhattan'
#     }
#     return Response (person)

@api_view (['GET'])
def getData (request):
    firstname = Firstname.objects.all ()
    serializer = FirstnameSerializer (firstname, many=True)
    return Response (serializer.data)

@api_view (['POST'])
def postData (request):
    serializer = FirstnameSerializer (data=request.data)
    if serializer.is_valid ():
        serializer.save ()
    return Response (serializer.data)


# @api_view (['POST'])
# def postData (request):
#     firstname = request.data ['firstname']
#     output = {'output' : firstname}
#     return Response (output)