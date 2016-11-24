# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import msgprint
from frappe.model.mapper import get_mapped_doc
from frappe.utils import cstr, flt, getdate, new_line_sep

def validate(doc,method):
	if doc.taxa_cambio:

		print flt(doc.rounded_total) / flt(doc.taxa_cambio)
		doc.contra_valor = round(flt(doc.rounded_total) / flt(doc.taxa_cambio),2)
		

