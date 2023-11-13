from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


class Machine(models.Model):
    MACHINE_NAME_MAX_LEN = 30
    MACHINE_NAME_MIN_LEN = 5
    MACHINE_DESCRIPTION_MAX_LEN = 350
    MIN_TOOLS_VALUE = 1

    machine_name = models.CharField(
        verbose_name='Name',
        max_length=MACHINE_NAME_MAX_LEN,
        validators=[MinLengthValidator(MACHINE_NAME_MIN_LEN)],
        null=False,
        blank=False,
    )

    number_of_tools = models.PositiveIntegerField(
        verbose_name='Number of Tools',
        validators=[MinValueValidator(MIN_TOOLS_VALUE)],
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=MACHINE_DESCRIPTION_MAX_LEN,
        null=True,
        blank=True,
    )


class Operations(models.Model):
    OPERATION_NAME_MAX_LEN = 30
    OPERATION_NAME_MIN_LEN = 5
    OPERATION_DESCRIPTION_MAX_LEN = 300
    OPERATION_DESCRIPTION_MIN_LEN = 50

    operation_name = models.CharField(
        verbose_name='Name',
        max_length=OPERATION_NAME_MAX_LEN,
        validators=[MinLengthValidator(OPERATION_NAME_MIN_LEN)],
        null=False,
        blank=False,
    )

    operation_id = models.PositiveIntegerField(
        verbose_name='Id',
    )

    operation_description = models.TextField(
        max_length=OPERATION_DESCRIPTION_MAX_LEN,
        verbose_name='Description',
        validators=[MinLengthValidator(OPERATION_DESCRIPTION_MIN_LEN)],
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name_plural = 'Operations'


class Tool(models.Model):
    TOOL_NAME_MAX_LEN = 30
    TOOL_NAME_MIN_LEN = 5

    tool_name = models.CharField(
        verbose_name='Name',
        max_length=TOOL_NAME_MAX_LEN,
        validators=[MinLengthValidator(TOOL_NAME_MIN_LEN)],
        null=False,
        blank=False,
    )

    tool_length = models.FloatField(
        verbose_name='Tool Length',
        null=True,
        blank=True
    )

    tool_diameter = models.FloatField(
        verbose_name='Tool Diameter',
        null=True,
        blank=True
    )

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        verbose_name='Machine',
        null=True,
        blank=True,
    )

    operation = models.ForeignKey(
        Operations,
        on_delete=models.CASCADE,
        verbose_name='Operation',
        null=True,
        blank=True,
    )
