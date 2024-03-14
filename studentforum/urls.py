from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    path("logout_page", views.logout_page, name="logout_page"),
    re_path(r"^newreqs/$", views.NewReqListView.as_view(), name="new_reqs"),
    re_path(r"^req/(?P<pk>\d+)$", views.ReqDetailView.as_view(), name="req-detail")
]
