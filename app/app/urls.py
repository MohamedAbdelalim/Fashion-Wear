from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from demo.views import index ,MyTokenObtainPairSerializer
from demo.views import registerPage, loginPage, logoutUser, product, checkout

urlpatterns = [
    path('', index,name='index'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('demo.urls')),

    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('product/', product, name='product'),
    path('checkout/', checkout, name='checkout'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
