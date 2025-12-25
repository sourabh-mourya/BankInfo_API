from rest_framework import serializers
from .models import Bank, Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['ifsc', 'branch',]

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['bank_id', 'name']



class BranchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['ifsc', 'branch', 'address', 'city', 'district', 'state', 'bank']