from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from MembershipApp.models import Members
from MembershipApp.serializers import MemberSerializer

@csrf_exempt

def MembershipApi(request, id=0):
  if request.method=='GET':
      member_data = JSONParser().parse(request)
      member = Members.objects.get(MemberId=member_data['MemberId'])
      print(member.MemberCountry)
      # member_serializer = MemberSerializer(data=member)
      if member.MemberCountry:
          return JsonResponse("This is a valid member ID.")
      return JsonResponse("This is not a valid member ID.")
  elif request.method=='POST':
      member_data = JSONParser().parse(request)
      member_serializer = MemberSerializer(data=member_data)
      if member_serializer.is_valid():
          member_serializer.save()
          return JsonResponse("Membership was created successfully",safe=False)
      return JsonResponse("We ran into a problem while creating your membership, please contact here.",safe=True)
