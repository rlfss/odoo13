# -*- coding: utf-8 -*-
# from odoo import http


# class TranlateFieldContenct(http.Controller):
#     @http.route('/tranlate_field_contenct/tranlate_field_contenct/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tranlate_field_contenct/tranlate_field_contenct/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tranlate_field_contenct.listing', {
#             'root': '/tranlate_field_contenct/tranlate_field_contenct',
#             'objects': http.request.env['tranlate_field_contenct.tranlate_field_contenct'].search([]),
#         })

#     @http.route('/tranlate_field_contenct/tranlate_field_contenct/objects/<model("tranlate_field_contenct.tranlate_field_contenct"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tranlate_field_contenct.object', {
#             'object': obj
#         })
