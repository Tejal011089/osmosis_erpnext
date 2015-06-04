// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

cur_frm.add_fetch('customer','customer_name','customer_name');
cur_frm.add_fetch('lead','lead_name','customer_name');
//cur_frm.add_fetch('customer_address','lead_name','customer_name');



cur_frm.fields_dict['customer_address'].get_query = function(doc, dt, dn) {
	if (doc.customer)
		return{
			filters:{'customer': doc.customer}
		}
	else
		return{
			filters:{'lead': doc.lead}
		}

}

cur_frm.cscript.customer_address = function(doc,dt,dn) {
	//var d = locals[dt][dn];
	if(doc.customer_address) {
		return frappe.call({
			method: "erpnext.selling.doctype.first_inspection_report.first_inspection_report.get_address",
			args: {address: doc.customer_address},
			callback: function(r) {
				console.log(r.message);
				doc.address = r.message;
				refresh_field('address');
			}
		});
	}


}