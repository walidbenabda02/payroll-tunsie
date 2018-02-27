from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp


class hr_contract(models.Model):
    _inherit = 'hr.contract'

    nationalite = fields.Char('Nationalite', size=64)
    qualif = fields.Char('Qualification', size=64)
    niveau = fields.Char('Niveau', size=64)
    coef = fields.Char('Coefficient', size=64)


class res_company(models.Model):
    _inherit = 'res.company'

    plafond_secu = fields.Float('Plafond de la Securite Sociale', digits_compute=dp.get_precision('Payroll'))
    nombre_employes = fields.Integer('Nombre d\'employes')
    cotisation_prevoyance = fields.Float('Cotisation Patronale Prevoyance', digits_compute=dp.get_precision('Payroll'))
    org_ss = fields.Char('Organisme de securite sociale', size=64)
    conv_coll = fields.Char('Convention collective', size=64)


class hr_payslip(models.Model):
    _inherit = 'hr.payslip'

    payment_mode = fields.Char('Mode de paiement', size=64)


class hr_employee(models.Model):
    _inherit = 'hr.employee'

    matricule_cnss = fields.Integer('Matricule CNSS', size=10)
    num_chezemployeur =fields.Integer('Numero chez l\'employeur')