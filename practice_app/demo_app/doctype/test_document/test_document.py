# Copyright (c) 2026, Mithun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.types import DF

class Test_Document(Document):
	description : DF.Data

	def before_save(self):
		if not self.description:
			self.description = "Default description"

def validate(self , data):
	frappe.msgprint(data)
	frappe.msgprint("ToDo is being validated")