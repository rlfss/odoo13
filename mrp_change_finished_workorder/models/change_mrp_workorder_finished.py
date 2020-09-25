from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from collections import defaultdict
from math import floor

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError
from odoo.tools import float_compare, float_round
class MrpWorkorder(models.Model):
    _description = 'Change Work Order done'
    _inherit = ['mrp.workorder']

    @api.model
    def write(self, values):
        if 'workorder.state' in values:

            del values['workorder.state']

        return super(MrpWorkorder, self).write(values)
