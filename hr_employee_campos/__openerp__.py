{
    'name': "Módulo que agrega campos al empleado",
    'version': '1.0',
    'depends': ['hr'],
    'author': "X8BIT SA DE CV",
    'category': 'Recursos Humanos',
    'description': """
    Módulo que agrega campos al empleado
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_campos.xml',
    ],
    'installable': True,
    'auto_install': False,
}