##############################################################################
# Copyright (c) 2025 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the Odoo Proprietary License v1.0 (OPL).
# See LICENSE file for full licensing details.
##############################################################################

{
    "name": "Macros Ingredients",
    "version": "18.0.1.0.0",
    "summary": "Creates ingredients",
    "author": "Noah Sanchez Geurts",
    "license": "OPL-1",
    "depends": [
        'uom',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/macros_ingredients_category.xml',
        'views/macros_ingredients.xml',
        'views/macros_menu.xml',
    ],
    "installable": True,
}
