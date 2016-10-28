# -*- coding: utf-8 -*-
# Copyright (c) 2015, Helio de Jesus and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class FolhadeObras(Document):

	def autoname(self):
		self.numero_obra = make_autoname('FO/' + '.#####' + './.' + 'YYYY')
		self.name = self.numero_obra


@frappe.whitelist()
def get_avaria_cliente(frm,cdt):
	print frappe.get_all("Avarias_Cliente",filters={'Parent':cdt},fields=['Parent','avcliente_descricao'])	
	return frappe.get_all("Avarias_Cliente",filters={'Parent':cdt},fields=['Parent','avcliente_descricao'])

@frappe.whitelist()
def get_avarias_clientes():
	print frappe.get_all("Avarias_Cliente",filters={'Parent':['!=','']},fields=['Parent','avcliente_descricao'])
	return frappe.get_all("Avarias_Cliente",filters={'Parent':['!=','']},fields=['Parent','avcliente_descricao'])

