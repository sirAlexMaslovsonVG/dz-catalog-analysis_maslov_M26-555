import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    """
    Функция возвращает среднюю оценку по каталогу, округленную до одного знака
    """
    if not movies:
        return 0
    ratings = [item["rating"] for item in movies]
    return round(sum(ratings) / len(ratings), 1)


def catalog_age_stats(movies, current_year=2026):
    """
    Функция возвращает возвращает кортеж (самый старый фильм в годах,
    самый новый фильм в годах, среднее)
    """
    if not movies:
        return (0, 0, 0)

    ages = [current_year - item["year"] for item in movies]
    oldest_age = max(ages)  # самый старый фильм
    newest_age = min(ages)  # самый новый фильм
    avg_age = math.ceil(sum(ages) / len(ages))

    return (oldest_age, newest_age, avg_age)


def duration_in_hours(minutes):
    """
    Функция возвращает перевод из минут в часы и минуты в формате *ч *м
    """
    hours = minutes // 60  # целочисленное деление
    mins = minutes % 60  # остаток от деления
    return f"{hours}ч {mins}м"


def rating_tier(rating):
    """
    Функция по оценке возвращает категорию: "шедевр" (≥9), "хорошо" (7-8.9),
    "средне" (5-6.9), "слабо" (<5)
    """
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо" if rating >= 0 else "некорректная оценка"


def decade_label(year):
    """
    Функция возвращает метку "новые" (после 2020), "недавние" (2015-2020)
    или "старые" (раньше 2015)
    """
    if not isinstance(year, int):
        return "неизвестно"
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# for + continue — фильмы без жанра "comedy"
for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

# while + break — первый фильм с рейтингом > 9.0
i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(f"Найден шедевр: {movies[i]['title']} — {movies[i]['rating']}")
        break
    i += 1
else:
    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """
    Функция возвращает количество фильмов длиннее threshold минут
    """
    count = 0
    for item in movies:
        if item["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    """
    Функция возыращает строку приведенную к формату
    Title Case (каждое слово c заглавной буквы)
    """
    words = title.split()
    words_appear = [word[0].upper() + word[1:] for word in words]
    return " ".join(words_appear)


def make_slug(title):
    """
    Функция возвращает нормализованное название в «слаг» вида the-quiet-algorithm
    """
    normalized = normalize_title(title)
    lower_words = normalized.lower().split()
    return "-".join(lower_words)


def format_report_line(movie):
    """
    Функция возвращает единую строку c описанием фильма
    """
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(movie["genres"])
    return f'"{title}" ({year}) - {rating}/10, {duration}, жанры: {genres}'


def titles_sorted_by_rating(movies):
    """
    Функция возвращает список названий фильмов, отсортированных
    по убыванию рейтинга
    """
    by_rating = sorted(movies, key=lambda m: m["rating"], reverse=True)
    """
    Если изменить вывод titles_sorted_by_rating и
    реализовать там вывод отсортированного списка обьектов, то функция
    получилась бы более универсальной
    """
    return [movie["title"] for movie in by_rating]


def top_n_by_rating(movies, n=3):
    """
    Функция возвращает список из n кортежей (title, rating) — топ по рейтингу
    """
    by_rating = sorted(movies, key=lambda m: m["rating"], reverse=True)[:n]
    return [(m["title"], m["rating"]) for m in by_rating]


def count_by_genre(movies):
    """
    Функция возвращает словарь {жанр: количество фильмов}
    """
    result = {}
    for movie in movies:
        for genre in movie["genres"]:
            result[genre] = result.get(genre, 0) + 1
    return dict(sorted(result.items(), key=lambda value: value[1], reverse=True))


def actor_filmography(movies):
    """
    Функция возвращает словарь {актёр: [список названий фильмов]}
    """
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


def above_average_movies(movies):
    """
    Функция возвращает словарь {title: rating} только для фильмов
    рейтингом выше среднего
    """
    avg = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avg
    }
