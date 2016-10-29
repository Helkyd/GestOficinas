
# Copyright (c) 2016, Helio de Jesus and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

def get_notification_config():
	return { "for_doctype":
		{
			"Folha de Obras": {"fo_status": ['in','Aberta, Em Curso']},
			"Ordem de Reparacao": {"or_status": ['in','Aberta, Em Curso']}

		}
	}


