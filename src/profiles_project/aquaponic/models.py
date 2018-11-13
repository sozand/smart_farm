from django.db import models
import datetime


# Create your models here.

class Farm(models.Model):
    farm_name = models.CharField(max_length=250)
    start_date = models.DateTimeField(auto_now_add=True)
    weeks_between_harvest = models.DecimalField(max_digits=3, decimal_places=2)
    annual_production_InKg = models.DecimalField(max_digits=10, decimal_places=3)
    final_culling_at_harvest_InPercent = models.DecimalField(max_digits=8, decimal_places=5)
    target_rearing_temperature_InCelsius = models.DecimalField(max_digits=3, decimal_places=3)
    target_Size_InGram = models.DecimalField(max_digits=8, decimal_places=5)
    initial_Size_InGram = models.DecimalField(max_digits=8, decimal_places=5)
    number_of_growout_states = models.IntegerField()

    class Meta:
        ordering = ('start_date',)

    def __str__(self):
        return "%s" % self.farm_name


class Address(models.Model):
    Line1 = models.CharField(max_length=250)
    Line2 = models.CharField(max_length=250)
    Subdistrict = models.CharField(max_length=250)
    District = models.CharField(max_length=250)
    Province = models.CharField(max_length=250)
    State = models.CharField(max_length=250)
    Country = models.CharField(max_length=250)
    Zip_Code = models.CharField(max_length=250)
    Full_Address = models.CharField(max_length=250)

    Farm = models.OneToOneField(
        Farm,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        ordering = ('Province',)

    def __str__(self):
        return self.Full_Address


class Unit(models.Model):
    Unit_Name = models.CharField(max_length=250)
    Create_by = models.CharField(max_length=250)
    Create_On = models.DateTimeField(auto_now_add=True)
    Description = models.CharField(max_length=250)

    class Meta:
        ordering = ('Unit_Name',)

    def __str__(self):
        return self.Unit_Name


class Species(models.Model):
    species_name = models.CharField(max_length=250)
    farms = models.ManyToManyField(Farm, through='FarmingSpeciesRearingUnit')
    add_On_Date = models.DateTimeField(auto_now_add=True)
    suitable_farming_temperature_max_InCelsius = models.DecimalField(max_digits=3, decimal_places=3)
    suitable_farming_temperature_min_InCelsius = models.DecimalField(max_digits=3, decimal_places=3)

    class Meta:
        ordering = ('species_name',)

    def __str__(self):
        return self.species_name


class TypeOfRearingUnit(models.Model):
    typeName = models.CharField(max_length=250)
    rearing_Capacity = models.DecimalField(max_digits=10, decimal_places=3)
    unit_volume = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.CharField(max_length=250)


class FarmingSpeciesRearingUnit(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    add_On_Date = models.DateTimeField(default=datetime.datetime.now)
    type_of_rearing_unit = models.ForeignKey(TypeOfRearingUnit, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)

    class Meta:
        ordering = ('farm',)

    def __str__(self):
        return self.farm


class RearingParameterFeedConversionRate(models.Model):
    Value = models.DecimalField(max_digits=8, decimal_places=5)
    recorded_on_Date = models.DateTimeField(auto_now_add=True)
    RearingUnit = models.ForeignKey(FarmingSpeciesRearingUnit, on_delete=models.CASCADE)
    unit = models.OneToOneField(
        Unit,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        ordering = ('recorded_on_Date',)

    def __str__(self):
        return self.Value


class RearingParameterMaximumDensityAllowableFactor(models.Model):
    Value = models.DecimalField(max_digits=8, decimal_places=5)
    recorded_on_Date = models.DateTimeField(auto_now_add=True)
    RearingUnit = models.ForeignKey(FarmingSpeciesRearingUnit, on_delete=models.CASCADE)
    unit = models.OneToOneField(
        Unit,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        ordering = ('recorded_on_Date',)

    def __str__(self):
        return self.Value


class RearingParameterRearingTemperature(models.Model):
    Value = models.DecimalField(max_digits=8, decimal_places=5)
    recorded_on_Date = models.DateTimeField(auto_now_add=True)
    RearingUnit = models.ForeignKey(FarmingSpeciesRearingUnit, on_delete=models.CASCADE)
    unit = models.OneToOneField(
        Unit,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        ordering = ('recorded_on_Date',)

    def __str__(self):
        return self.Value


class RearingParameterGrowthPerMonth(models.Model):
    Value = models.DecimalField(max_digits=8, decimal_places=5)
    recorded_on_Date = models.DateTimeField(auto_now_add=True)
    RearingUnit = models.ForeignKey(FarmingSpeciesRearingUnit, on_delete=models.CASCADE)
    unit = models.OneToOneField(
        Unit,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        ordering = ('recorded_on_Date',)

    def __str__(self):
        return self.Value


class RearingParameterConditionFactor(models.Model):
    Value = models.DecimalField(max_digits=8, decimal_places=5)
    recorded_on_Date = models.DateTimeField(auto_now_add=True)
    RearingUnit = models.ForeignKey(FarmingSpeciesRearingUnit, on_delete=models.CASCADE)
    unit = models.OneToOneField(
        Unit,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        ordering = ('recorded_on_Date',)

    def __str__(self):
        return self.Value


