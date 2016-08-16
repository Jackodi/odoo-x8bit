from openerp import models, fields, api
# import logging

class hr_employee_campos(models.Model):
	#_name = 'hr.employee'
	_inherit = 'hr.employee'

	#fields
	nss = fields.Integer(string="NSS",size=11)
	curp = fields.Char(string='CURP', size=18)
	f_ingreso_laboral = fields.Date(string='Fecha de ingreso laboral')