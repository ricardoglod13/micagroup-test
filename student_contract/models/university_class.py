from odoo import models, fields, api
from odoo.exceptions import ValidationError


class UniversityClass(models.Model):
    _name = 'university.class'
    _description = 'Clases'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    credit_unity = fields.Integer(string='Unidades de crédito')
    active = fields.Boolean(string='Activo', default=True)

    @api.constrains('name')
    def check_name(self):
        for record in self:
            search = self.search([('name', '=', record.name), ('id', '!=', record.id)])
            if search:
                raise ValidationError(f'Ya la clase {record.name} existe.\nPor favor verificar.')
