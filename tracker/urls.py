from django.urls import path
from .views import (
    SignupView, LoginView,
    AssignmentCreateView,
    SubmissionCreateView,
    SubmissionListView
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),

    path('assignments/', AssignmentCreateView.as_view(), name='create-assignment'),
    path('assignments/<int:assignment_id>/submit/', SubmissionCreateView.as_view(), name='submit-assignment'),
    path('assignments/<int:assignment_id>/submissions/', SubmissionListView.as_view(), name='view-submissions'),
]


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
