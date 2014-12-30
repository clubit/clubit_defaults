from openerp.osv import fields
from openerp.osv import osv
from openerp.tools.translate import _

class account_invoice(osv.osv):
    _inherit = 'account.invoice'
    _order = 'number desc'

account_invoice()
