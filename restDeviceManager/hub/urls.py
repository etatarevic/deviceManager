from django.urls import path
from . import views

urlpatterns = [
    path('', views.HubView.as_view(
            {
                "get":"list",
                "post":"create",
            }
        )),
    path('<slug:pk>/', views.HubView.as_view(
            {
                "get":"retrieve",
                "put":"update",
                "patch":"partial_update",
                "delete":"destroy"
            }
        )),
]