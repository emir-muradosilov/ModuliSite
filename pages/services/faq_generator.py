FAQ_PATTERNS = [

    "Сколько стоит {service} в {city}?",
    "Как заказать {service} в {city}?",
    "Сколько времени занимает производство {service}?",
    "Какая стоимость {service} в {city}?",
    "С чего начать если я хочу купить {service}?",
    "Вы выполняете работы под ключ?",
    "Если нужно здание C-0 или С-1 - подходят ли под это Модульные здания?",
    "Как быстро возможен выезд по {city}?",
]


def generate_faqs(page, city):

    faqs = []

    for question in FAQ_PATTERNS:

        faqs.append({
            'question': question.format(
                service=page.title.lower(),
                city=city.name
            )
        })

    return faqs