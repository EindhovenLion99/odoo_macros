##############################################################################
# Copyright (c) 2025 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the Odoo Proprietary License v1.0 (OPL).
# See LICENSE file for full licensing details.
##############################################################################

{
    "name": "Macros Dishes",
    "version": "18.0.1.0.0",
    "summary": "Creates dishes",
    "author": "Noah Sanchez Geurts",
    "license": "OPL-1",
    "depends": [
        'macros_ingredients',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/macros_dish_category.xml',
        'views/macros_dish.xml',
        'views/macros_menu.xml',
    ],
    "installable": True,
}
