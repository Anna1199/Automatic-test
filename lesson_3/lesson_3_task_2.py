from smartphone import Smartphone
phone1=Smartphone('iPhone', '15 Pro', '+79871234567')

phone2=Smartphone('iPhone', '15 ProMax', '+79871223397')

phone3=Smartphone('Vivo', 'v27e', '+793171234527')

phone4=Smartphone('Samsung', 'Galaxy', '+79871098567')

phone5=Smartphone('Honer', 'test', '+79871234110')

catalog=[phone1, phone2, phone3, phone4, phone5]

for phone in catalog:
    print(phone.brand, '-', phone.model, '.', phone.phone_numb)