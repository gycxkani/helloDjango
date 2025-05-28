from django.db import models

# Create your models here.


class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name="姓名")
    gender = models.CharField(max_length=16, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = "person"
        verbose_name = "人员信息"
