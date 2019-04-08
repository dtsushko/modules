from odoo import models, fields


class Person(models.Model):
    _name = 'person.person'
    age = fields.Integer()
    country = fields.Char()

    def set_name(self):
        return self._name
