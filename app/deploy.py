""" Скрипт для заполнения базы левыми значениями"""
import random
from typing import List

from faker.providers import BaseProvider

from config.database import get_db
from models.building import Building
from faker import Faker

from models.field import Field
from models.organization import Organization

fake = Faker("ru_RU")

session = next(get_db())

class IndustryProvider(BaseProvider):
    def industry(self):
        industries = [
                # Технологии и IT
    "Веб-разработка",
    "Мобильная разработка",
    "DevOps",
    "Кибербезопасность",
    "Data Science",
    "Искусственный интеллект",
    "Blockchain",
    "Cloud Computing",
    "UI/UX дизайн",
    "QA и тестирование",

    # Финансы и бизнес
    "Бухгалтерия",
    "Аудит",
    "Инвестиции",
    "Банковское дело",
    "Финтех",
    "Страхование",
    "Налоговое планирование",
    "Управленческий консалтинг",
    "Фондовый рынок",

    # Медицина и здоровье
    "Терапия",
    "Хирургия",
    "Стоматология",
    "Педиатрия",
    "Фармацевтика",
    "Медицинские технологии",
    "Телемедицина",
    "Косметология",

    # Образование
    "Высшее образование",
    "Языковые курсы",
    "Онлайн-обучение",
    "Корпоративное обучение",
    "Репетиторство",

    # Торговля и продажи
    "Розничная торговля",
    "Оптовая торговля",
    "E-commerce",
    "Маркетплейсы",
    "Продажи B2B",
    "Продажи B2C",

    # Производство
    "Пищевая промышленность",
    "Автомобилестроение",
    "Электроника",
    "Текстиль",
    "Химическая промышленность",
    "Металлургия",

    # Транспорт и логистика
    "Грузоперевозки",
    "Складская логистика",
    "Авиаперевозки",
    "Морские перевозки",
    "Курьерские услуги",

    # Строительство и недвижимость
    "Жилое строительство",
    "Коммерческая недвижимость",
    "Архитектура",
    "Инженерные системы",
    "Ремонт и отделка",

    # Маркетинг и реклама
    "Digital-маркетинг",
    "SEO",
    "Контент-маркетинг",
    "SMM",
    "PR",
    "Брендинг",

    # Творчество и медиа
    "Кино и телевидение",
    "Музыка",
    "Издательское дело",
    "Журналистика",
    "Фотография",
    "Иллюстрация",

    # Услуги
    "Юридические услуги",
    "Риэлторские услуги",
    "HR-услуги",
    "Клининг",
    "Ремонт техники",

    # Гостиничный бизнес
    "Отели",
    "Рестораны",
    "Кафе",
    "Кейтеринг",
    "Туризм",

    # Сельское хозяйство
    "Растениеводство",
    "Животноводство",
    "Агротехнологии",
    "Виноделие",

    # Энергетика
    "Нефть и газ",
    "Возобновляемая энергетика",
    "Электроэнергетика",
    "Энергосбережение",

    # Наука и исследования
    "Биотехнологии",
    "Нанотехнологии",
    "Космические исследования",
    "Экологические исследования"
        ]
        return self.random_element(industries)

fake.add_provider(IndustryProvider)


def fill_buildiings(count: int = 100) -> List[Building]:
    """Заполнить здания"""
    blds = []
    for i in range(count):
        blds.append(Building(address=fake.address(),
                             lat=fake.latitude(),
                             lngt=fake.longitude()
                             )
                    )

    session.add_all(blds)
    session.flush()
    ids = [bld.id for bld in blds]
    session.commit()

    return blds



def fill_fields(count: int = 999)-> List[Field]:
    """Заполнить сферы деятельности"""
    flds_l1 = []
    for i in range(int(count/3)):
        flds_l1.append(Field(name=fake.industry()
                             )
                    )

    session.add_all(flds_l1)
    session.flush()
    ids_l1 = [fld.id for fld in flds_l1]
    session.commit()

    flds_l2 = []
    for i in range(int(count/3)):
        flds_l2.append(Field(name=fake.industry(),
                          parent_id=random.choice(ids_l1)
                             )
                    )

    session.add_all(flds_l2)
    session.flush()
    ids_l2 = [fld.id for fld in flds_l2]
    session.commit()

    flds_l3 = []
    for i in range(int(count / 3)):
        flds_l3.append(Field(name=fake.industry(),
                             parent_id=random.choice(ids_l2)
                             )
                       )

    session.add_all(flds_l3)
    session.flush()
    ids_l3 = [fld.id for fld in flds_l3]
    session.commit()

    return flds_l1+flds_l2+flds_l3

def fill_organizations(b_ids: list, f_ids: list):
    """ЗАполнить организации"""
    orgs = []
    for bld in b_ids:
        orgs.append((Organization(name=fake.company(),
                     number=fake.phone_number(),
                     building=bld,
                     fields=[random.choice(f_ids)])))
        orgs.append((Organization(name=fake.company(),
                                  number=fake.phone_number(),
                                  building=bld,
                                  fields=[random.choice(f_ids)])))
        orgs.append((Organization(name=fake.company(),
                                  number=fake.phone_number(),
                                  building=bld,
                                  fields=[random.choice(f_ids)])))

    session.add_all(orgs)
    session.commit()


if __name__ == '__main__':
    builds = fill_buildiings(100)
    fields = fill_fields(1000)
    fill_organizations(builds, fields)