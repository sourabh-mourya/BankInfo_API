from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer,BranchDetailSerializer


@api_view(['GET'])
def get_banks(request):
    banks = Bank.objects.all()
    serializer = BankSerializer(banks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_bank_branches(request, bank_id):
    try:
        bank = Bank.objects.get(bank_id=bank_id)
    except Bank.DoesNotExist:
        return Response({"error": "Bank not found"}, status=status.HTTP_404_NOT_FOUND)

    branches = bank.branches.all()  
    serializer = BranchSerializer(branches, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_branch_by_ifsc(request, ifsc):
    try:
        branch = Branch.objects.get(ifsc=ifsc)
    except Branch.DoesNotExist:
        return Response(    
            {"error": "Branch not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = BranchDetailSerializer(branch)
    return Response(serializer.data)
