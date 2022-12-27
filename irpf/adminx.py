from irpf.models import Enterprise, Negotiation, Earnings, Position, Instituition, Provision
from irpf.plugins import ListActionModelPlugin, GuardianAdminPlugin, AssignUserAdminPlugin
from irpf.views.import_list import AdminImportListModelView
from irpf.views.report_irpf import AdminReportIrpfModelView
from xadmin import sites, site
from xadmin.views import ListAdminView, ModelFormAdminView

site.register_plugin(ListActionModelPlugin, ListAdminView)
site.register_view("^irpf/import-listmodel/(?P<model_app_label>.+)/$", AdminImportListModelView,
                   "import_listmodel")
site.register_view("^ifpf/report-irpf/(?P<model_app_label>.+)/$", AdminReportIrpfModelView,
                   "reportirpf")

site.register_plugin(GuardianAdminPlugin, ListAdminView)
site.register_plugin(AssignUserAdminPlugin, ModelFormAdminView)


@sites.register(Instituition)
class InstituitionAdmin:
	list_display = (
		"name",
		"cnpj"
	)


class BaseIRPFAdmin:
	readonly_fields = ("user",)
	# GuardianAdminPlugin
	guardian_protected = True
	# AssignUserAdminPlugin
	assign_current_user = True


@sites.register(Enterprise)
class EnterpriseAdmin:
	list_filter = ("category",)
	search_fields = ("code", "name", "cnpj")
	list_display = (
		'code',
		'category',
		'name',
		'cnpj'
	)


@sites.register(Position)
class PositionAdmin(BaseIRPFAdmin):
	...


@sites.register(Negotiation)
class NegotiationAdmin(BaseIRPFAdmin):
	list_filter = ("kind", "date")
	search_fields = ("code",)
	list_display = (
		"code",
		"kind",
		"institution",
		"quantity",
		"total",
		"date"
	)


@sites.register(Earnings)
class EarningsAdmin(BaseIRPFAdmin):
	list_filter = ("kind", "date")
	search_fields = ("code",)
	list_display = (
		"flow",
		"kind",
		"code",
		"name",
		"institution",
		"quantity",
		"total",
		"date"
	)


@sites.register(Provision)
class ProvisionAdmin(BaseIRPFAdmin):
	search_fields = ("code", "kind")
	list_display = (
		'code',
		'name',
		'date_ex',
		'date_payment',
		'kind',
		'quantity',
		'total'
	)
