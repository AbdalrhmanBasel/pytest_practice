
list1 = ['http://www.google.com/images', 'https://ca.google.com/images' ,'https://www.google.com/images'
         ,'http://uk.google.com/images','https://www.google.com/images']


list1 = [item.replace('http://', 'https://') for item in list1]

for item in list1:
    if not 'www' in item:
        old_item = item
        v = str(item[8:10])
        new_item = item.replace(v, 'www')
        list1.append(new_item)
        list1.remove(old_item)

print(list1)
