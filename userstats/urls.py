from django.urls import path

from userstats import views

urlpatterns = [
    path('expense_category_data', views.ExpenseSummaryView.as_view(), name="expense-category"),
    path('income_source_date', views.IncomeSummaryView.as_view(), name="income-source"),
]