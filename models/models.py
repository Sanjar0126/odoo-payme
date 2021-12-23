# -*- coding: utf-8 -*-

from odoo import models, fields, api


class payme(models.Model):
    _name = 'payme.payme'
    _description = 'payme.payme'

    name = fields.Char()
    value = fields.Integer()
    card = fields.Many2one(comodel_name='card', ondelete='set null')

class card(models.Model):
    _name = 'payme.card'
    _description = 'payme.card'
    
    token = fields.Char(required=True)
    number = fields.Char(required=True)
    expire = fields.Char(required=True)
    active = fields.Boolean(default=False)