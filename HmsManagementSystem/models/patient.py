from odoo import  models , fields


class Patient(models.Model):
    _name = "hms.patient.system"
    _description = "Hospital Management System"

    fname = fields.Char()
    lname = fields.Char()
    birthday = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()

    blood_type = fields.Selection(
        [('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('ab+', 'AB+'), ('ab-', 'AB-'), ('o+', 'O+'),
         ('o-', 'O-')],

    )
    pcr = fields.Boolean(string='PCR')
    image_upload = fields.Binary()
    address = fields.Char()
    age = fields.Integer()






