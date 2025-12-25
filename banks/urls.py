from django.urls import path
from .views import (
    get_banks,
    get_bank_branches,
    get_branch_by_ifsc
)

urlpatterns = [
    path('banks/', get_banks),
    path('banks/<int:bank_id>/branches/', get_bank_branches),
    path('branches/<str:ifsc>/', get_branch_by_ifsc),
]
