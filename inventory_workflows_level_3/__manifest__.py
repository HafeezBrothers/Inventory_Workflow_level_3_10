{
    'name':   'Inventory Workflows (Level 3)',
    'author': 'Hafeez Brothers',
    'version': '1.0',

    'depends': [
                'base',
                
                'stock'
                
                ],
    
    'data': [
      
        'Views/stock_picking_workflow.xml',
        'security/hr_user_rights_inventory.xml'
    ],
    
    'application': True,
    'price':50.00,
    'currency':'EUR', 

}
