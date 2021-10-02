from django.db import models
import uuid

class Members(models.Model):
  MemberId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  MemberFirstName = models.CharField(max_length=500)
  MemberLastName = models.CharField(max_length=500)
  MemberDateOfBirth = models.DateField()
  MemberCountry = models.CharField(max_length=500)

