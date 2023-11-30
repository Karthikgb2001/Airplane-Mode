// Copyright (c) 2023, promantia and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh(frm) {
        frm.add_custom_button("Assign Seat", () => {
            let dialog = new frappe.ui.Dialog({
                title: "Select Seat",
                fields: [
                    {
                        label: __("Seat Number"),
                        fieldname: "seat_number",
                        fieldtype: "Data",
                        reqd: true
                    }
                ],
                primary_action: function() {
                    let seatNumber = dialog.get_value("seat_number");
                    frm.set_value("seat", seatNumber);
                    dialog.hide();
                }
            });
            dialog.show();
        });
    },
    // before_save: function(frm){
    //     frappe.call({
    //         method: "airplane_mode.airplane_mode.doctype.airplane_ticket.airplane_ticket.check_capacity",
    //         args: {
    //             flight: frm.doc.airplane
    //         }
    //     }) 
    // }
});
