from odoo import api, exceptions, fields, models, _
import datetime


class LandProject(models.Model):
    _name = 'land.project'
    _description = "Land Project"
    _order = 'id desc'

    name = fields.Char(string="Project Name")
    address = fields.Char(string="Address")
    start_date = fields.Date(string="Project Opening Date")
    end_date = fields.Date(string="Project Completed Date")
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('ongoing', 'Ongoing'),
            ('cancel', 'Cancelled'),
        ],
        string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')

    expected_cost = fields.Float(string="Expected Cost")
    actual_cost = fields.Float(string="Actual Cost")

    total_area = fields.Char(string="Total Area")
    project_availability = fields.Char(string="Projects Availability")

    land_project_line_ids = fields.One2many('land.project.line', 'land_project_line_id',
                                            string='Land Project Lines', copy=True, auto_join=True)


class LandProjectLine(models.Model):
    _name = 'land.project.line'
    _description = "Land Project Line"

    land_project_line_id = fields.Many2one('land.project', string='Land Project ID', required=True,
                                           ondelete='cascade', index=True, copy=False)

    position_name = fields.Char(string="Position Name")
    minimum_sale_amount = fields.Float(string="Minimum Sale Amount")
    commission = fields.Float(string="Commission")
    commission_amount = fields.Float(string="Commission Amount")
    assignee_person = fields.Many2one('res.users', string="Assignee Person")

    land_status = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('ready', 'Ready'),
            ('book', 'Booked'),
            ('sold', 'Sold'),
            ('cancel', 'Cancelled'),
        ],
        string='Land Status', required=True, copy=False, tracking=True, default='draft')

    project_state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('ongoing', 'Ongoing'),
            ('cancel', 'Cancelled'),
        ],
        string='Project Status', required=True, readonly=True, copy=False, tracking=True, default='draft')




