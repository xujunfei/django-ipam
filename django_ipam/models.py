from swapper import swappable_setting

from .base.models import AbstractIpAddress, AbstractSubnet

from django.db import models
from openwisp_utils.base import TimeStampedEditableModel

class Subnet(AbstractSubnet):
    subnet_class_choices = (
        ("BGP", "BGP"),
        ("CT", "电信"),
        ("CU", "联通"),
        ("CM", "移动"),
        ("LOCAL", "私网地址"),
    )
    subnet_class = models.CharField(max_length=10, blank=True, choices=subnet_class_choices, verbose_name="IP分类")
    product = models.ForeignKey('Product', models.CASCADE, blank=True, null=True)

    class Meta(AbstractSubnet.Meta):
        abstract = False
        swappable = swappable_setting('django_ipam', 'Subnet')


class IpAddress(AbstractIpAddress):
    class Meta(AbstractIpAddress.Meta):
        abstract = False
        swappable = swappable_setting('django_ipam', 'IpAddress')


class CsvImportException(Exception):
    pass


class Product(TimeStampedEditableModel):
    customer_name = models.CharField(max_length=100, blank=True, verbose_name="客户名称")
    order_id = models.CharField(max_length=100, blank=True, verbose_name="订单编号")
    description = models.CharField(max_length=100, blank=True, verbose_name="描述")

    class Meta:
        verbose_name = "客户线路"
        verbose_name_plural = "客户线路表"

    def __str__(self):
        return "%s(%s)" % (self.customer_name, self.order_id)
