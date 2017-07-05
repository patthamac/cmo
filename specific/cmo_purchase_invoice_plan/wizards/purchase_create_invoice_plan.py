# -*- coding: utf-8 -*-
from . import models, fields


class PurchaseCreateInvoicePlan(models.Model):
    _inherit = 'purchase.create.invoice.plan'

    invoice_mode = fields.Selection(
        [('change_price', 'As 1 Job (change price)'), ],
        default='change_price',
    )
