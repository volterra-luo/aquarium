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
        return self.proj_name
    
class Tanker(models.Model):
    License_Num_Belong = {"83377":u"公司车",
                          "83399":u"公司车",
                          "69783":u"段总"}
    lpn = models.CharField(max_length=10,verbose_name=u"车牌号")
    
    def _category(self):
        return self.License_Num_Belong[self.lpn]
    _category.short_description = u"属于哪个车队?"
    belong = property(_category)
    
    class Meta:
        verbose_name_plural = u"罐车"
        
    def __unicode__(self):
        return self.lpn
    
class Product(models.Model):
    type = models.CharField(max_length=10)
    
    class Meta:
        verbose_name_plural = u"生产产品"

    def __unicode__(self):
        return self.type
    
class Transport(models.Model):
    crg_id = models.CharField(max_length=30,primary_key=True,
                              unique=True,verbose_name=u"运输单号")
    tanker = models.ForeignKey(Tanker,verbose_name=u"罐车")
    proj = models.ForeignKey(Project)
    product = models.ForeignKey(Product)
    date = models.DateField()
    driver = models.CharField(max_length=30)
    quantity = models.FloatField()
    dis_mod = models.FloatField(default=0.0,blank=True)
    timeout = models.IntegerField(default=0,blank=True)
    price = models.FloatField(default=30.0)
    
    class Meta:
        verbose_name_plural = u"运输单"
    
    def __unicode__(self):
        return self.crg_id
    
