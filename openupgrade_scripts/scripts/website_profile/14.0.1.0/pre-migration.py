from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env["ir.ui.view"].search([("key", "=", "website_profile.badge_content")]).unlink()
