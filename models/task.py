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
    work_report = fields.Text()
    # urgent_grade = fields.Selection(selection=[
        # ('overdue', 'Overdue'),
        # ('urgent', 'Urgent'),
        # ('normal', 'Normal')],
        # compute='_compute_urgent_grade',
        # store=False,
        # readonly=True)
    ## 附件
    attachment_files = fields.One2many('ir.attachment','res_id',
            domain=['&',('res_model','=','realty_plan.task'),('res_field','=','attachment_files')],
            string='Attachment Docs')
    attachment_count = fields.Integer('Attachment docs count', compute='_compute_attachment_count')

    # Constaints
    _sql_constraints = [
            ('name_uniq', 'unique (name)', "Task name already exists!"),
            ('code_uniq', 'unique (code)', "Task code already exists!"),
            ]

    # 附件相关
    @api.multi
    def _compute_attachment_count(self):
        read_group_res = self.env['ir.attachment'].read_group(
            [('res_model','=',self._name),('res_field','=','attachment_files'),('res_id','in',self.ids)],
            ['res_id'],['res_id']
            )
        attachdata = dict((res['res_id'],res['res_id_count']) for res in read_group_res)
        for record in self:
            record.attachment_count = attachdata.get(record.id,0)

    @api.multi
    def _action_get_attachment_tree_view_attachment_files(self):
        attachment_action = self.env.ref('base.action_attachment')
        action = attachment_action.read()[0]
        action['context'] = {'default_res_model':self._name,'default_res_id':self.ids[0], 'default_res_field':'attachment_files'}
        action['domain'] = str(['&', ('res_model', '=', self._name),('res_field','=','attachment_files'),('res_id', 'in', self.ids)])
        action['search_view_id'] = (self.env.ref('realty_plan.ir_attachment_view_search_inherit_task').id,)
        return action
    # @api.depends('close_date')
    # def _compute_urgent_grade(self):
        # pass


