from odoo import models, api, fields
from odoo.tools.misc import xlwt

class AppointmentReportWizard(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Print Appointment Report Wizard"
    
    patient_id = fields.Many2one("hospital.patient", string="Patient")
    date_from  = fields.Date("Date From")
    date_to = fields.Date("Date To")


    def action_print_excel_report(self):
        
        domain= []
        
        patient_id = self.patient_id
        if patient_id:
            domain  += [('patient_id','=',patient_id.id)]
            
        date_from =  self.date_from
        if date_from:
            domain += [('date_appointment','>=',date_from)]
        
        date_to = self.date_to
        if date_from:
            domain += [('date_appointment','>=',date_to)]
            
        
        appointments = self.env['hospital.appointment'].search_read(domain)
        print("Appointments", appointments)
        
        data = {
            'appointments': appointments,
            'form_data': self.read()[0]
        }
        print("--------------------------form_data---------------------------------\n", data)
        
        return self.env.ref('om_hospital.report_patient_appointments_xls').report_action(self, data=data)


    def action_print_report():
        pass
        
            