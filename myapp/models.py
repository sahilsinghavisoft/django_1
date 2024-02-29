from django.db import models

#employee model
class employee(models.Model):
    employee_ID=models.IntegerField(default=0)
    employee_role=models.CharField(max_length=50)
    employee_salary=models.IntegerField(default=0)
    #company=models.ForeignKey(company)
#company model
class company(models.Model):
    company_name=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=
    (("IT","IT"),
    ("NON IT","NON IT"),
    ("HR","HR")
    ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.company_name+self.type