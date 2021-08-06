from webbrowser import get
import eel

class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_count_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code,item_count):
        self.item_order_list.append(item_code)
        self.item_count_list.append(item_count)

    def view_item_list(self):
        eel.blank_order_js()
        for item_code,item_count in zip(self.item_order_list,self.item_count_list):
            item_name,item_price = self.get_item_data(item_code)
            eel.add_order_js(f"{item_name}　{item_price}円 {item_count}個")
    
    def get_item_data(self,item_code):
        for item_data in self.item_master:
            if item_data.item_code == item_code:
                return item_data.item_name,item_data.price
    
    def view_item_data(self,item_code):
        for item_data in self.item_master:
            if item_data.item_code == item_code:
                eel.show_item_data(f"検索された商品：{item_data.item_name} {item_data.price}円")
    
    def total_money(self):
        i = 0
        for item_code,item_count in zip(self.item_order_list,self.item_count_list):
            item_name,item_price = self.get_item_data(item_code)
            i += item_price * int(item_count)
        eel.total_money_js(f"合計金額：{i}")
        return i
    
    def accounting_money(self,input_money):
        self.input_money = input_money
        self.sum = self.total_money()
        self.exchange = int(self.input_money) - self.sum
    
    def output_receipt(self):
        for item_code,item_count in zip(self.item_order_list,self.item_count_list):
            order_item,order_price = self.get_item_data(item_code)
            eel.output_receipt_js(f"{order_item} {order_price}円 {item_count}個")
        eel.output_receipt_js("----------------------")
        eel.output_receipt_js(f"合計金額:　　{self.sum}円")
        eel.output_receipt_js(f"お支払い金額：{self.input_money}円")
        eel.output_receipt_js(f"お釣り：　　　{self.exchange}円")

    def delete_item(self,delete_item_code):
        i = 0
        for item_code,item_count in zip(self.item_order_list,self.item_count_list):
            item_name,item_price = self.get_item_data(item_code)
            if item_code == delete_item_code:
                self.item_order_list.remove(item_code)
                self.item_count_list.pop(i)
            i += 1
        self.view_item_list()