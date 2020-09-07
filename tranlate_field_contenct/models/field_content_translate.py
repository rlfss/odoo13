from odoo import models, fields
class Company(models.Model):
    _inherit = "res.company"
    #website_description = fields.Html(translate=False)
    name = fields.Char(translate=True)