from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^books$', views.books, name="books"),
    url(r'^categories$', views.categories, name="categories"),
    url(r'^students$', views.students, name="students"),
    url(r'^returning$', views.returning, name="returning"),
    url(r'^borrow$', views.borrow, name="borrow"),
    url(r'^edit_book/(\d+)/$', views.edit_book, name="edit_book"),
    url(r'^edit_category/(\d+)/$', views.edit_category, name="edit_category"),
    url(r'^delete_book/(\d+)/$', views.delete_book, name="delete_book"),
    url(r'^delete_student/(\d+)/$', views.delete_student, name="delete_student"),
    url(r'^delete_category/(\d+)/$', views.delete_category, name="delete_category"),
    url(r'^delete_borrow/(\d+)/$', views.delete_borrow, name="delete_borrow"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
