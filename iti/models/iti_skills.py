from odoo import fields, models


class ItiSkills(models.Model):
    _name = 'iti.skills'
    _description = 'skills info'

    name = fields.Char()
