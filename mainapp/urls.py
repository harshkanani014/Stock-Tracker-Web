from django.urls import path
from . import views

urlpatterns = [
    path('', views.stockPicker, name="StockPicker"),
    path('stock-tracker', views.stockTracker, name="StockTracker")
]