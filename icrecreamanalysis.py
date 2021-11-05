#
# Analysis if the ice cream dataset.
#

file = open("ice_cream.csv")
ice_cream_eaters = {}
line_num = 0
for line in file:
    line = line.rstrip()
    if line_num == 0:
        headers = line.split(",")
        headers.pop(0)
    else:
        ice_cream_eater = line.split(",")
        id = ice_cream_eater.pop(0)
        zipped_eater = zip(headers,ice_cream_eater)
        ice_cream_eaters[id] = dict(zipped_eater)
        # for key, value in zipped_eater:
        #     eater_dict
        # ice_cream_eaters[id] = tuple(ice_cream_eater)
    line_num += 1

