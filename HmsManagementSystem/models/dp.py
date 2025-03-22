from odoo import fields , models

class Department(models.Model):
    _name = 'hms.dp'
    _description = "department info"


    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patient_id = fields.One2many('hms.patient.system','department_id')