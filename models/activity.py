from odoo import api, exceptions, fields, models, _
import datetime

class LandActivity(models.Model):
    _name = 'land.activity'
    _description = "Activity"
    _order = 'id desc'
    c_lines = [
            ('mobile', 'Mobile'),
            ('email', 'Email'),
            ('meeting', 'Meeting'),
            ('todo', 'To Do')
        ]

    name = fields.Char(string="Name")
    purpose = fields.Char(string="Subject")
    start_date = fields.Date(string="Activity Date")
    next_date = fields.Date(string="Next Activity Date")
    project_id = fields.Many2one('land.project', 'Project')
    remarks = fields.Char(string="Remarks")
    follow_up = fields.Boolean(string="Follow Up")

    communication_channel = fields.Selection(
        selection=c_lines,
        string='Communication', required=True)
    next_communication_channel = fields.Selection(
        selection=c_lines,
        string='Next Communication')
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('cancel', 'Cancelled'),
        ],
        string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')
