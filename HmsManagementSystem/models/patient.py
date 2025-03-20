from odoo import models, fields, api
from odoo.exceptions import UserError

class Patient(models.Model):
    _name = "hms.patient.system"
    _description = "Hospital Management System"

    fname = fields.Char(required=True)
    lname = fields.Char(required=True)
    birthday = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection(
        [('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('ab+', 'AB+'), ('ab-', 'AB-'), ('o+', 'O+'), ('o-', 'O-')],
    )
    pcr = fields.Boolean(string='PCR')
    image_upload = fields.Binary()
    address = fields.Char()
    age = fields.Integer()
    doctor_id = fields.Many2many('hms.doctor', readonly=True)
    department_id = fields.Many2one('hms.dp')
    department_capacity = fields.Integer(related="department_id.capacity")




    @api.onchange('department_id')
    def _onchange_department_id(self):
        if self.department_id:
            self.doctor_id = [(6, 0, self.department_id.doctor_ids.ids)]
            self.doctor_id.readonly = False
        else:
            self.doctor_id = [(5, 0, 0)]
            self.doctor_id.readonly = True

    @api.onchange('pcr')
    def _onchange_pcr(self):
        self.cr_ratio.required = self.pcr

    @api.onchange('age')
    def _onchange_age(self):
        if self.age < 50:
            self.history = False
        if self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    'title': "PCR Checked",
                    'message': "PCR field has been automatically checked because the age is lower than 30."
                }
            }