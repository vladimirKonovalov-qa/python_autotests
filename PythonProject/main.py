import requests
import json

token = 'd62ce03fb6aaf83e538b8038214fc938'
'''response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Картошказавр",
    "photo": "https://s252vla.storage.yandex.net/rdisk/59d3848e74a08bfe6d9c54cf87507293977e631a819919109a5c9fa6f0af04bb/638b98f3/-OLcqwDxmgkd24NTgwuo4Fd9ibFUCkYJSXDoQb55FdRjZZWCi_j3ZQvWYqeGwBOueQfPOOnmtN_DGNVbWlGsqA==?uid=0&filename=1511455329230%20%281%29.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&fsize=197872&hid=d0681a7674b827da63fc1ed4ead26803&media_type=image&tknv=v2&etag=64a3d0731f525c9b76587928afd574de&rtoken=JDLLZiHsLJQo&force_default=no&ycrid=na-edacfb8856e576902972793bfc7fa9a5-downloader24f&ts=5eef0d691e2c0&s=ce802ea70029ee2c5f3cb4a66ccfd74b95018da09547c456fd745a2604da373a&pb=U2FsdGVkX1_bkPiGp0C3T-Kd_lMFollWVksZ0uM8-ImmGMDOqK2N3DJyewlax9GpusAC9oaoI96s8YGx0gfw1nO-lSOfTsaPrQboJZHRErE"
})

print(response.text)

response = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1325,
    "name": "Кубон",
    "photo": "https://s499sas.storage.yandex.net/rdisk/f73991d8d7c7ee3d2a69d0177c9e1a85f532e7df3430d25ffbe90aa2b7c17538/638baebf/-OLcqwDxmgkd24NTgwuo4MFVkzlo4aUka9756RuA4_phGfTrdK0evwhUK437kGwjVc6hY1-QXFRjKXxpwH9uSQ==?uid=0&filename=Без%20имени-1.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&fsize=778555&hid=25fef4b862a33c1c1fcbb51842f42b20&media_type=image&tknv=v2&etag=91031496d3e224633ca479bac96e192f&rtoken=n5ydnwLOWrgq&force_default=no&ycrid=na-e872b3349263bb5d4105271af81d1fcb-downloader16e&ts=5eef22329edc0&s=fcbb9b8e227e242d529630930f9315f413e5cf828d5368ce80bb1d7efe1fb7d5&pb=U2FsdGVkX1_oIkqPKSG1gxBRmIVdBpUX2fTD8q7QmS8z2KGjxNMDeAooR5VF13L5l1k1nTlb1C8tm-5XLFlrCbzdK2RSqABFnEKuiMTee3g"
})

print(response.text)

response = requests.post('https://pokemonbattle.me:5000//trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": "1325"
})

print(response.text)'''

response = requests.post('https://pokemonbattle.me:5000//trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": "1327"
})

print(response.text)