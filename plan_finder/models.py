from __future__ import unicode_literals

from django.db import models

import csv

class LoadedModel(models.Model):

    class Meta:
        abstract = True

    @classmethod
    def load_from_csv(cls, file_path):
        with open(file_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                cls.objects.create(**row)

class Region(LoadedModel):

    zip_code = models.IntegerField()
    region = models.IntegerField()

class Price(LoadedModel):

    carrier = models.CharField(max_length=255)
    plan = models.CharField(max_length=255)  # foreign key
    region = models.IntegerField()  # One to Many
    age = models.IntegerField()
    monthly_premium = models.DecimalField(decimal_places=2, max_digits=10)

    def get_plan(self):
        return Plan.objects.get(carrier=self.carrier, name=self.plan)

class Plan(LoadedModel):
    carrier = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ambulance = models.CharField(max_length=255)
    application_fee = models.CharField(max_length=255)
    baby_care = models.CharField(max_length=255)
    brand_drugs = models.CharField(max_length=255)
    chiropractic = models.CharField(max_length=255)
    coinsurance = models.CharField(max_length=255)
    deductible = models.CharField(max_length=255)
    emergency_room = models.CharField(max_length=255)
    generic_drugs = models.CharField(max_length=255)
    hospitalization = models.CharField(max_length=255)
    hsa_eligible = models.CharField(max_length=255)
    labor = models.CharField(max_length=255)
    lifetime_maximum = models.CharField(max_length=255)
    mail_order_drugs = models.CharField(max_length=255)
    mental_health = models.CharField(max_length=255)
    obgyn_exam = models.CharField(max_length=255)
    oon_authorization = models.CharField(max_length=255)
    oon_coinsurance = models.CharField(max_length=255)
    oon_coverage = models.CharField(max_length=255)
    oon_deductible = models.CharField(max_length=255)
    oon_oop_limit = models.CharField(max_length=255)
    oop_limit = models.CharField(max_length=255)
    out_of_country = models.CharField(max_length=255)
    pcp_required = models.CharField(max_length=255)
    pcp_visit = models.CharField(max_length=255)
    periodic_exam = models.CharField(max_length=255)
    plan_type = models.CharField(max_length=255)
    prenatal_office_visit = models.CharField(max_length=255)
    separate_rx_deductible = models.CharField(max_length=255)
    specialist_referrals_required = models.CharField(max_length=255)
    specialist_visit = models.CharField(max_length=255)
    specialty_drugs = models.CharField(max_length=255)
    substance_abuse = models.CharField(max_length=255)
    surgery = models.CharField(max_length=255)
    urgent_care = models.CharField(max_length=255)
    xray = models.CharField(max_length=255)
