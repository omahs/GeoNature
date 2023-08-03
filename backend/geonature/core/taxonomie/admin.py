from apptax.admin.admin_view import (
    BibListesView,
    TaxrefView,
    TMediasView,
    BibAttributsView,
    BibThemesView,
)
from geonature.core.admin.utils import CruvedProtectedMixin


class CruvedProtectedBibListesView(CruvedProtectedMixin, BibListesView):
    module_code = "TAXHUB"
    object_code = "LISTE"
    extra_actions_perm = {".import_cd_nom_view": "C"}


class CruvedProtectedTaxrefView(CruvedProtectedMixin, TaxrefView):
    module_code = "TAXHUB"
    object_code = "TAXON"


class CruvedProtectedTMediasView(CruvedProtectedMixin, TMediasView):
    module_code = "TAXHUB"
    object_code = "TAXON"


class CruvedProtectedBibAttributsView(CruvedProtectedMixin, BibAttributsView):
    module_code = "TAXHUB"
    object_code = "ATTRIBUT"


class CruvedProtectedBibThemes(CruvedProtectedMixin, BibThemesView):
    module_code = "TAXHUB"
    object_code = "THEME"
