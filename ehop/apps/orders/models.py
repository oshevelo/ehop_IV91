from django.db import models

from ehop.apps.carts.models import Cart
from ehop.apps.userprofiles.models import UserProfile
from ehop.apps.shipments.models import Shipment
from ehop.apps.payments.models import Payment


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
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL)
    cart_items = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipments_info = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    payment_info = models.ForeignKey(Payment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=15, choices=ORDER_STATUS_CHOICE, default=AWAITING_PAYMENT)

    def __str__(self):
        return f'Order #{self.id} by {self.user}.'

