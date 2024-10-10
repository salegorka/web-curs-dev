from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    path("logout_page", views.logout_page, name="logout_page"),
    re_path(r"^reqs/new$", views.NewReqListView.as_view(), name="new_reqs"),
    re_path(r"^reqs/wait$", views.WaitReqListView.as_view(), name="wait_reqs"),
    re_path(r"^reqs/signed$", views.SignReqListView.as_view(), name="sign_reqs"),
    re_path(r"^reqs/done$", views.DoneReqListView.as_view(), name="done_reqs"),
    re_path(r"^req/(?P<pk>\d+)$", views.ReqDetailView.as_view(), name="req-detail"),
    re_path(r"^req/(?P<pk>\d+)/statuschange$", views.status_change,  name="status_change")
]
