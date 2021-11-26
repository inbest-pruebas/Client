# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class client_name(models.Model):
#     _name = 'client_name.client_name'
#     _description = 'client_name.client_name'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
