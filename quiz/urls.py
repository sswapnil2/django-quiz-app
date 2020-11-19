from django.urls import re_path
from .views import QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake, index, login_user, logout_user

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^login/$', login_user, name='login'),
    re_path(r'^logout/$', logout_user, name='logout'),
    re_path(r'^quizzes/$', QuizListView.as_view(), name='quiz_index'),
    re_path(r'^category/$', CategoriesListView.as_view(), name='quiz_category_list_all'),
    re_path(r'^category/(?P<category_name>[\w|\W-]+)/$', ViewQuizListByCategory.as_view(), name='quiz_category_list_matching'),
    re_path(r'^progress/$', QuizUserProgressView.as_view(), name='quiz_progress'),
    re_path(r'^marking/$', QuizMarkingList.as_view(), name='quiz_marking'),
    re_path(r'^marking/(?P<pk>[\d.]+)/$', QuizMarkingDetail.as_view(), name='quiz_marking_detail'),
    #  passes variable 'quiz_name' to quiz_take view
    re_path(r'^(?P<slug>[\w-]+)/$', QuizDetailView.as_view(), name='quiz_start_page'),
    re_path(r'^(?P<quiz_name>[\w-]+)/take/$', QuizTake.as_view(), name='quiz_question'),
]
