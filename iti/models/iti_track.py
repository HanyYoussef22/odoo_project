from odoo import models, fields


class ItiTrack(models.Model):
    _name = 'iti.track'
    _description = 'track info'

    # _rec_name = 'name'

    name = fields.Char()
    capacity = fields.Integer()
    isOpen = fields.Boolean()
    student_id = fields.One2many('iti.student','track_id')

