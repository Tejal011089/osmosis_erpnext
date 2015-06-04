# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class FirstInspectionReport(Document):
	pass

@frappe.whitelist()
def get_address(address):
	frappe.errprint(address)
	if address:
		customer_address=frappe.db.sql("""select concat(ifnull(address_line1,0), ',' ,ifnull(city,0), ',' ,ifnull(country,0), ',' ,ifnull(phone,0)) as address from `tabAddress` 
								where name='%s'"""%address,as_dict=1)
		frappe.errprint(customer_address)

	return  customer_address[0].address