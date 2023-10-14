from odoo import fields, models, api


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointments"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(string="Patient", comodel_name="hospital.patient", tracking=True)
    ref = fields.Char(string="Reference")
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime("Appointment Time", tracking=True, default=fields.Datetime.now)
    doctor_id = fields.Many2one('res.users', string='Doctor')
    booking_date = fields.Date("Booking Date", default=fields.Date.context_today)
    prescription = fields.Html(string="Prescription")

    priority = fields.Selection([('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High')], string="Priority")
    status = fields.Selection(
        [('draft', 'Draft'), ('in_consultation', 'In Consultation'), ('done', 'Done'), ('cancel', 'Cancelled')],
        default='draft',
        required=True,
        string="Status")

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Testing...............")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successful',
                'type': 'rainbow_man',
            }
        }

    def display_notification(self):
        """Display Notification"""

        action = self.env.ref('om_hospital.action_hospital_patient')

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Click to open the Patient Record',
                'message': '%s',
                'links': [{
                    'label': self.patient_id.name,
                    'url': f'#action={action.id}&id={self.patient_id.id}&model=hospital.patient',
                }],
                'sticky': True,
            }
        }
