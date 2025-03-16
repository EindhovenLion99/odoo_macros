##############################################################################
# Copyright (c) 2025 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the Odoo Proprietary License v1.0 (OPL).
# See LICENSE file for full licensing details.
##############################################################################

from odoo import api, fields, models


class MacrosDishLine(models.Model):
    _name = 'macros.dish.line'

    dish_id = fields.Many2one('macros.dish')
    ingredient_id = fields.Many2one('macros.ingredient')
    uom_id = fields.Many2one(related='ingredient_id.uom_id')
    quantity = fields.Float()

    # Macros

    calories = fields.Float(compute='_compute_macros')
    protein = fields.Float(compute='_compute_macros')
    fat = fields.Float(compute='_compute_macros')
    carbs = fields.Float(compute='_compute_macros')

    @api.depends('ingredient_id', 'quantity')
    def _compute_macros(self):
        for line in self:
            line.calories = line.ingredient_id.calories * line.quantity / 100
            line.protein = line.ingredient_id.protein * line.quantity / 100
            line.fat = line.ingredient_id.fat * line.quantity / 100
            line.carbs = line.ingredient_id.carbs * line.quantity / 100
