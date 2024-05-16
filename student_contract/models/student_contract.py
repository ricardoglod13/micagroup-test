from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentContract(models.Model):
    _name = 'student.contract'
    _description = 'Contrato de Estudiantes'
    _rec_name = 'name'

    name = fields.Char(string='Nombre', default='/')
    student_id = fields.Many2one(comodel_name='res.partner', string='Estudiante', domain="[('is_student', '=', True)]")
    date_from = fields.Date(string='Fecha desde')
    date_to = fields.Date(string='Fecha hasta')
    class_ids = fields.One2many(comodel_name='teacher.student.class', inverse_name='contract_id', string='Clases')
    state = fields.Selection(selection=[('draft', 'Borrador'), ('posted', 'Publicado'), ('expired', 'Expirado')], default='draft')

    @api.constrains('date_from', 'date_to')
    def check_dates(self):
        for record in self:
            if record.date_from > record.date_to:
                raise ValidationError('La Fecha desde debe ser mayor a la Fecha hasta.')

    def check_contract_expired(self):
        self = self.search([('state', '=', 'posted')])
        contract_ids = self.filtered(lambda contract: contract.date_from > contract.date_to)
        contract_ids.write({
            'state': 'expired'
        })

    def action_posted(self):
        for record in self:
            data = {
                'state': 'posted'
            }

            if record.name == '/':
                sequence_code = f'student.contract.{record.env.company.id}'
                sequence_id = self.env['ir.sequence'].search([('code', '=', sequence_code)])
                if not sequence_id:
                    sequence_id = self.env['ir.sequence'].create({
                        'number_next': 1,
                        'number_increment': 1,
                        'padding': 6,
                        'name': 'Contrato de Estudiantes',
                        'code': sequence_code,
                        'implementation': 'standard',
                        'prefix': f'CST/%(year)s/%(month)s/',
                        'active': True
                    })
                
                data.update({
                    'name': sequence_id.next_by_id()
                })

            record.write(data)

    def action_draft(self):
        for record in self:
            record.write({
                'state': 'draft'
            })

    def _get_spanish_state(self):
        state = list(filter(lambda x: x[0] == self.state, self._fields['state']._description_selection(self.env)))
        return state[0][1] if state else ''

class TeacherStudentClass(models.Model):
    _name = 'teacher.student.class'
    _rec_name = 'contract_id'

    contract_id = fields.Many2one(comodel_name='student.contract', string='Contrato')
    class_id = fields.Many2one(comodel_name='university.class', string='Clase')
    teacher_id = fields.Many2one(comodel_name='hr.employee', string='Profesor', domain="[('is_teacher', '=', True), ('class_ids', 'in', class_id)]")

    @api.constrains('contract_id.student_id', 'teacher_id')
    def check_teacher(self):
        for record in self:
            if record.teacher_id.address_home_id == record.contract_id.student_id:
                raise ValidationError('Un estudiante no puede elegirse a si mismo como profesor.')
