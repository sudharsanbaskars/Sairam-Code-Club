from django.urls import path,reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.home, name="home"),

	path('list_event/', views.EventListView.as_view(), name="event_list_view"),
	path('detail_event/<int:pk>/', views.EventDetailView.as_view(), name="event_detail_view"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)