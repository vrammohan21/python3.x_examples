import dearpygui.dearpygui as dpg

dpg.create_context()
with dpg.window(label="Warehouse Management"):
    dpg.add_text("Warehouse Dashboard")
    dpg.add_button(label="Manage Inventory")
    dpg.create_viewport(title='Warehouse App', width=600, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()