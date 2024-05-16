# -*- coding: utf-8 -*-

{
    'name': 'Student Contract',
    'version': '1.0.0',
    'category': 'Generic Modules',
    'author': 'Ricardo Sánchez',
    'summary': 'Student Contract Test to MiCasino.com',
    'description': "Student Contract Test to MiCasino.com",
    'depends': [
        'contacts', 'hr'
    ],
    'data': [
        'security/ir_groups.xml',
        'security/ir.model.access.csv',

        'data/university_class.xml',
	    'data/ir_cron.xml',

        'views/inherits/hr/hr_employee.xml',
        'views/inherits/res/res_partner.xml',
        'views/student_contract.xml',
        'views/university_class.xml',
        'report/student_contract.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
