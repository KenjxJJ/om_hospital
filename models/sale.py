from odoo import fields, models, api
from odoo.addons.sale.models.sale_order import SaleOrder as OdooSaleOrder


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    sale_description = fields.Char(string='Sale Description')


def unlink(self):
    return super(OdooSaleOrder, self).unlink()

OdooSaleOrder.unlink = unlink
