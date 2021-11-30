# -*- coding: utf-8 -*-
# from odoo import http


# class Names(http.Controller):
#     @http.route('/names/names/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/names/names/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('names.listing', {
#             'root': '/names/names',
#             'objects': http.request.env['names.names'].search([]),
#         })

#     @http.route('/names/names/objects/<model("names.names"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('names.object', {
#             'object': obj
#         })
