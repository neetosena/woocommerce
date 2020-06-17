import csv
import shutil
from tempfile import NamedTemporaryFile
from pprint import pprint
import codecs
import class_csv
import pandas as pd

data1 = class_csv.Woocommerce()
data1.file_name2 = "name_file.csv"
data1.ids_number = 5746
data1.name = "title of the file"
data1.short_description = "short description"
data1.categories = "Safety"
data1.images = "https://yoururl.ie/safety-14.jpg"


data1.type_material = ['Corribord', 'UV Direct Print', 'Dibond',
                       'Stickers Gloss Laminated']
data1.quantity_type = ['10', '25', '30', '35', '40']
data1.size = ['610mm x 460mm']
data1.qtd_products_materials = 4
data1.qtd_size = 1


data1.price = [8.00, 4.00, 10.08, 5.04]


# -------------------------------------------------------------------------------


with open(data1.file_name2, 'w', newline='') as f:
    field_names = ['ID', 'Type', 'SKU', 'Name', 'Published', 'Is featured?',
                   'Visibility in catalog', 'Short description', 'Date sale price starts', 'Date sale price ends', 'Tax status',
                   'Tax class', 'In stock?', 'Stock', 'Low stock amount', 'Backorders allowed?', 'Sold individually?', 'Weight (g)', 'Length (cm)',
                   'Width (cm)', 'Height (cm)', 'Allow customer reviews?', 'Purchase note', 'Sale price', 'Regular price', 'Categories', 'Tags', 'Shipping class',
                   'Images', 'Download limit', 'Download expiry days', 'Parent', 'Grouped products', 'Upsells', 'Cross-sells', 'External URL',
                   'Button text', 'Position', 'Attribute 1 name', 'Attribute 1 value(s)', 'Attribute 1 visible', 'Attribute 1 global', 'Attribute 2 name',
                   'Attribute 2 value(s)', 'Attribute 2 visible', 'Attribute 2 global', 'Attribute 3 name', 'Attribute 3 value(s)', 'Attribute 3 visible',
                   'Attribute 3 global', 'Attribute 4 name', 'Attribute 4 value(s)', 'Attribute 4 visible', 'Attribute 4 global']

    themwriter = csv.DictWriter(f, fieldnames=field_names)
    themwriter.writeheader()
    themwriter.writerow({'ID': data1.ids_number, 'Type': data1.type_, 'Name': data1.name, 'Published': data1.published, 'Is featured?': data1.is_featured, 'Visibility in catalog': data1.visibility, 'Short description': data1.short_description, 'Tax status': data1.tax_status, 'In stock?': data1.in_stock, 'Backorders allowed?': data1.back_order,
                         'Sold individually?': data1.sold_individual, 'Allow customer reviews?': data1.allow_cust_reviews, 'Categories': data1.categories, 'Images': data1.images, 'Position': data1.position, 'Shipping class': data1.shipping_class,
                         'Attribute 1 name': data1.attribute, 'Attribute 1 value(s)': data1.gwt_header_of_header(data1.quantity_type), 'Attribute 1 visible': data1.attribute_1_visible, 'Attribute 1 global': data1.attribute_1_global, 'Attribute 2 name': data1.attribute_2_name, 'Attribute 2 value(s)': data1.gwt_header_of_header(data1.size), 'Attribute 2 visible': data1.attribute_2_visible, 'Attribute 2 global': data1.attribute_2_global, 'Attribute 3 name': data1.attribute_3_name, 'Attribute 3 value(s)': data1.gwt_header_of_header(data1.type_material),
                         'Attribute 3 visible': data1.attribute_3_visible, 'Attribute 3 global': data1.attribute_3_global})
