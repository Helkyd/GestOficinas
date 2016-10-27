# -*- coding: utf-8 -*-
# Copyright (c) 2015, Helio de Jesus and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class MarcaCarros(Document):

	def autoname(self):
		self.name = make_autoname(self.marca + '-' + '.#####')
		frappe.throw(_("Cliente Conta-Corrente nao selecionado !!!! A MESA mantem-se aberta."))


