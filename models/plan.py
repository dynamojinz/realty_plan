# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _

class Plan(models.Model):
    _name = 'realty_plan.plan'

    name = fields.Char()
    task_ids = fields.One2many('realty_plan.task', 'plan_id', string="Tasks", copy=True)
    version = fields.Char(default='master',readonly=True)
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
        ], default='draft')




