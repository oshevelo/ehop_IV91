import uuid

from django.contrib.auth.models import User
from django.db import models


# temporary commented, waiting for other models
#
# from apps.carts.models import Cart
# from apps.shipments.models import Shipment
# from apps.payments.models import Payment
# from apps.products.models import Product


class Order(models.Model):
    """
    Awaiting payment — Order received, no payment initiated. Awaiting payment (unpaid).
    On hold — stock is reduced, but customer need to confirm payment.
    Processing — Payment received (paid) and stock has been reduced; order is awaiting fulfillment.
                All product orders require processing, except those that only contain products which
                are both Virtual and Downloadable.
    Awaiting shipment - Order is formed and is being prepared for shipment.
    Is shipped - Order is sent to the customer.
    Completed — Order fulfilled and complete – requires no further action.
    Canceled — Canceled by an admin or the customer – stock is increased, no further action required.
    Refunded — Refunded by an admin – no further action required.
    """
    AWAITING_PAYMENT = "Awaiting payment"
    ON_HOLD = "On hold"
    PROCESSING = "Processing"
    AWAITING_SHIPMENT = "Awaiting shipment"
    IS_SHIPPED = "Is shipped"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    REFUNDED = "Refunded"

    ORDER_STATUS_CHOICE = [
        (AWAITING_PAYMENT, "Awaiting payment"),
        (ON_HOLD, "On hold"),
        (PROCESSING, "Processing"),
        (AWAITING_SHIPMENT, "Awaiting shipment"),
        (IS_SHIPPED, "Is shipped"),
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled"),
        (REFUNDED, "Refunded"),

    ]

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # temporary commented, waiting for other models
    #
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    # payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=25, choices=ORDER_STATUS_CHOICE, default=AWAITING_PAYMENT)
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f'Order #{self.public_id} by {self.user}. Status : {self.order_status}.'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    # temporary commented, waiting for Product model
    #
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        # add {} to self.product.name when Product model will be created
        return f'self.product.name - {self.quantity} items.'
