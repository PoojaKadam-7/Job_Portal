from django.contrib import admin
from django.urls import path
from job import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('view_users/', views.view_users, name='view_users'),
    path('user_login/', views.user_login, name='user_login'),
    path('recruiter_login/', views.recruiter_login, name='recruiter_login'),
    path('recruiter_home/', views.recruiter_home, name='recruiter_home'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_home/', views.user_home, name='user_home'),
    path('lastest_jobs/', views.lastest_jobs, name='lastest_jobs'),
    path('user_latestjobs/', views.user_latestjobs, name='user_latestjobs'),
    path('Logout/', views.Logout, name='Logout'),
    path('contact/', views.contact, name='contact'),
    path('add_job/', views.add_job, name='add_job'),
    path('job_list/', views.job_list, name='job_list'),
    path('applied_candidate/', views.applied_candidate, name='applied_candidate'),
    path('change_logo/<int:pid>', views.change_logo, name='change_logo'),
    path('applyforjob/<int:pid>', views.applyforjob, name='applyforjob'),
    path('job_detail/<int:pid>', views.job_detail, name='job_detail'),
    path('edit_jobdetails/<int:pid>', views.edit_jobdetails, name='edit_jobdetails'),
    path('delete_user/<int:pid>', views.delete_user, name='delete_user'),
    path('delete_recruiter/<int:pid>', views.delete_recruiter, name='delete_recruiter'),
    path('change_status/<int:pid>', views.change_status, name='change_status'),
    path('recruiter_pending', views.recruiter_pending, name='recruiter_pending'),
    path('recruiter_accepted', views.recruiter_accepted, name='recruiter_accepted'),
    path('recruiter_rejected', views.recruiter_rejected, name='recruiter_rejected'),
    path('recruiter_all', views.recruiter_all, name='recruiter_all'),
    path('Change_passwordadmin', views.Change_passwordadmin, name='Change_passwordadmin'),
    path('Change_passworduser', views.Change_passworduser, name='Change_passworduser'),
    path('Change_passwordrecruiter', views.Change_passwordrecruiter, name='Change_passwordrecruiter'),
    path('recruiter_signup/', views.recruiter_signup, name='recruiter_signup'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)