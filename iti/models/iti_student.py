from odoo import models, fields,api

class ItiStudent(models.Model):
    _name = "iti.student"
    _description = "student info"

    name = fields.Char(required=True)
    email = fields.Char()
    birth_date = fields.Date()
    salary = fields.Float()
    tax = fields.Float()
    address = fields.Text()
    gender = fields.Selection(
        [('m', 'male'), ('f', 'female')]
    )
    image = fields.Binary()
    cv = fields.Html()
    age = fields.Integer()

    track_id=fields.Many2one('iti.track')
    track_capacity=fields.Integer(related="track_id.capacity")

    skills_id=fields.Many2many('iti.skills')
    student_grade_id = fields.One2many('student.grade', 'student_id')

    @api.onchange("gender")
    def _on_change(self):
        domain = {'track_id': [()]}
        if self.gender == 'm':
            domain = {'track_id': [('isOpen', '=', True)]}
            self.salary = 10000
        else:
            self.salary = 5000
        return {
            'warning': {
                'title': 'Hello',
                'message': 'You have changed the gender',
        },
            'domain':  domain
        }



    class StudentGrades(models.Model):
        _name = "student.grade"

        student_id = fields.Many2one('iti.student')
        course_id = fields.Many2one('iti.course')

        degree=fields.Selection(
            [('excellent','Excellent'),
            ('very good','Very Good'),
            ('good','Good'),
            ('pass','Pass'),
            ('fail','Fail')]
        )

        class ItiCourse(models.Model):
            _name = "iti.course"
            name = fields.Char()

            student_grade_id = fields.One2many('student.grade', 'course_id')
