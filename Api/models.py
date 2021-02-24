from django.db import models

class WorldData(models.Model):
    model       =   models.CharField(max_length=50)
    scenario    =   models.CharField(max_length=50, db_index=True) 
    variable    =   models.ForeignKey('Variable', on_delete=models.CASCADE)
    _2005       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2010       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2015       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2020       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2025       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2030       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2035       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2040       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2045       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2050       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2055       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2060       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2065       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2070       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2075       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2080       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2085       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2090       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2095       =   models.DecimalField(max_digits=12, decimal_places=6)
    _2100       =   models.DecimalField(max_digits=12, decimal_places=6)

    def __str__(self):
        return self.model + "-" + self.scenario + "-" + str(self.variable)
    class Meta:
        verbose_name_plural = "World Data"
        unique_together     =  (("model", "scenario", "variable"))

class Variable(models.Model):
    variable    =   models.CharField(max_length=20, primary_key=True, db_index=True)
    unit        =   models.CharField(max_length=20)
    section     =   models.CharField(max_length=10)

    def __str__(self):
        return self.variable