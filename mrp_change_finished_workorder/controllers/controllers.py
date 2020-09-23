# -*- coding: utf-8 -*-
# from odoo import http


# class MrpChangeFinishedWorkorder(http.Controller):
#     @http.route('/mrp_change_finished_workorder/mrp_change_finished_workorder/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_change_finished_workorder/mrp_change_finished_workorder/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_change_finished_workorder.listing', {
#             'root': '/mrp_change_finished_workorder/mrp_change_finished_workorder',
#             'objects': http.request.env['mrp_change_finished_workorder.mrp_change_finished_workorder'].search([]),
#         })

#     @http.route('/mrp_change_finished_workorder/mrp_change_finished_workorder/objects/<model("mrp_change_finished_workorder.mrp_change_finished_workorder"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_change_finished_workorder.object', {
#             'object': obj
#         })
