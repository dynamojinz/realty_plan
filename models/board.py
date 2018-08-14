# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _
import datetime

class PlanBoard(models.AbstractModel):
    _inherit = 'board.board'
    _name = 'realty_plan.board'
    _auto = False

    @api.model
    def create(self, vals):
        return self

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = models.AbstractModel.fields_view_get(self, view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        res.update({
            'arch': self._arch_preprocessing(res['arch']),
            'toolbar': {'print': [], 'action': [], 'relate': []}
        })
        # print(res)
        return res

    @api.model
    def _arch_preprocessing(self, arch):
        from lxml import etree

        def remove_unauthorized_children(node):
            for child in node.iterchildren():
                if child.tag == 'action':
                    if child.get('invisible'):
                        node.remove(child)
                    strname = child.get('name', False)
                    if strname:
                        child.set('name', str(self.env.ref(strname).id))
                    domain = child.get('domain', False)
                    if domain:
                        newdomain = domain.replace("uid", str(self.env.user.id))
                        if newdomain != domain:
                            child.set('domain', newdomain)
                else:
                    remove_unauthorized_children(child)
            return node

        archnode = etree.fromstring(arch)
        return etree.tostring(remove_unauthorized_children(archnode), pretty_print=True, encoding='unicode')




