#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

app_label = u'运费统计'

class Group(models.Model):
    group_name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = u"销售分组"
        
    def __unicode__(self):
        return self.group_name

class Project(models.Model):
    staff = models.ForeignKey(Group)
    proj_name = models.CharField(max_length=30)
    item_name = models.CharField(max_length=30)
    distance = models.FloatField()
    date = models.DateField()
    
    class Meta:
        verbose_name_plural = u"工程项目"
    
    def __unicode__(self):
        return self.prog_name
    
class Transport(models.Model):
    PRODUCT_TYPE = (
                ('A','C30'),
                ('B','C25'),
    )
    License_Num = (
                (u'公司车','83377'),
                (u'XX车队','8888'),
    )
    lpn = models.CharField(max_length=10,choices=License_Num)
    proj = models.ForeignKey(Project)
    date = models.DateField()
    type = models.CharField(max_length=1,choices=PRODUCT_TYPE)
    driver = models.CharField(max_length=30)
    quantity = models.FloatField()
    dis_mod = models.FloatField(default=0.0,blank=True)
    timeout = models.IntegerField(default=0,blank=True)
    price = models.FloatField()
    
    class Meta:
        verbose_name_plural = u"运输单"
    
    def __unicode__(self):
        return self.lpn
    
