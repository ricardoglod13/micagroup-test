from odoo import models

class StudentContractReport(models.AbstractModel):
    _name = "report.student_contract.student_contract_report"
    _description = "Contrato de Estudiante"

    def _get_report_values(self, docids, data):
        docs = self.env['student.contract'].browse(docids),
        return {
            'data': data,
            'docids': docids,
            'docs': docs
        }
