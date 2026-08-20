# Copyright (c) 2026, Mithun and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.types import DF  # DF - DocField

class Restaurant(Document):
	restaurant_name : DF.Data
	restaurant_id : DF.Data
	restaurant_ratings : DF.Int

	def validate(self):
		if len(self.restaurant_id) > 10:
			frappe.throw("Restaurant ID should not exceed 10 characters");

		if frappe.db.exists(
			"Restaurant" ,
			{
				"restaurant_id" : self.restaurant_id,
				"name" : ["!=" , self.name]
			}
		):
			frappe.throw("Restaurant with this ID already exists")

	def on_update(self):
		print("Restaurant updated")

	def on_trash(self):
		print("Restaurant trashed")

	def on_save(self):
		print("Restaurant saved")

