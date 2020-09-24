from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from collections import defaultdict
from math import floor

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError
from odoo.tools import float_compare, float_round
class ChangeWorkorder(models.Model):
    _description = 'Change Work Order done'
    _inherit = ['mrp.workorder']

    
    def write(self, values):

        if list(values.keys()) != ['time_ids'] and any(workorder.state == 'don' for workorder in self):
            raise UserError(_('You can not change the finished work order TEST.'))

        return super().write(values)