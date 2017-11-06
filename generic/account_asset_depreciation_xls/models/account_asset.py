# -*- coding: utf-8 -*-
# Copyright 2009-2017 Noviat
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class AccountAsset(models.Model):
    _inherit = 'account.asset'

    @api.model
    def _xls_acquisition_fields(self):
        """
        Update list in custom module to add/drop columns or change order
        """
        return [
            'account', 'name', 'code', 'date_start', 'depreciation_base',
            'salvage_value',
        ]

    @api.model
    def _xls_active_fields(self):
        """
        Update list in custom module to add/drop columns or change order
        """
        return [
            'account', 'name', 'date_purchase', 'date_start', 'purchase_value',
            'asset_value_previous', 'percent', 'salvage_value',
            'asset_line_amount', 'depreciated_value', 'remaining_value',
            'code', 'note',
        ]  # 'depreciation_base' 'fy_start_value' 'fy_depr', 'fy_end_value',
        # 'fy_end_depr', 'method', 'method_number', 'prorata', 'residual_value'

    @api.model
    def _xls_acquisition_template(self):
        """
        Template updates

        """
        return {}

    @api.model
    def _xls_active_template(self):
        """
        Template updates

        """
        return {}
