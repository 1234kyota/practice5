import eel
import pandas as pd
import desktop
import pos_system

app_name="html"
end_point="index.html"
size=(700,600)

#Itemマスターのインスタンス作成
item_master = []
item_master_df = pd.read_csv('./master.csv',dtype={"item_code":object})
item_master_list = item_master_df.values.tolist()
for item in item_master_list:
    item_master.append(pos_system.Item(item[0],item[1],int(item[2])))

#orderインスタンス作成
order = pos_system.Order(item_master)

@ eel.expose
def view_item_data(item_code):
    order.view_item_data(item_code)

@ eel.expose
def view_item_order_and_total_money(item_code,item_count):
    order.add_item_order(item_code,item_count)
    order.view_item_list()
    order.total_money()

@eel.expose
def accounting_money(input_money):
    order.accounting_money(input_money)
    order.output_receipt()

@eel.expose
def delete_item(delete_order_code):
    order.delete_item(delete_order_code)
    order.total_money()

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)

