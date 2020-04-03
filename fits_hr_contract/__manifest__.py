{
    "name": "Fits Custom Contract",
    "version": "1.0", 
    "depends": [
        "base","hr","hr_contract","base_action_rule"
    ],
    "author": "Fits! Team - by PT. Fujicon Priangan Perdana",
    "category": "",
    'website': "http://fujicon-japan.com",
    "description": """\

   Penambahan Bidang OT Included, Tujangan Transportasi, Kelas BPJS

""",
    "data": [
        "views/hr_contract_view.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}