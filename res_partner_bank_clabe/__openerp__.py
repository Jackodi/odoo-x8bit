{
    'name': "Modulo para agregar el campo CLABE a res.partner.bank",
    'version': '1.0',
    'depends': [],
    'author': "Lizbeth Contreras",
    'category': 'Timesheet',
    'description': """
    Modulo para agregar el campo CLABE a res.partner.bank
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_bank_clabe.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo.xml',
    ],
}