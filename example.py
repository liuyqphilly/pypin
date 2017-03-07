"""client script"""
import pypin

api = pypin.API("")

print (api.get_me())

print (api.get_boards())

# print API_CLIENT.create_board({'name': 'test3'})

# print API_CLIENT.create_pin({
#     'board': 'yvesfu/test3',
#     'note': 'a new pin',
#     'link': 'https://www.spartasales.com',
#     'image_url': 'http://img.over-blog-kiwi.com/0/86/68/47/20140304/ob_9b442c_baby-115a.jpg'
# })
