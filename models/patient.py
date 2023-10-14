from odoo import fields, models, api
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="Reference", default='HP000')
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age')
    gender = fields.Selection(
        [('male', 'Male'), ('female', "Female")], string="Gender", tracking=True)
    active = fields.Boolean(string="Active", default=True)
    # appointment_ids = fields.One2many(string="Appointments", comodel_name='hospital.appointment',
    #                                   inverse_name='patient_id', tracking=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        """ Compute the age of the patient"""
        current_date = date.today()

        for rec in self:
            if rec.date_of_birth:
                rec.age = current_date.year - rec.date_of_birth.year
            else:
                rec.age = 0
