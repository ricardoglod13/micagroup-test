from odoo import models, fields

class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    
    is_teacher = fields.Boolean(string='Profesor')
    class_ids = fields.Many2many(comodel_name='university.class', string='Clases')
    