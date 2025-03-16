##############################################################################
# Copyright (c) 2025 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the Odoo Proprietary License v1.0 (OPL).
# See LICENSE file for full licensing details.
##############################################################################

from odoo import fields, models


class MacrosIngredientCategory(models.Model):
    _name = "macros.dish.category"

    name = fields.Char(required=True)
