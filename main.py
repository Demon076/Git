import json
from functools import reduce
with open("animals.json", "r") as read_file:
    data = json.load(read_file)
birds = filter(lambda u: u["animal_type"]=="Bird",data)
print('Птицы',list(birds))
active = filter(lambda u: u["active_time"]=="Diurnal",data)
print('Количество дневных животных',len(list(active)))
weight=min(data,key=lambda x:x['weight_min'])
print('Животное с минимальным весом',weight['name'])


