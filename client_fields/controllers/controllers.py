# -*- coding: utf-8 -*-
# from odoo import http


# class ClientName(http.Controller):
#     @http.route('/client_name/client_name/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/client_name/client_name/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('client_name.listing', {
#             'root': '/client_name/client_name',
#             'objects': http.request.env['client_name.client_name'].search([]),
#         })

#     @http.route('/client_name/client_name/objects/<model("client_name.client_name"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('client_name.object', {
#             'object': obj
#         })
