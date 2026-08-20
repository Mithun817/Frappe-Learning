import frappe

def my_task():
    print("Sample test to demonstrate the task functionality,\n hello \n world")

def context_data(context):
    print(context)
context_data("dummy data")

@frappe.whitelist()
def tasks():
    rest = frappe.qb.DocType("Restaurant")
    td = frappe.qb.DocType("Test_Document")

    query = frappe.qb.from_(rest).inner_join(td).on(rest.name == td.restaurant_id).select(rest.name,
        rest.restaurant_name,
        rest.ratings)
    results = query.run(as_dict = True)

    if results:
        doc = frappe.get_doc("Restaurant", results[0].name)
        doc.ratings = 1
        doc.save()
        name = [result.name for result in results]

        frappe.db.set_value(
            "Restaurant",
            {"name" : ["in" , name]},
            "ratings",
            1,
            update_modified=False
        )
    return results