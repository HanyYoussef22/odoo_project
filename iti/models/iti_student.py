from odoo import models,fields,api

class ItiStudent(models.Model):
    _name = "iti.student"
    _description = "student info"

    name = fields.Char()
    email = fields.Char()
    birth_date = fields.Date()
    salary = fields.Float()
    tax = fields.Float()
    address = fields.Text()
    gender = fields.Selection(
        [('m', 'male'), ('f', 'female')]
    )
    accepted = fields.Boolean()
    image = fields.Binary()
    cv = fields.Html()

