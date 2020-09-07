# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tranlate_field_contenct(models.Model):
#     _name = 'tranlate_field_contenct.tranlate_field_contenct'
#     _description = 'tranlate_field_contenct.tranlate_field_contenct'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
