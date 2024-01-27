{
    'name': 'Land Project Module',
    'version': '1.0',
    'category': '',
    'author': 'Rocky',
    'summary': 'Land project module for sale and maintain land property',
    'description': 'Land project module for sale and maintain land property',
    'depends': ['base'],
    'data': [
        'security/land_project_security.xml',
        'security/ir.model.access.csv',
        'views/land_project_view.xml',
        'views/land_activity_view.xml',
        'views/menu_list.xml',
    ],
    'installable': True,
    'application': True,
}
