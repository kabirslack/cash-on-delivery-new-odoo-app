from odoo import models, fields

class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('cod', 'Cash on Delivery')])

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _cod_form_validate(self, data):
        return True
