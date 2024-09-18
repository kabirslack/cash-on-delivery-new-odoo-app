{
    'name': 'Cash on Delivery Payment',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Add Cash on Delivery payment method to website purchases',
    'description': """
        This module allows customers to choose Cash on Delivery (COD) as a payment method during checkout.
    """,
    'author': 'Your Name',
    'depends': ['website_sale'],
    'data': [
        'views/payment_templates.xml',
    ],
    'installable': True,
    'application': True,
}
