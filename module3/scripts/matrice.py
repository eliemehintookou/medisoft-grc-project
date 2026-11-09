# -*- coding: utf-8 -*-
"""Matrice des rôles (RBAC) de MediSoft — référence de la revue des accès.

Chaque rôle métier liste les seuls droits autorisés. Tout droit absent de la
matrice est considéré comme excédentaire lors de la revue.
"""

# Groupes Entra ID sensibles (accès à privilèges ou aux données de santé)
GROUPES_SENSIBLES = {
    "GRP-ADMIN-ENTRA": "Administration de l'annuaire",
    "GRP-SUPPORT-DONNEES-PATIENTS": "Accès aux dossiers patients (support N2)",
    "GRP-OPS": "Équipe Ops (accès infrastructure)",
    "GRP-SECURITE": "Équipe sécurité (outils de sécurité)",
}

# Jeux d'autorisations AWS sensibles
AWS_SENSIBLES = {"AdministratorAccess", "OpsEngineer", "PowerUser"}

# role: (libellé, groupes Entra, droits AWS "compte:permission_set", rôle GitHub, console MediSoft Care)
MATRICE = {
    "DIR":        ("Direction",                      ["GRP-ALL", "GRP-DIRECTION"], [], "aucun", "aucun"),
    "CTO":        ("Directeur technique",            ["GRP-ALL", "GRP-DIRECTION", "GRP-RD", "GRP-RD-LEADS"],
                   ["dev:Developer", "preprod:PowerUser", "prod:ReadOnly"], "owner", "aucun"),
    "RSSI":       ("RSSI",                           ["GRP-ALL", "GRP-SECURITE"],
                   ["dev:SecurityAudit", "preprod:SecurityAudit", "prod:SecurityAudit", "securite:SecurityAudit", "sauvegarde:SecurityAudit"],
                   "member", "lecture-journaux"),
    "DPO":        ("Délégué à la protection des données", ["GRP-ALL", "GRP-DPO"], [], "aucun", "lecture-journaux"),
    "DEV":        ("Développeur",                    ["GRP-ALL", "GRP-RD"], ["dev:Developer", "preprod:ReadOnly"], "member", "aucun"),
    "DEV-LEAD":   ("Lead développeur",               ["GRP-ALL", "GRP-RD", "GRP-RD-LEADS"],
                   ["dev:Developer", "preprod:PowerUser", "prod:ReadOnly"], "maintainer", "aucun"),
    "OPS":        ("Ingénieur Ops",                  ["GRP-ALL", "GRP-OPS"],
                   ["dev:PowerUser", "preprod:PowerUser", "prod:OpsEngineer", "sauvegarde:ReadOnly"], "member", "admin-plateforme"),
    "OPS-LEAD":   ("Responsable Ops",                ["GRP-ALL", "GRP-OPS", "GRP-ADMIN-ENTRA"],
                   ["dev:PowerUser", "preprod:PowerUser", "prod:OpsEngineer", "sauvegarde:OpsEngineer", "securite:ReadOnly"],
                   "owner", "admin-plateforme"),
    "SUP-N1":     ("Support niveau 1",               ["GRP-ALL", "GRP-SUPPORT"], [], "aucun", "support-n1"),
    "SUP-N2":     ("Support niveau 2",               ["GRP-ALL", "GRP-SUPPORT", "GRP-SUPPORT-DONNEES-PATIENTS"], [], "aucun", "support-n2"),
    "COM":        ("Commercial",                     ["GRP-ALL", "GRP-SALES"], [], "aucun", "demo"),
    "MKT":        ("Marketing",                      ["GRP-ALL", "GRP-MARKETING"], [], "aucun", "aucun"),
    "RH":         ("Ressources humaines",            ["GRP-ALL", "GRP-RH"], [], "aucun", "aucun"),
    "FIN":        ("Finance",                        ["GRP-ALL", "GRP-FINANCE"], [], "aucun", "aucun"),
    "JUR":        ("Juridique",                      ["GRP-ALL", "GRP-JURIDIQUE"], [], "aucun", "aucun"),
    "PRESTA-DEV": ("Prestataire développement",      ["GRP-EXT-RD"], ["dev:Developer"], "outside-collaborator", "aucun"),
    "PRESTA-OPS": ("Prestataire Ops",                ["GRP-EXT-OPS"], ["dev:ReadOnly", "preprod:ReadOnly"], "aucun", "aucun"),
}

# Comptes techniques déclarés (registre des comptes de service)
COMPTES_TECHNIQUES = {
    "breakglass-01@medisoft.example": ("Compte d'urgence (bris de glace)", "RSSI",
                                       ["prod:AdministratorAccess", "dev:AdministratorAccess", "preprod:AdministratorAccess",
                                        "securite:AdministratorAccess", "sauvegarde:AdministratorAccess"]),
    "breakglass-02@medisoft.example": ("Compte d'urgence (bris de glace)", "RSSI",
                                       ["prod:AdministratorAccess", "dev:AdministratorAccess", "preprod:AdministratorAccess",
                                        "securite:AdministratorAccess", "sauvegarde:AdministratorAccess"]),
    "svc-backup@medisoft.example": ("Compte de service des sauvegardes", "Resp. Ops", []),
    "svc-ci@medisoft.example": ("Compte de service de la CI/CD", "CTO", []),
}

SEUIL_INACTIVITE_JOURS = 90
