from django.urls import path
from . import views


urlpatterns = [
    path('dashboards', views.show_dashboards, name='dashboards'),
    path('create_dashboard', views.create_dashboard),
    path('<int:dashboard_id>/', views.get_dashboard, name='dashboard_by_id'),
    path('<int:dashboard_id>/add_figure', views.add_figure, name='add_figure')
    # path('<int:dashboard_id>/parse_theme', views.parse_theme, name='parse_theme')
]
