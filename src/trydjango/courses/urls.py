"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import (
            CourseView,
            CourseListView,
            CourseCreateView,
            CourseUpdateView,
            CourseDeleteView,
            my_fbv,
            )


app_name = 'products'
urlpatterns = [
    # path('', CourseView.as_view(template_name='courses/about.html'), name='courses-list'), 
    path('', CourseListView.as_view(), name='courses-list'), 
    path('<int:my_id>/', CourseView.as_view(), name='courses-detail'), 
    path('create/', CourseCreateView.as_view(), name='courses-create'), 
    path('<int:my_id>/update/', CourseUpdateView.as_view(), name='courses-update'), 
    path('<int:my_id>/delete/', CourseDeleteView.as_view(), name='courses-delete'), 
    # path('', my_fbv, name='courses-list'),
]