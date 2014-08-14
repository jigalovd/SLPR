# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Customer(models.Model):
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return "%s - %s" %(self.first_name, self.last_name)
    
    lp = models.CharField(primary_key=True, db_column='LP', unique=True, max_length=255) # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start_date', blank=True, null=True) # Field name made lowercase.
    end_date = models.DateTimeField(db_column='End_Date', blank=True, null=True) # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=255, blank=True) # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=255, blank=True) # Field name made lowercase.
    additional_info = models.CharField(db_column='Additional_Info', max_length=255, blank=True) # Field name made lowercase.
    photo = models.CharField(db_column='PHOTO', max_length=255, blank=True) # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True) # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True) # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True) # Field name made lowercase.
    number_of_spots = models.IntegerField(db_column='Number_Of_Spots', blank=True, null=True) # Field name made lowercase.
    c_spots = models.IntegerField(db_column='C_spots', blank=True, null=True) # Field name made lowercase.
    carspacenumber = models.CharField(db_column='CarSpaceNumber', max_length=100, blank=True) # Field name made lowercase.
    appartment = models.CharField(db_column='Appartment', max_length=100, blank=True) # Field name made lowercase.
    company_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    
    class Meta:
        
        db_table = 'customer'
