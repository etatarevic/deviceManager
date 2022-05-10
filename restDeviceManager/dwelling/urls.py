from django.urls import path
from .views import dwelling, location

urlpatterns = [
    path('', dwelling.DwellingView.as_view(
            {
                "get":"list",
                "post":"create",
            }
        )),
    path('<slug:pk>/', dwelling.DwellingView.as_view(
            {
                "get":"retrieve",
                "patch":"partial_update",
                "put":"update",
                "delete":"destroy",
            }
        )),
    path('location', location.LocationView.as_view(
            {
                "get":"list",
                "post":"create",
            }
    )),
    path('location/<slug:pk>/', location.LocationView.as_view(
            {
                "get":"retrieve",
                "put":"update",
                "patch":"partial_update",
                "delete":"destroy",
            }
    )),
]