##############################################################################
# Copyright (c) 2025 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the Odoo Proprietary License v1.0 (OPL).
# See LICENSE file for full licensing details.
##############################################################################

from odoo import api, fields, models


class MacrosDish(models.Model):
    _name = 'macros.dish'

    name = fields.Char(required=True)
    category_id = fields.Many2one('macros.dish.category')
    date = fields.Datetime()

    # Pricing

    price = fields.Float()

    # Macros

    ingredient_line_ids = fields.One2many('macros.dish.line', 'dish_id')

    calories = fields.Float(compute='_compute_total_macros', store=True)
    protein = fields.Float(compute='_compute_total_macros', store=True)
    fat = fields.Float(compute='_compute_total_macros', store=True)
    carbs = fields.Float(compute='_compute_total_macros', store=True)

    @api.depends(
        'ingredient_line_ids',
        'ingredient_line_ids.ingredient_id.calories',
        'ingredient_line_ids.ingredient_id.protein',
        'ingredient_line_ids.ingredient_id.fat',
        'ingredient_line_ids.ingredient_id.carbs',
    )
    def _compute_total_macros(self):
        for dish in self:
            dish.calories = sum(line.calories for line in dish.ingredient_line_ids)
            dish.protein = sum(line.protein for line in dish.ingredient_line_ids)
            dish.fat = sum(line.fat for line in dish.ingredient_line_ids)
            dish.carbs = sum(line.carbs for line in dish.ingredient_line_ids)

    def copy(self, default=None):
        default = dict(default or {})
        dish_line_ids_data = self.ingredient_line_ids.copy_data()
        default['date'] = fields.Datetime.now()
        default['ingredient_line_ids'] = [(0, 0, line_data) for line_data in dish_line_ids_data]
        return super().copy(default)

