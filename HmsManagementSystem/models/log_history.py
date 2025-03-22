from odoo import fields ,models


class LogHistory(models.Model):
    _name = 'log.history'
    _description = 'Log History info'

    state = fields.Selection(
        [
            ('undetermined','Undetermined'),
            ('Good' , 'Good'),
            ('fair','Fair'),
            ('serious','Serious'),
        ]
    )

    patient_ids =fields.Many2one('hms.patient.system')