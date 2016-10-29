# -*- coding: utf-8 -*-
# Copyright (c) 2015, Helio de Jesus and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from datetime import datetime, timedelta
from frappe.utils import cstr, get_datetime, getdate, cint, get_datetime_str
import codecs

class FolhadeObras(Document):

	def autoname(self):
		self.numero_obra = make_autoname('FO/' + '.#####' + './.' + 'YYYY')
		self.name = self.numero_obra


	def validate(self):
		self.criar_projecto()




	def criar_projecto(self):
		if self.fo_status == "Em Curso":
			projecto = frappe.get_doc({
				"doctype": "Project",
				"project_name": self.numero_obra,
				"priority": "Medium",
				"status": "Open",
				"expected_start_date": get_datetime(frappe.utils.now()) + timedelta(days=1) ,
				"is_active": "Yes",
				"project_type": "Internal",
				"customer": self.nome_cliente
			})
			projecto.insert()
			frappe.msgprint('{0}{1}'.format("Numero da Folha de Obra criada como Projeto ", self.numero_obra))
			#create the Tasks
			i=0
			d=self.avarias_cliente
			while i <> -1:
				posic = d.find('\n', i,len(d)+1)
				if posic != -1:
					palavratmp = d[0:posic]
					d = d[posic:len(d)]
					i = posic
				else:
					palavratmp= d
					i =-1
				#print str(palavratmp.encode('utf-8'))
				if palavratmp !='':
					tarefas = frappe.get_doc({
						"doctype": "Task",
						"project": self.numero_obra,
						"subject": palavratmp.encode('utf-8'),
						"status": "Open",
						"description": "Tarefa adicionada pelo Sistema",
						"exp_start_date": get_datetime(frappe.utils.now()) + timedelta(days=1)

					})
					tarefas.insert()
					frappe.msgprint('{0}{1}'.format(palavratmp.encode('utf-8'), " Criada como tarefa no Projecto ", self.numero_obra))
			


@frappe.whitelist()
def get_avaria_cliente(frm,cdt):
	print frappe.get_all("Avarias_Cliente",filters={'Parent':cdt},fields=['Parent','avcliente_descricao'])	
	return frappe.get_all("Avarias_Cliente",filters={'Parent':cdt},fields=['Parent','avcliente_descricao'])

@frappe.whitelist()
def get_avarias_clientes():
	print frappe.get_all("Avarias_Cliente",filters={'Parent':['!=','']},fields=['Parent','avcliente_descricao'])
	return frappe.get_all("Avarias_Cliente",filters={'Parent':['!=','']},fields=['Parent','avcliente_descricao'])



