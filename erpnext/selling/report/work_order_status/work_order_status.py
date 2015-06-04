# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	order_details=get_sales_order_details()
	#sl_entries = get_sales_order_details(filters)
	#frappe.errprint(sl_entries)
	
	data = []
	#order_details=[]
	return columns, order_details

def get_columns():
	return [_("Work Order number") + ":Link/Sales Order:130",_("Order date") + ":Datetime:90",  _("Client Name") + ":Link/Customer:100",
		 _("Scope Of Work") + ":Link/Project:100",_("Order value") + ":Currency:100", _("Additional Work value") + ":Currency:100", _("Total Work Order Value") + ":Currency:100",
		 _("Mkt. Person") + ":Link/Sales Person:110",
		 _("Target To Start") + ":Datetime:110", _("Target To finish") + ":Datetime:110",
		_("Actual Start Date") + ":Datetime:110", _("Actual End Date") + ":Datetime:95",_("Work Status") + ":Data:95"]


def get_sales_order_details():
	return frappe.db.sql("""select so.name, so.transaction_date,so.Customer,so.project_name,
		so.total,so.total,so.grand_total,
		(select sales_person from `tabSales Team` where parent= so.name limit 1),
		p.expected_start_date,p.expected_end_date,p.expected_start_date,p.expected_end_date,p.status 
		from `tabSales Order` so join `tabProject` p on p.name=so.project_name """,as_list=1)
	


