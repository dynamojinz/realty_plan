# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _
from odoo.tools import pycompat

class TaskType(models.Model):
    _name = 'realty_plan.task.type'
    name = fields.Char()


class Task(models.Model):
    _name = 'realty_plan.task'
    _order = 'code asc'

    name = fields.Char()
    code = fields.Char()
    plan_id = fields.Many2one('realty_plan.plan', ondelete="cascade")
    type_id = fields.Many2one('realty_plan.task.type')
    grade = fields.Selection(selection=[
        ('keynode', 'Key Node'),
        ('level_1', 'Level 1'),
        ('level_2', 'Level 2'),
       ])
    owner_id = fields.Many2one('res.users')
    # manager_id = fields.Many2one('res.users')
    start_date = fields.Date()
    close_date = fields.Date()
    state = fields.Selection(selection=[
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('canceled', 'Canceled')],default='open', readonly=True)
    # urgent_grade = fields.Selection(selection=[
        # ('overdue', 'Overdue'),
        # ('urgent', 'Urgent'),
        # ('normal', 'Normal')],
        # compute='_compute_urgent_grade',
        # store=False,
        # readonly=True)

    # Constaints
    _sql_constraints = [
            ('name_uniq', 'unique (name)', "Task name already exists!"),
            ('code_uniq', 'unique (code)', "Task code already exists!"),
            ]

    # @api.depends('close_date')
    # def _compute_urgent_grade(self):
        # pass


