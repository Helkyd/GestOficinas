// Copyright (c) 2016, Helio de Jesus and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ordem de Reparacao', {
	onload: function(frm) {
	

//		cur_frm.toggle_enable("or_date",false)
		cur_frm.toggle_enable("or_operador",false)
		cur_frm.toggle_enable("or_marca_veiculo",false)
		cur_frm.toggle_enable("or_modelo_veiculo",false)
		cur_frm.toggle_enable("or_numero_chassi",false)
		cur_frm.toggle_enable("or_numero_motor",false)
		cur_frm.toggle_enable("or_ano_veiculo",false)
	}
		
});

frappe.ui.form.on('Ordem de Reparacao', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on('Ordem de Reparacao','or_nome_cliente',function(frm,cdt,cdn){

	frappe.model.set_value(cdt,cdn,'or_operador',frappe.session.user)
	if (cur_frm.doc.or_nome_cliente){
		customer_('Address',cur_frm.doc.or_nome_cliente+ "-Billing")
		cur_frm.refresh_fields('or_client_number');
	}


});

frappe.ui.form.on('Ordem de Reparacao','or_matricula',function(frm,cdt,cdn){
	
	veiculos_('Veiculos',cur_frm.doc.or_matricula)
	cur_frm.refresh_fields('or_marca_veiculo');


});


var customer_ = function(frm,cdt,cdn){
	frappe.model.with_doc(frm, cdt, function() { 
		var endereco = frappe.model.get_doc(frm,cdt)
		if (endereco){
			cur_frm.doc.or_client_number = endereco.phone
			cur_frm.doc.or_email_cliente = endereco.email_id
		//Check if has car already registered ....
		}
		cur_frm.refresh_fields();

	});


}

var veiculos_ = function(frm,cdt,cdn){
	frappe.model.with_doc(frm, cdt, function() { 
		var carro = frappe.model.get_doc(frm,cdt)
		if (carro){
			cur_frm.doc.or_marca_veiculo = carro.marca
			cur_frm.doc.or_modelo_veiculo = carro.modelo
			cur_frm.doc.or_numero_chassi = carro.veiculo_numero_chassi
			cur_frm.doc.or_numero_motor = carro.veiculo_codigo_motor
			cur_frm.doc.or_ano_veiculo = carro.veiculo_ano
		}
		
		cur_frm.refresh_fields();

	});


}

