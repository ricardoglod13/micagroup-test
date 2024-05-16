from odoo import models, fields


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string='Estudiante')
