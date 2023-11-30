# Copyright (c) 2023, promantia and contributors
# For license information, please see license.txt

import frappe
from frappe import _
import random
import string
from frappe.model.document import Document

class AirplaneTicket(Document):
	
	def before_save(self):
		add_ons = self.add_ons
		total_amount = 0
		for item in add_ons:
			total_amount += item.amount

		self.total_amount=total_amount
		self.total_price = self.total_amount+self.flight_price
		check_capacity(self.airplane)
	
	def before_insert(self):
		airplane_ticket = frappe.db.get_value("Airplane Flight", self.airplane, 'airplane')
		self.airline = frappe.db.get_value("Airplane", airplane_ticket , 'airline')

def check_capacity(flight):
	airplane = frappe.db.get_value("Airplane Flight", flight, "airplane")
	capacity = frappe.db.get_value("Airplane", airplane, "capacity")
	ticket_count = frappe.db.count("Airplane Ticket", {"airplane": flight, "docstatus": 1})
	
	if ticket_count > capacity:
    	   frappe.throw(_("The number of tickets for this flight has reached its capacity. Cannot create a new ticket"))

		

		 
	 
 






    
    
 




		
	

	 

	 





 