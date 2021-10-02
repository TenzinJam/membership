from rest_framework import serializers
from MembershipApp.models import Members

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Members
        fields=('MemberId', 'MemberFirstName', 'MemberLastName', 'MemberDateOfBirth', 'MemberCountry' )

