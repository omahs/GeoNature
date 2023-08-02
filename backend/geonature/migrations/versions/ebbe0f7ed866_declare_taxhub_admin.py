"""declare taxhub TAXHUB

Revision ID: ebbe0f7ed866
Revises: f1dd984bff97
Create Date: 2023-08-02 13:15:38.542530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ebbe0f7ed866"
down_revision = "f1dd984bff97"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        INSERT INTO gn_commons.t_modules
        (module_code, module_label, module_picto, module_desc, module_external_url, module_target, active_frontend, active_backend)
        VALUES('TAXHUB', 'Taxhub', 'fa-leaf', 'Module TaxHin',  'test', '_blank', false, false);

        INSERT INTO gn_permissions.t_objects
        (code_object, description_object)
        VALUES
        ('TAXON', 'Gestion des taxons dans TaxHub'),
        ('THEME', 'Gestion des thêmes d''attribut dans TaxHub'),
        ('MEDIA', 'Gestion des médias dans TaxHub'),
        ('LISTE', 'Gestion des listes dans TaxHub'),
        ('ATTRIBUT', 'Gestion des types d''attributs dans TaxHub')
        ;


        INSERT INTO
            gn_permissions.t_permissions_available (
                id_module,
                id_object,
                id_action,
                scope_filter,
                label
            )
        SELECT
            m.id_module,
            o.id_object,
            a.id_action,
            v.scope_filter,
            v.label
        FROM (
                VALUES
                 ('TAXHUB', 'TAXON', 'R', False, 'Voir les taxons')
                ,('TAXHUB', 'TAXON', 'U', False, 'Modifier les taxons (médias - liste - attributs)')
                ,('TAXHUB', 'THEME', 'C', False, 'Créer des thêmes')
                ,('TAXHUB', 'THEME', 'R', False, 'Voir les thêmes')
                ,('TAXHUB', 'THEME', 'U', False, 'Modifier les thêmes')
                ,('TAXHUB', 'THEME', 'D', False, 'Supprimer des thêmes')
                ,('TAXHUB', 'MEDIA', 'R', False, 'Voir les médias')
                ,('TAXHUB', 'MEDIA', 'U', False, 'Modifier les médias')
                ,('TAXHUB', 'MEDIA', 'D', False, 'Supprimer les médias')
                ,('TAXHUB', 'LISTE', 'C', False, 'Creer des listes')
                ,('TAXHUB', 'LISTE', 'R', False, 'Voir les listes')
                ,('TAXHUB', 'LISTE', 'U', False, 'Modifier les listes')
                ,('TAXHUB', 'LISTE', 'D', False, 'Supprimer des listes')
                ,('TAXHUB', 'ATTRIBUT', 'C', False, 'Créer des types d''attribut')
                ,('TAXHUB', 'ATTRIBUT', 'R', False, 'Voir les types d''attribut')
                ,('TAXHUB', 'ATTRIBUT', 'U', False, 'Modfier les types d''attribut')
                ,('TAXHUB', 'ATTRIBUT', 'D', False, 'Supprimer les types d''attribut')
            ) AS v (module_code, object_code, action_code, scope_filter, label)
        JOIN
            gn_commons.t_modules m ON m.module_code = v.module_code
        JOIN
            gn_permissions.t_objects o ON o.code_object = v.object_code
        JOIN
            gn_permissions.bib_actions a ON a.code_action = v.action_code
        WHERE m.module_code = 'TAXHUB'
    """
    )


def downgrade():
    op.execute(
        "DELETE FROM gn_permissions.t_permissions_available WHERE id_module = (SELECT id_module FROM gn_commons.t_modules WHERE module_code = 'TAXHUB')"
    )
