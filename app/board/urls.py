from django.urls import path
from .handlers import (main, feed, auth, dashboard, figure)


urlpatterns = [
    path('', main.feed_redirect, name='main'),
    path('feed/', feed.list_dashboards, name='feed'),
    path('signout/', auth.sign_out, name='signout'),
    path('signin/', auth.sign_in, name='signin'),
    path('signup/', auth.sign_up, name='signup'),
    path('dashboards/', dashboard.show_dashboards, name='dashboards'),
    path('dashboards/create_dashboard/', dashboard.create_dashboard),
    path('p/<int:dashboard_id>/', dashboard.view_dashboard, name='view_by_id'),
    path('<int:dashboard_id>/', dashboard.get_dashboard, name='dashboard_by_id'),
    path('<int:dashboard_id>/add_description', dashboard.add_description, name='add_description'),
    path('<int:dashboard_id>/add_figure', figure.add_figure, name='add_figure')
]
