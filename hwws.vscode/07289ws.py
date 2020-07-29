# pip install Faker

from faker import Faker


fake = Faker('ko_KR')
Faker.seed(4321)

print(fake.name())

fake2 = Faker('ko_KR')
print(fake2.name())
