# -*- coding: utf-8 -*-
from odoo import http


class Payme(http.Controller):
    @http.route('/payme/payme', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('payme.index', {
            'objects': ["First", "Second", "Third", "Fourth"]
        })

    @http.route('/payme/payme/objects', auth='public')
    def list(self, **kw):
        return http.request.render('payme.listing', {
            'root': '/payme/payme',
            'objects': http.request.env['payme.payme'].search([]),
        })

    @http.route('/payme/payme/objects/<model("payme.payme"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('payme.object', {
            'object': obj
        })
