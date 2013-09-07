#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

app_label = u'运费统计'

class Group(models.Model):
    group_name = models.CharField(u'销售组名称',max_length=20)
    
    class Meta:
        verbose_name_plural = u"销售分组"
        
    def __unicode__(self):
        return self.group_name

class Project(models.Model):
    staff = models.ForeignKey(Group)
    proj_name = models.CharField(u'工程名',max_length=30)
    item_name = models.CharField(u'项目名',max_length=30)
    distance = models.FloatField(u'运距')
    date = models.DateField(u'日期')
    
    class Meta:
        verbose_name_plural = u"工程项目"
    
    def __unicode__(self):
        return self.proj_name
    
class Tanker(models.Model):
    License_Num_Belong = {"83377":u"公司车",
                          "83399":u"公司车",
                          "69783":u"段总",
                          "96128":u"段总",
                          "3236":u"王巨全",
                          "66928":u"郑小兵"}
    lpn = models.CharField(u"车牌号码",max_length=10)
    
    def _category(self):
        return self.License_Num_Belong[self.lpn]
    _category.short_description = u"属于哪个车队?"
    belong = property(_category)
    
    class Meta:
        verbose_name_plural = u"罐车"
        
    def __unicode__(self):
        return self.lpn
    
class Product(models.Model):
    type = models.CharField(u'产品型号',max_length=10)
    
    class Meta:
        verbose_name_plural = u"生产产品"

    def __unicode__(self):
        return self.type
    
class Transport(models.Model):
    crg_id = models.CharField(u"运输单号",max_length=30,
                              primary_key=True,unique=True)
    tanker = models.ForeignKey(Tanker,verbose_name=u"罐车")
    proj = models.ForeignKey(Project,verbose_name=u"工程项目")
    product = models.ForeignKey(Product,verbose_name=u"产品型号",default="C30")
    date = models.DateField(u'日期')
    driver = models.CharField(u'司机',max_length=30,default=u"魏志伟")
    quantity = models.FloatField(u'单次运量')
    dis_mod = models.FloatField(u'运距修正',default=0.0,blank=True)
    timeout = models.FloatField(u'超时修正',default=0.0,blank=True)
    price = models.FloatField(u'单价',default=30.0)
    
    class Meta:
        verbose_name_plural = u"运输单"
    
    def __unicode__(self):
        return self.crg_id
    
