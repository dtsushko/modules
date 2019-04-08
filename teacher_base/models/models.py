from odoo import fields, models
import person

class Teachers(models.Model):
    _inherit = 'person.person'

    name = fields.Char()
    course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")





class Courses(models.Model):
    _name = 'academy.courses'

    name = fields.Char()
    teacher_id = fields.Many2one('person.person', string="Teacher")