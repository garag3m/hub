from rest_framework.test import force_authenticate, APIRequestFactory
from .models import UUIDUser
from .views import UUIDUserViewSet

print('oi')
factory = APIRequestFactory()
print('oi')
user = UUIDUser.objects.get(username='admin')
print('oi')
view = UUIDUserViewSet.as_view({'get': 'list'})
print('oi')

# Make an authenticated request to the view...
request = factory.get('/user/', format='json')
force_authenticate(request, user=user)
response = view(request)
print(response)
