// Copyright (c) 2023, promantia and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airline', {
    refresh: function(frm) { 
		if (frm.doc.website) {
         cur_frm.add_web_link("https://www.airbus.com/en", "Website")
		}
    }
});


/*if (frm.doc.website) {	
	frm.add_custom_button(__('Visit Website'), function() {
		window.open(frm.doc.website);
	}).addClass('btn-primary');
}
*/