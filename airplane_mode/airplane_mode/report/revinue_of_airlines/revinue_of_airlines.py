# Copyright (c) 2023, promantia and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns, data =[
        {
        "label":"Airline",
        "fieldname":"airline",
        "fieldtype":"link",
    },
        {
        
        "label":"Revinue",
        "fieldname":"revinue",
        "fieldtype":"Currency",
        },],[]
    records = frappe.get_all("Airplane Ticket",fields=["total_price","airline"],filters={"docstatus":1})  
    revinue_by_airline = {}
    for record in records:
        if record.airline in revinue_by_airline:
            revinue_by_airline[record.airline] = revinue_by_airline[record.airline] + record.total_price
        else:
            revinue_by_airline[record.airline] = record.total_price
    
    for airline,revinue in revinue_by_airline.items():
        data.append({"airline":airline,"revinue":revinue})


    return columns, data

