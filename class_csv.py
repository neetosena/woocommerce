from pprint import pprint
import math


class Woocommerce:
    file_name2 = "title.csv"
    ids_number = 5670
    type_ = "variable"
    name = "Sign Covid-19 CIF Return to Work"
    published = "1"
    is_featured = "0"
    visibility = "visible"
    short_description = "610mm x 460mm | 800mm x 600mm | 1200mm x 800mm"
    tax_status = "taxable"
    in_stock = "1"
    back_order = "0"
    sold_individual = "0"
    allow_cust_reviews = "1"
    categories = "covid 19"
    shipping_class = "class3"
    images = "https://put-your-url.ie"
    position = "0"
    attribute = "Quantity"

    attribute_1_visible = "1"
    attribute_1_global = "0"

    attribute_2_name = "size"

    attribute_2_visible = "1"
    attribute_2_global = "0"

    attribute_3_name = "Material Types"

    attribute_3_visible = "1"
    attribute_3_global = "0"

    type_material = ['Corribord', 'Foamex PVC', 'Dibond',
                     'Laminated Poster Paper', 'Laminated Vinyl']
    quantity_type = ['1', '10', '15', '25', '30']
    size = ['610mm x 460mm', '800mm x 600mm', '1200mm x 800mm']
    qtd_products_materials = 5
    qtd_size = 3

    price = [8.12, 12.28, 24.56, 9.08, 13.84, 27.64, 10.08, 15.36, 30.72, 5.04, 7.68, 15.36,
             6.08, 9.20, 18.40]

    # -------------------------------------------------------------------------------Function to calculate simple Price per quantity----------------------------------------------------------------------
    # 1 = Supplier Price x 2.5
    # 2 = Supplier Price x 2.45
    # 3 = Supplier Price x 2.4
    # 4 = Supplier Price x 2.35
    # 5 = Supplier Price x 2.3
    # 10 = Supplier Price x 2.2
    # 15 = Supplier Price x 2.15
    # 20 = Supplier Price x 2.1
    # 25 = Supplier Price x 2.05
    # 30 = Supplier Price x 2
    # 35 = Supplier Price x 1.95
    # 40 = Supplier Price x 1.9
    # 45 = Supplier Price x 1.9
    # 50 = Supplier Price x 1.85

    def calculate_with_quantity(self, num):
        # calculate what is the difference between the thrid column with second column is 112.5%
        number_conv_to_2_column = (num * 1.125)
        # calculate what is the difference between the thrid column with first column is 1.25
        number_conv_to_1_column = (num * 1.25)

        new_number_1 = number_conv_to_1_column * 2.5
        new_number_2 = number_conv_to_2_column * 2.45
        new_number_3 = number_conv_to_2_column * 2.4
        new_number_4 = number_conv_to_2_column * 2.35
        new_number_5 = number_conv_to_2_column * 2.3
        new_number_6 = num * 2.2
        new_number_7 = num * 2.15
        new_number_8 = num * 2.1
        new_number_9 = num * 2.05
        new_number_10 = num * 2
        new_number_11 = num * 1.95
        new_number_12 = num * 1.9
        new_number_13 = num * 1.85

        list_ = list()

        # convert string list in int list using map
        quantity_type_float = list(map(float, self.quantity_type))
        j = 0
        for x in range(len(quantity_type_float)):

            if (quantity_type_float[x] < 2):
                j = quantity_type_float[x] * new_number_1
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] == 2):
                j = quantity_type_float[x] * new_number_2
                # list_.append("{:0.2f}".format(quantity_type_float[x] * num3))
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] == 3):
                j = quantity_type_float[x] * new_number_3
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] == 4):
                j = quantity_type_float[x] * new_number_4
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] == 5):
                j = quantity_type_float[x] * new_number_5
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] <= 10):
                j = quantity_type_float[x] * new_number_6
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] <= 15):
                j = quantity_type_float[x] * new_number_7
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] <= 20):
                j = quantity_type_float[x] * new_number_8
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] <= 25):
                j = quantity_type_float[x] * new_number_9
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] <= 30):
                j = quantity_type_float[x] * new_number_10
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] <= 35):
                j = quantity_type_float[x] * new_number_11
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] <= 40):
                j = quantity_type_float[x] * new_number_12
                list_.append(math.ceil(j))

            elif (quantity_type_float[x] > 40):
                j = quantity_type_float[x] * new_number_13
                list_.append(math.ceil(j))

        return list_

    def calculate_all_the_prices(self):
        number_var = self.qtd_products_materials * self.qtd_size
        list_ = list()

        for i in range(number_var):
            list_.append(self.calculate_with_quantity(self.price[i]))

        return list_

    def organize_param(self, y):
        list_ = list()
        list_2 = list()
        list_.append(y)
        for i in range(2):
            x = self.qtd_size + y
            y = x + self.qtd_size
            list_.append(x)
            list_.append(y)

        for j in range(self.qtd_products_materials):
            list_2.append(list_[j])

        return list_2

    def organize_all_prices(self):
        number_var = self.qtd_products_materials * self.qtd_size
        list_ = list()
        for j in range(self.qtd_size):
            for x in range(self.qtd_products_materials):
                for y in range(number_var):
                    if (y == self.organize_param(j)[x]):
                        list_.append(self.calculate_all_the_prices()[y])
        return list_

    def organize_all_prices_in_1_list(self):
        list_ = self.organize_all_prices()
        list_2 = list()
        for j in range(len(self.quantity_type)):
            for x in list_:
                list_2.append(x[j])
        return list_2

# -----------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_calc_total_product(self):
        quantity_type_number = len(self.quantity_type)
        return int(self.qtd_products_materials * self.qtd_size * quantity_type_number)

    def gwt_header_of_header(self, header):
        comma = ", "
        return comma.join(header)

    def get_ids_(self):
        num = 0
        list_ = list()
        for x in range(1, self.get_calc_total_product()+1):
            num = self.ids_number + x
            list_.append(num)
        return list_

    def number_or_text_repeatedly(self, text):
        list_ = list()
        for x in range(1, self.get_calc_total_product()+1):
            list_.append(text)
        return list_

    def numbers_continue_(self, num):
        list_ = list()
        number = 0
        number = num
        num2 = 0
        for x in range(self.get_calc_total_product()):
            num2 = number + x
            list_.append(num2)

        return list_

    def get_quantity_variation(self):
        list_ = list()
        quantity_type_int_range = len(self.quantity_type)
        number_var = self.qtd_products_materials * self.qtd_size

        # convert string list in int list using map
        quantity_type_int = list(map(int, self.quantity_type))
        for x in range(quantity_type_int_range):
            for y in range(number_var):
                num2 = quantity_type_int[x]
                list_.append(num2)

        return list_

    def get_quantity_size(self):
        list_ = list()
        quantity_type_int_range = len(self.quantity_type)
        for i in range(quantity_type_int_range):
            for x in range(len(self.size)):
                for y in range(self.qtd_products_materials):
                    list_.append(self.size[x])
        return list_

    def get_quantity_type(self):
        list_ = list()
        quantity_type_int_range = len(self.quantity_type)
        for j in range(len(self.size)):
            for x in range(quantity_type_int_range):
                for y in range(len(self.type_material)):
                    list_.append(self.type_material[y])

        return list_

