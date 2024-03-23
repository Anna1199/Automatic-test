from address import Address
from mailing import Mailing

to_address=Address('123123','Georogia','Lenina', '67', '1')
from_address=Address('446765','Russia','Lenina', '67', '1')
my_mailing=Mailing(to_address, from_address, 1000, '№ 123')

print(f'Sending {my_mailing.track} from {my_mailing.from_address.index}, {my_mailing.from_address.city}, {my_mailing.from_address.steet}, {my_mailing.from_address.home}-{my_mailing.from_address.unit} to {my_mailing.to_address.index}, {my_mailing.to_address.city}, {my_mailing.to_address.home}-{my_mailing.to_address.unit}. Cost {my_mailing.cost} money.')