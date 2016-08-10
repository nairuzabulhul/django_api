Add authentication to Django API



1- Add Authentication to the settings.py

    'rest_framework.authtoken',

2- in serializer.py Import User Authentication 

  from django.contrib.auth.models import User
  
  Add owner to the BookSerializer
  
    owner = serializers.ReadOnlyField(source='owner.username')


3-Add the Authentication url link:

  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  
  
4- In models.py  add the owner to the class

    owner = models.ForeignKey('auth.User', related_name='books', default=1)
    
    
5- In the views.py, import rest_framework permissions:

    from rest_framework import permissions
    

6- Add permission_classes to the the views

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

7- Add pre_save function to the class views:

    def pre_save(self, obj):
        obj.owner = self.request.username
    
    