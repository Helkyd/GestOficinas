# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Gestoficinas",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Gestoficinas")
		},

		{
		   "_doctype": "Folha de Obras", 
		   "color": "grey", 
		   "icon": "octicon octicon-file-directory", 
		   "label": "Folha de Obras", 
		   "link": "List/Folha de Obras", 
		   "module_name": "Folha de Obras", 
		   "type": "link"
		  },
		 {
		   "_doctype": "Ordem de Reparacao", 
		   "color": "grey", 
		   "icon": "octicon octicon-file-directory", 
		   "label": "Ordem de Reparacao", 
		   "link": "List/Ordem de Reparacao", 
		   "module_name": "Ordem de Reparacao", 
		   "type": "link"
		  }, 
	]
