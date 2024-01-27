from odoo import api, exceptions, fields, models, _
import datetime


class LandCRM(models.Model):
    _name = 'land.crm'
    _description = "Land CRM"
    _order = 'id desc'

    name = fields.Char(string="CRM Name")

    expected_revenue = fields.Float(string="Expected Revenue")
    probability = fields.Float(string="Probability")

    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    email = fields.Char(string='Email', related='customer_id.email')
    phone = fields.Char(string='Phone', related='customer_id.phone')
    salesperson = fields.Many2one('res.users', string='Salesperson')
    expected_closing = fields.Date(string="Expected Closing")
    tags = fields.Char(string="Tags")

    company_name = fields.Char(string="Company Name")
    address = fields.Char(string="Address")
    website = fields.Char(string="Website")
    job_position = fields.Char(string="Job Position")
    mobile = fields.Char(string="Mobile")

    medium = fields.Char(string="Medium")
    source = fields.Char(string="Source")
    referred_by = fields.Char(string="Referred By")

    tracking = fields.Char(string="Tracking")
    sales_team = fields.Char(string="Sales Team")
    days_to_assign = fields.Float(string="Days to Assign")
    days_to_close = fields.Float(string="Days to Close")






