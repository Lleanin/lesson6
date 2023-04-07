import file_operations
import random
from faker import Faker
from random import randint

fake = Faker("ru_RU")


def save_cards(count):
    for item in range(8):
        for key in alphabet:
            skills[item] = skills[item].replace(key, str(alphabet[key]))
        runic_skills.append(skills[item])

    for i in range(count):
        rskills_random = random.sample(runic_skills, 8)

        context = {
            "first_name": fake.first_name_male(),
            "last_name": fake.last_name_male(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": randint(3, 18),
            "agility": randint(3, 18),
            "endurance": randint(3, 18),
            "intelligence": randint(3, 18),
            "luck": randint(3, 18),
            "skill_1": rskills_random[0],
            "skill_2": rskills_random[1],
            "skill_3": rskills_random[2]
        }

        file_operations.render_template("charsheet.svg",
                                        "files/result{}.svg".format(i),
                                        context)


alphabet = {
    'а': 'а͠', 'б': 'б̋',
    'в': 'в͒͠', 'г': 'г͒͠',
    'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒',
    'з': 'з̋̋͠', 'и': 'и',
    'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠',
    'н': 'н͒', 'о': 'о̋',
    'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒',
    'у': 'у͒͠', 'ф': 'ф̋̋͠',
    'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠',
    'щ': 'щ̋', 'ъ': 'ъ̋͠',
    'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋',
    'В': 'В͒͠', 'Г': 'Г͒͠',
    'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒',
    'З': 'З̋̋͠', 'И': 'И',
    'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠',
    'Н': 'Н͒', 'О': 'О̋',
    'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒',
    'У': 'У͒͠', 'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠',
    'Щ': 'Щ̋', 'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}

skills = [
    "Стремительный прыжок", "Электрический выстрел", "Ледяной удар",
    "Стремительный удар", "Кислотный взгляд", "Тайный побег",
    "Ледяной выстрел", "Огненный заряд"
]
runic_skills = []


def main():
    count = int(input('Введите кол-во повторений:'))
    save_cards(count)


if __name__ == '__main__':
    main()
