from openerp import models, fields, api
# import logging

class res_partner_bank_clabe(models.Model):
	#_name = 'hr.employee'
	_inherit = 'res.partner.bank'

	#fields
	clabe = fields.Char(string="CLABE",size=19)