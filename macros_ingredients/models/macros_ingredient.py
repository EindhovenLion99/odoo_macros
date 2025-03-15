##############################################################################
# Copyright (c) 2025 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the Odoo Proprietary License v1.0 (OPL).
# See LICENSE file for full licensing details.
##############################################################################

from odoo import fields, models


class MacrosIngredient(models.Model):
    _name = 'macros.ingredient'

    name = fields.Char(required=True)
    provider = fields.Char()
    category_id = fields.Many2one('macros.ingredient.category')

    # Pricing

    uom_id = fields.Many2one(
        'uom.uom', string='Unit of Measure', default=lambda self: self.env.ref('uom.product_uom_unit')
    )
    price = fields.Float()

    # Macros

    calories = fields.Float()
    protein = fields.Float()
    fat = fields.Float()
    carbs = fields.Float()
