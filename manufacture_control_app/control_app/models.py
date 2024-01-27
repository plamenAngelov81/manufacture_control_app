from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


class OrderParts(models.Model):
    ORDER_NUM_MAX_LEN = 50
    ORDER_NUM_MIN_LEN = 5
    ITEM_NUM_MAX_LEN = 50
    ITEM_NUM_MIN_LEN = 5
    PART_NAME_MAX_LEN = 50
    PART_NAME_MIN_LEN = 5

    order_number = models.CharField(
        verbose_name='Order Number',
        max_length=ORDER_NUM_MAX_LEN,
        validators=[MinLengthValidator(ORDER_NUM_MIN_LEN)],
        null=False,
        blank=False,
    )

    item_number = models.CharField(
        verbose_name='Item Number',
        max_length=ITEM_NUM_MAX_LEN,
        validators=[MinLengthValidator(ITEM_NUM_MIN_LEN)],
        null=False,
        blank=False,
    )
    part_name = models.CharField(
        verbose_name='Part Name',
        max_length=PART_NAME_MAX_LEN,
        validators=[MinLengthValidator(PART_NAME_MIN_LEN)],
        null=False,
        blank=False,
    )

    part_quantity = models.PositiveIntegerField(
        verbose_name='Quantity',
        null=True,
        blank=True,
    )


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

    class Meta:
        verbose_name_plural = 'Machines'
        ordering = ['pk']

    def __str__(self):
        return self.machine_name


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
        unique=True,
    )

    operation_description = models.TextField(
        max_length=OPERATION_DESCRIPTION_MAX_LEN,
        verbose_name='Description',
        validators=[MinLengthValidator(OPERATION_DESCRIPTION_MIN_LEN)],
        null=False,
        blank=False,
    )

    part_order = models.ForeignKey(
        OrderParts,
        on_delete=models.CASCADE,
        verbose_name='Part Order',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'Operations'

    def __str__(self):
        return self.operation_name


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

    class Meta:
        verbose_name_plural = 'Tools'

    def __str__(self):
        return self.tool_name
