# pip install Faker

from faker import Faker
fake = Faker('ko_KR')
fake.seed_instance(4321)
print(fake.name())

# fake_ko = Faker('ko_KR')
# print(fake_ko.name())

# fake2 = Faker('ko_KR')
# print(fake2.name())
