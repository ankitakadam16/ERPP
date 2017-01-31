from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import *
from .models import *
from gitweb.serializers import repoLiteSerializer
from ERP.serializers import serviceSerializer
from ERP.models import service
from projects.models import project
from projects.serializers import projectLiteSerializer
from datetime import datetime

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('pk', 'created' , 'number' , 'ifsc' , 'bank'  , 'bankAddress' , 'contactPerson' , 'authorizedSignaturies')

class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = ('head' , 'name' , 'code' , 'created' , 'account' , 'projects')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('pk', 'fromAcc' , 'toAcc' , 'ammount' , 'user' , 'balance')


class InvoiceSerializer(serializers.ModelSerializer):
    service = serviceSerializer(many = False , read_only = True)
    class Meta:
        model = Invoice
        fields = ('pk', 'user' , 'created' , 'service' , 'amount' , 'currency' , 'dated' , 'attachment' , 'sheet', 'description', 'approved')
        read_only_fields = ('user',)

    def create(self , validated_data):
        u = self.context['request'].user
        print 'came to create an Invoce' , u
        inv = Invoice(**validated_data)
        inv.user = u
        inv.service = service.objects.get(pk = self.context['request'].data['service'])
        inv.approved = False
        inv.save()
        return inv

    def update(self, instance, validated_data):
        # if the user is manager or something then he can update the approved flag
        instance.service = service.objects.get(pk = self.context['request'].data['service'])
        reqData = self.context['request'].data
        dateStr = reqData['dated']
        instance.dated = datetime.strptime(dateStr, '%Y-%m-%d').date()
        print service.objects.get(pk = reqData['service'])
        instance.service = service.objects.get(pk = reqData['service'])
        for f in ['amount' , 'currency' , 'sheet' , 'description']:
            setattr(instance , f , validated_data.pop(f))
        if 'attachment' in reqData:
            instance.attachment = validated_data.pop('attachment')
        instance.save()
        print instance.service
        return instance


class ExpenseSheetSerializer(serializers.ModelSerializer):
    invoices = InvoiceSerializer(many = True , read_only = True)
    project = projectLiteSerializer(many = False , read_only = True)
    class Meta:
        model = ExpenseSheet
        fields = ('pk','user' , 'created' , 'approved' , 'approvalMatrix' , 'approvalStage' , 'dispensed' , 'notes' , 'project' , 'transaction', 'invoices', 'submitted')
        read_only_fields = ('transaction', 'invoices', 'user', 'project' )
    def create(self , validated_data):
        u = self.context['request'].user
        reqData = self.context['request'].data
        es = ExpenseSheet(**validated_data)
        es.approvalStage = 0
        if 'project' in reqData:
            es.project = project.objects.get(id = int(reqData['project']))
        else:
            raise ValidationError(detail= 'project ID not found')
        es.dispensed = False
        es.submitted = False
        es.user = u
        es.save()
        return es
    def update(self , instance , validated_data):
        print 'came'
        reqData = self.context['request'].data
        if 'notes' in reqData:
            instance.notes = validated_data.pop('notes')
        if 'project' in reqData:
            instance.project = project.objects.get(pk = int(reqData['project']))
        if instance.user == self.context['request'].user and 'submitted' in reqData:
            if not instance.submitted:
                instance.submitted = True
        instance.save()
        return instance
