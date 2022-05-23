from pyexpat import model
from statistics import mode
from tkinter import Y
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class AddStudent(models.Model):
    Gen = [('Male', 'Male'), ('Female', 'Female'), ]
    Level = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ]
    sys = [('MainStream', 'MainStream'), ('Credit', 'Credit')]
    stat = [('Active', 'Active'), ('InActive', 'InActive')]
    Dep = [('General', 'General'), ('BIO', 'BIO'), ('DS', 'DS'),
           ('CS', 'CS'), ('SE', 'SE'), ('IT', 'IT'),
           ('AI', 'AI'), ('IS', 'IS')
           ]

    FullName = models.CharField(max_length=200)
    StudentID = models.CharField(max_length=8, primary_key=True)
    Gpa = models.DecimalField(max_digits=5, decimal_places=2)
    Gender = models.CharField(max_length=10, choices=Gen)
    Birth = models.DateField()
    StudentLevel = models.CharField(max_length=1, choices=Level, default='1')
    Status = models.CharField(max_length=20, choices=stat, default='Active')
    System = models.CharField(max_length=20, choices=sys, default='MainStream')
    Department = models.CharField(max_length=500, choices=Dep, default='General')
    Email = models.EmailField(max_length=254)
    # Mobile =  PhoneField(blank=True, help_text='Contact phone number')
    Mobile = PhoneNumberField()

    def __str__(self):
        return self.FullName

    class Meta:
        verbose_name = 'Student'
        ordering = ['FullName']
                
class ContactUs(models.Model):
    FullName =models.CharField(max_length=200)
    Email = models.EmailField(max_length = 254)
    Mobile = PhoneNumberField()
    Message = models.TextField(max_length=5000)
    
    def __str__(self):
        return self.FullName
    
    class Meta:
        verbose_name = 'Contact'
        ordering = ['FullName']