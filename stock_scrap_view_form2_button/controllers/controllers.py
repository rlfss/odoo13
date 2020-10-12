# -*- coding: utf-8 -*-
# from odoo import http


# class StockScrapViewForm2Button(http.Controller):
#     @http.route('/stock_scrap_view_form2_button/stock_scrap_view_form2_button/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_scrap_view_form2_button/stock_scrap_view_form2_button/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_scrap_view_form2_button.listing', {
#             'root': '/stock_scrap_view_form2_button/stock_scrap_view_form2_button',
#             'objects': http.request.env['stock_scrap_view_form2_button.stock_scrap_view_form2_button'].search([]),
#         })

#     @http.route('/stock_scrap_view_form2_button/stock_scrap_view_form2_button/objects/<model("stock_scrap_view_form2_button.stock_scrap_view_form2_button"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_scrap_view_form2_button.object', {
#             'object': obj
#         })
