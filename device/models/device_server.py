from odoo import fields, models


class Server(models.Model):
    _name = 'device.server'
    _description = 'Server'
    name = fields.Char('Name', required=True)
    server_id = fields.Char('Server ID')
    active = fields.Boolean('Active?', default=True)
    server_quota = fields.Integer()
    device_id = fields.Many2many('device.device', string='Device')
