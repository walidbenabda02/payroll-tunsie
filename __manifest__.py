{
    'name': 'Tunisia Payroll',
    'category': 'Localization/Payroll',
    'author': 'Walid ben abda',
    'website': 'https://www.walid-it.tn',
    'category': "Localization",
    'version': '10.0.0.1',
    'depends': ['hr_payroll'],

    'description': """Tunisian Payroll Rules.
======================

   Gestion de la Paie Tunisienne:    
    - Gestion des employés.
    - Gestion des contrats.
    - Configuration et paramètrage
            * Les rubriques de paie :primes,indemnités,avantages,déductions,...
            * Les rubriques cotisable ,imposable , soumise à la prime d'ancienneté  ...
            * Les cotisations : cotisations salariales et patronales CNSS,Mutuelle...
            * Barème de la prime d'ancienneté,cotisations CNSS ...       
    - Calcul de paie selon les normes tunisien : calcul automatique de la prime d'ancienneté,heures supplémentaire,cotisations salariales et patronales,...
    - Gestion des congés  :Calcul automatique des congés non payés à partir du module hr_holidays
    - Comptabilisation de la paie :  configuration des comptes de credit et de débit
    - Reporting : les  bulletins de paie,journale de paie ,Ordres de virement ...
    """,
    'data': [
        'views/l10n_tn_paye_view.xml',
        'data/l10n_tn_paye_data.xml'
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
