#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create: 2020-11-11 13:25:56
# LastEdit: 2020-11-11 17:58:49
"""说明暂无"""
__author__ = '749B'


from django.contrib import admin

from .base.admin import AbstractIpAddressAdmin, AbstractSubnetAdmin
from .models import IpAddress, Subnet, Product

from openwisp_utils.admin import TimeReadonlyAdminMixin


@admin.register(IpAddress)
class IPAddressAdmin(AbstractIpAddressAdmin):
    pass


@admin.register(Subnet)
class BaseSubnet(AbstractSubnetAdmin):
    list_display = ('__str__', 'master_subnet', 'subnet_class2', 'product2', 'description')

    def subnet_class2(self, obj, lv=''):
        """递归获取父级网络的IP分类(subnet_class)"""
        name = obj.subnet_class
        if name:
            return lv + dict(obj.subnet_class_choices).get(name, "未知选项")
        if obj.master_subnet:
            lv += '*'
            return self.subnet_class2(obj.master_subnet, lv)
    subnet_class2.short_description = "IP分类(继承)"
    subnet_class2.empty_value_display = "没有继承"

    def product2(self, obj):
        return obj.product
    product2.short_description = "绑定线路"
    product2.empty_value_display = "—未分配—"


@admin.register(Product)
class ProductAdmin(TimeReadonlyAdminMixin, admin.ModelAdmin):
    list_display = ('__str__', 'description', )


