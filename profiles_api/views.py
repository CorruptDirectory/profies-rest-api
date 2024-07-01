from rest_framework.views import APIView
from rest_framework.response import Response

# Django ootab, et APIView tagastaks Response objekti

class HelloApiView(APIView):
    """TestAPI View
    You define a url (endpoint),
     then you assign this to a view,
      and djr handles it by calling appropriate
       function in a view for HTTP request that you made.
    """
    
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as funtion (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Cnock cnock...', 'an_apiview': an_apiview})