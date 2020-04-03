from odoo import api, fields, models, _
import time
import logging

class CustomContract(models.Model):
    _inherit = 'hr.contract'
    
    
    overtime_included = fields.Integer('Overtime Included')
    transportation_allowance = fields.Float('Tunjangan Transportasi')
    kelas_bpjs = fields.Selection([('1','Kelas 1'),
                                   ('2','Kelas 2'),
                                   ('3','Kelas 3'),
                                   ('4','Sesuai Default')], string= 'Kelas BPJS Kesehatan')
    