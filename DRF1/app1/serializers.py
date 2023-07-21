from rest_framework import serializers
from app1.models import Employee

def outside_validation(value):
    if value % 1000 != 0:
        raise serializers.ValidationError('The salary should be multiples of 1000\'s')

class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=64)
    esal = serializers.FloatField(validators=[outside_validation])
    eaddr = serializers.CharField(max_length=64)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.eno = validated_data.get('eno', instance.eno)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.esal = validated_data.get('esal', instance.esal)
        instance.eaddr = validated_data.get('eaddr', instance.eaddr)
        instance.save()
        return instance

    # def validate_esal(self, value):
    #     if value < 25000:
    #         raise serializers.ValidationError('the salary should be more than 25000')
    #     return value

    # def validate(self, data):
    #     ename = data.get('ename')
    #     esal = data.get('esal')
    #     if ename == 'sita':
    #         if esal < 30000:
    #             raise serializers.ValidationError('check the details perfectly..once again')
    #     return data

