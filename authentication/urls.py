
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from authentication.views import SignUpView, OnBoardingView

router = DefaultRouter()
router.register(r'onboarding', OnBoardingView, basename='onboarding')
router.register(r'signup', SignUpView, basename='signup')

urlpatterns = [
    path('', include(router.urls)),
]


