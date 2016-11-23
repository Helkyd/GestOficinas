frappe.ui.form.on("Sales Order","cambio_bna", function(frm,cdt,cdn) {

	frappe.call({
		async: false,
		method: "gestoficinas.gestoficinas.doctype.cambios.cambios",
		args: {
			"fonte":"BNA"				
		},
		callback: function(r) {
			taxavenda = r.message
			cur_frm.doc.taxa_cambio = taxavenda[1]
			refresh_field("taxa_cambio")
		}
	});


});


cur_frm.cscript.custom_validate = function(doc, dt, dn) {

    if (doc.docstatus == 0){

		if (frappe.datetime.get_day_diff(new Date(), frappe.datetime.str_to_obj(doc.transaction_date)) > 0 && doc.order_type == "Sales") {
			//Due to normal clients this have to be removed for now....
			//validated = false;

			//msgprint("Data de Ordem de Venda nao pode ser anterior de hoje"); // or any other message you want..

		}

	}	

};
