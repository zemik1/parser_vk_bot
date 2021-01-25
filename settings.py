TOKEN = "58c63fd42e0fd5fea5117e112bab46883cd2745a9aa7b96babc3ff92511c7aa7958ab7024629ef2cdb208"

BASE_URL = "https://ege.sdamgia.ru/prob_catalog"
jsonData = """{
"constructor":[
  {
   "open": false,
   "issue": "1",
   "type": "short",
   "num": 1,
   "value": 0,
   "title": "Простейшие текстовые задачи",
   "subtopics": [
    {
     "id": 174,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Вычисления",
     "subtopics": null,
     "amount": 25
    },
    {
     "id": 1,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Округление с недостатком",
     "subtopics": null,
     "amount": 8
    },
    {
     "id": 2,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Округление с избытком",
     "subtopics": null,
     "amount": 21
    },
    {
     "id": 249,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Проценты",
     "subtopics": null,
     "amount": 25
    },
    {
     "id": 5,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Проценты и округление",
     "subtopics": null,
     "amount": 9
    }
   ],
   "amount": 88,
   "name": "prob1"
  },
  {
   "open": false,
   "issue": "2",
   "type": "short",
   "num": 2,
   "value": 0,
   "title": "Чтение графиков и диаграмм",
   "subtopics": [
    {
     "id": 6,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Определение величины по графику",
     "subtopics": null,
     "amount": 26
    },
    {
     "id": 8,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Определение величины по диаграмме",
     "subtopics": null,
     "amount": 20
    },
    {
     "id": 7,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Вычисление величин по графику или диаграмме",
     "subtopics": null,
     "amount": 10
    }
   ],
   "amount": 56,
   "name": "prob2"
  },
  {
   "open": false,
   "issue": "3",
   "type": "short",
   "num": 3,
   "value": 0,
   "title": "Квадратная решётка, координатная плоскость",
   "subtopics": [
    {
     "id": 252,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Многоугольники: вычисление длин и углов",
     "subtopics": null,
     "amount": 30
    },
    {
     "id": 190,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Многоугольники: вычисление площадей",
     "subtopics": null,
     "amount": 54
    },
    {
     "id": 123,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Круг и его элементы",
     "subtopics": null,
     "amount": 15
    },
    {
     "id": 181,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Координатная плоскость",
     "subtopics": null,
     "amount": 25
    }
   ],
   "amount": 124,
   "name": "prob3"
  },
  {
   "open": false,
   "issue": "4",
   "type": "short",
   "num": 4,
   "value": 0,
   "title": "Начала теории вероятностей",
   "subtopics": [
    {
     "id": 166,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Классическое определение вероятности",
     "subtopics": null,
     "amount": 52
    },
    {
     "id": 185,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Теоремы о вероятностях событий",
     "subtopics": null,
     "amount": 33
    }
   ],
   "amount": 85,
   "name": "prob4"
  },
  {
   "open": false,
   "issue": "5",
   "type": "short",
   "num": 5,
   "value": 0,
   "title": "Простейшие уравнения",
   "subtopics": [
    {
     "id": 14,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Линейные, квадратные, кубические уравнения",
     "subtopics": null,
     "amount": 10
    },
    {
     "id": 9,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Рациональные уравнения",
     "subtopics": null,
     "amount": 11
    },
    {
     "id": 10,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Иррациональные уравнения",
     "subtopics": null,
     "amount": 15
    },
    {
     "id": 11,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Показательные уравнения",
     "subtopics": null,
     "amount": 17
    },
    {
     "id": 12,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Логарифмические уравнения",
     "subtopics": null,
     "amount": 13
    },
    {
     "id": 13,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Тригонометрические уравнения",
     "subtopics": null,
     "amount": 3
    }
   ],
   "amount": 69,
   "name": "prob5"
  },
  {
   "open": false,
   "issue": "6",
   "type": "short",
   "num": 6,
   "value": 0,
   "title": "Планиметрия",
   "subtopics": [
    {
     "id": 79,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Решение прямоугольного треугольника",
     "subtopics": null,
     "amount": 49
    },
    {
     "id": 90,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Решение равнобедренного треугольника",
     "subtopics": null,
     "amount": 45
    },
    {
     "id": 96,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Треугольники общего вида",
     "subtopics": null,
     "amount": 28
    },
    {
     "id": 102,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Параллелограммы",
     "subtopics": null,
     "amount": 34
    },
    {
     "id": 94,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Трапеция",
     "subtopics": null,
     "amount": 25
    },
    {
     "id": 111,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Центральные и вписанные углы",
     "subtopics": null,
     "amount": 15
    },
    {
     "id": 112,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Касательная, хорда, секущая",
     "subtopics": null,
     "amount": 11
    },
    {
     "id": 113,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Вписанные окружности",
     "subtopics": null,
     "amount": 24
    },
    {
     "id": 114,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Описанные окружности",
     "subtopics": null,
     "amount": 28
    }
   ],
   "amount": 259,
   "name": "prob6"
  },
  {
   "open": false,
   "issue": "7",
   "type": "short",
   "num": 7,
   "value": 0,
   "title": "Производная и первообразная",
   "subtopics": [
    {
     "id": 69,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Физический смысл производной",
     "subtopics": null,
     "amount": 6
    },
    {
     "id": 68,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Геометрический смысл производной, касательная",
     "subtopics": null,
     "amount": 31
    },
    {
     "id": 70,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Применение производной к исследованию функций",
     "subtopics": null,
     "amount": 30
    },
    {
     "id": 183,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Первообразная",
     "subtopics": null,
     "amount": 5
    }
   ],
   "amount": 72,
   "name": "prob7"
  },
  {
   "open": false,
   "issue": "8",
   "type": "short",
   "num": 8,
   "value": 0,
   "title": "Стереометрия",
   "subtopics": [
    {
     "id": 192,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Куб;",
     "subtopics": null,
     "amount": 12
    },
    {
     "id": 193,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Прямоугольный параллелепипед&nbsp;",
     "subtopics": null,
     "amount": 29
    },
    {
     "id": 180,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Элементы составных многогранников",
     "subtopics": null,
     "amount": 15
    },
    {
     "id": 148,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Площадь поверхности  составного многогранника",
     "subtopics": null,
     "amount": 17
    },
    {
     "id": 140,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Объем составного многогранника",
     "subtopics": null,
     "amount": 16
    },
    {
     "id": 178,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Призма;",
     "subtopics": null,
     "amount": 52
    },
    {
     "id": 177,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Пирамида;",
     "subtopics": null,
     "amount": 67
    },
    {
     "id": 197,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Комбинации тел",
     "subtopics": null,
     "amount": 37
    },
    {
     "id": 194,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Цилиндр",
     "subtopics": null,
     "amount": 19
    },
    {
     "id": 144,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Конус",
     "subtopics": null,
     "amount": 29
    },
    {
     "id": 151,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Шар",
     "subtopics": null,
     "amount": 8
    }
   ],
   "amount": 301,
   "name": "prob8"
  },
  {
   "open": false,
   "issue": "9",
   "type": "short",
   "num": 9,
   "value": 0,
   "title": "Вычисления и преобразования",
   "subtopics": [
    {
     "id": 55,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Преобразования числовых рациональных выражений",
     "subtopics": null,
     "amount": 6
    },
    {
     "id": 60,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Преобразования алгебраических выражений и дробей",
     "subtopics": null,
     "amount": 25
    },
    {
     "id": 56,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Преобразования числовых иррациональных выражений",
     "subtopics": null,
     "amount": 16
    },
    {
     "id": 61,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Преобразования буквенных иррациональных выражений",
     "subtopics": null,
     "amount": 11
    },
    {
     "id": 57,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Вычисление значений степенных выражений",
     "subtopics": null,
     "amount": 18
    },
    {
     "id": 62,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Действия со степенями",
     "subtopics": null,
     "amount": 30
    },
    {
     "id": 58,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Преобразования числовых логарифмических выражений",
     "subtopics": null,
     "amount": 33
    },
    {
     "id": 63,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Преобразования буквенных логарифмических выражений",
     "subtopics": null,
     "amount": 4
    },
    {
     "id": 65,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Вычисление значений тригонометрических выражений",
     "subtopics": null,
     "amount": 30
    },
    {
     "id": 59,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Преобразования числовых тригонометрических выражений",
     "subtopics": null,
     "amount": 38
    },
    {
     "id": 64,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Преобразования буквенных тригонометрических выражений",
     "subtopics": null,
     "amount": 2
    }
   ],
   "amount": 213,
   "name": "prob9"
  },
  {
   "open": false,
   "issue": "10",
   "type": "short",
   "num": 10,
   "value": 0,
   "title": "Задачи с прикладным содержанием",
   "subtopics": [
    {
     "id": 71,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Линейные уравнения и неравенства",
     "subtopics": null,
     "amount": 2
    },
    {
     "id": 72,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Квадратные и степенные уравнения и неравенства",
     "subtopics": null,
     "amount": 16
    },
    {
     "id": 76,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Рациональные уравнения и неравенства",
     "subtopics": null,
     "amount": 14
    },
    {
     "id": 77,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Иррациональные уравнения и неравенства",
     "subtopics": null,
     "amount": 10
    },
    {
     "id": 73,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Показательные уравнения и неравенства",
     "subtopics": null,
     "amount": 7
    },
    {
     "id": 74,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Логарифмические уравнения и неравенства",
     "subtopics": null,
     "amount": 4
    },
    {
     "id": 75,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Тригонометрические уравнения и неравенства",
     "subtopics": null,
     "amount": 16
    },
    {
     "id": 184,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Разные задачи",
     "subtopics": null,
     "amount": 6
    }
   ],
   "amount": 75,
   "name": "prob10"
  },
  {
   "open": false,
   "issue": "11",
   "type": "short",
   "num": 11,
   "value": 0,
   "title": "Текстовые задачи",
   "subtopics": [
    {
     "id": 88,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Задачи на проценты, сплавы и смеси",
     "subtopics": null,
     "amount": 16
    },
    {
     "id": 84,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Задачи на движение по прямой",
     "subtopics": null,
     "amount": 30
    },
    {
     "id": 85,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Задачи на движение по окружности",
     "subtopics": null,
     "amount": 5
    },
    {
     "id": 86,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Задачи на движение по воде",
     "subtopics": null,
     "amount": 14
    },
    {
     "id": 87,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Задачи на совместную работу",
     "subtopics": null,
     "amount": 24
    },
    {
     "id": 89,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Задачи на прогрессии",
     "subtopics": null,
     "amount": 9
    }
   ],
   "amount": 98,
   "name": "prob11"
  },
  {
   "open": false,
   "issue": "12",
   "type": "short",
   "num": 12,
   "value": 0,
   "title": "Наибольшее и наименьшее значение функций",
   "subtopics": [
    {
     "id": 81,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Исследование степенных и иррациональных функций",
     "subtopics": null,
     "amount": 57
    },
    {
     "id": 83,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Исследование частных",
     "subtopics": null,
     "amount": 11
    },
    {
     "id": 82,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Исследование произведений",
     "subtopics": null,
     "amount": 28
    },
    {
     "id": 80,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Исследование показательных и логарифмических функций",
     "subtopics": null,
     "amount": 22
    },
    {
     "id": 78,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Исследование тригонометрических функций",
     "subtopics": null,
     "amount": 29
    },
    {
     "id": 175,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Исследование функций без помощи производной",
     "subtopics": null,
     "amount": 16
    }
   ],
   "amount": 163,
   "name": "prob12"
  },
  {
   "open": false,
   "issue": "13",
   "type": "detailed",
   "num": 1,
   "value": 0,
   "title": "Уравнения",
   "subtopics": [
    {
     "id": 275,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Иррациональные уравнения",
     "subtopics": null,
     "amount": 10
    },
    {
     "id": 290,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Рациональные уравнения",
     "subtopics": null,
     "amount": 3
    },
    {
     "id": 291,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Тригонометрические уравнения, разложение на множители",
     "subtopics": null,
     "amount": 25
    },
    {
     "id": 186,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Ло­га­риф­ми­че­ские и по­ка­за­тель­ные уравнения",
     "subtopics": null,
     "amount": 13
    },
    {
     "id": 167,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Тригонометрические уравнения",
     "subtopics": null,
     "amount": 54
    },
    {
     "id": 202,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Тригонометрические уравнения, исследование ОДЗ",
     "subtopics": null,
     "amount": 39
    },
    {
     "id": 201,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Уравнения смешанного типа",
     "subtopics": null,
     "amount": 58
    }
   ],
   "amount": 202,
   "name": "prob13"
  },
  {
   "open": false,
   "issue": "14",
   "type": "detailed",
   "num": 2,
   "value": 0,
   "title": "Стереометрическая задача",
   "subtopics": [
    {
     "id": 280,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Расстояние между прямыми и плоскостями",
     "subtopics": null,
     "amount": 15
    },
    {
     "id": 281,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Расстояние от точки до прямой и до плоскости",
     "subtopics": null,
     "amount": 14
    },
    {
     "id": 282,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Сечения многогранников",
     "subtopics": null,
     "amount": 40
    },
    {
     "id": 283,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Угол между плоскостями",
     "subtopics": null,
     "amount": 23
    },
    {
     "id": 284,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Угол между прямой и плоскостью",
     "subtopics": null,
     "amount": 19
    },
    {
     "id": 285,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Угол между скрещивающимися прямыми",
     "subtopics": null,
     "amount": 13
    },
    {
     "id": 257,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Объёмы многогранников",
     "subtopics": null,
     "amount": 22
    },
    {
     "id": 206,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Круглые тела: цилиндр, конус, шар",
     "subtopics": null,
     "amount": 20
    }
   ],
   "amount": 166,
   "name": "prob14"
  },
  {
   "open": false,
   "issue": "15",
   "type": "detailed",
   "num": 3,
   "value": 0,
   "title": "Неравенства",
   "subtopics": [
    {
     "id": 242,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Рациональные неравенства",
     "subtopics": null,
     "amount": 33
    },
    {
     "id": 243,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Неравенства, содержащие радикалы",
     "subtopics": null,
     "amount": 9
    },
    {
     "id": 237,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Показательные неравенства",
     "subtopics": null,
     "amount": 112
    },
    {
     "id": 238,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Логарифмические неравенства",
     "subtopics": null,
     "amount": 90
    },
    {
     "id": 239,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Неравенства с логарифмами по переменному основанию",
     "subtopics": null,
     "amount": 87
    },
    {
     "id": 244,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Неравенства с модулем",
     "subtopics": null,
     "amount": 17
    },
    {
     "id": 245,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Смешанные неравенства",
     "subtopics": null,
     "amount": 74
    }
   ],
   "amount": 422,
   "name": "prob15"
  },
  {
   "open": false,
   "issue": "16",
   "type": "detailed",
   "num": 4,
   "value": 0,
   "title": "Планиметрическая задача",
   "subtopics": [
    {
     "id": 276,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Многоугольники и их свойства",
     "subtopics": null,
     "amount": 60
    },
    {
     "id": 277,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Окружности и системы окружностей",
     "subtopics": null,
     "amount": 15
    },
    {
     "id": 278,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Окружности и треугольники",
     "subtopics": null,
     "amount": 51
    },
    {
     "id": 279,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Окружности и четырёхугольники",
     "subtopics": null,
     "amount": 42
    }
   ],
   "amount": 168,
   "name": "prob16"
  },
  {
   "open": false,
   "issue": "17",
   "type": "detailed",
   "num": 5,
   "value": 0,
   "title": "Финансовая математика",
   "subtopics": [
    {
     "id": 247,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Задачи на оптимальный выбор",
     "subtopics": null,
     "amount": 61
    },
    {
     "id": 221,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Банки, вклады, кредиты",
     "subtopics": null,
     "amount": 140
    }
   ],
   "amount": 201,
   "name": "prob17"
  },
  {
   "open": false,
   "issue": "18",
   "type": "detailed",
   "num": 6,
   "value": 0,
   "title": "Задача с параметром",
   "subtopics": [
    {
     "id": 171,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Уравнения с параметром",
     "subtopics": null,
     "amount": 44
    },
    {
     "id": 270,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Неравенства с параметром",
     "subtopics": null,
     "amount": 9
    },
    {
     "id": 268,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Системы с параметром",
     "subtopics": null,
     "amount": 25
    },
    {
     "id": 207,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Расположение корней квадратного трехчлена",
     "subtopics": null,
     "amount": 10
    },
    {
     "id": 273,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Использование симметрий",
     "subtopics": null,
     "amount": 18
    },
    {
     "id": 208,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Использование монотонности, оценок",
     "subtopics": null,
     "amount": 31
    },
    {
     "id": 274,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Аналитическое решение уравнений, неравенств, систем",
     "subtopics": null,
     "amount": 62
    },
    {
     "id": 271,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Координаты (x, a)",
     "subtopics": null,
     "amount": 13
    },
    {
     "id": 266,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Уравнение окружности",
     "subtopics": null,
     "amount": 36
    },
    {
     "id": 269,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Расстояние между точками",
     "subtopics": null,
     "amount": 7
    },
    {
     "id": 235,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Функции, зависящие от параметра",
     "subtopics": null,
     "amount": 26
    }
   ],
   "amount": 281,
   "name": "prob18"
  },
  {
   "open": false,
   "issue": "19",
   "type": "detailed",
   "num": 7,
   "value": 0,
   "title": "Числа и их свойства",
   "subtopics": [
    {
     "id": 172,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Числа и их свойства",
     "subtopics": null,
     "amount": 82
    },
    {
     "id": 217,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Числовые наборы на карточках и досках",
     "subtopics": null,
     "amount": 39
    },
    {
     "id": 209,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Последовательности и прогрессии",
     "subtopics": null,
     "amount": 44
    },
    {
     "id": 210,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Сюжетные задачи: кино, театр, мотки верёвки",
     "subtopics": null,
     "amount": 56
    }
   ],
   "amount": 221,
   "name": "prob19"
  },
  {
   "open": false,
   "issue": "Д1",
   "type": "extra",
   "value": 0,
   "title": "Выбор оптимального варианта",
   "subtopics": [
    {
     "id": 54,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Выбор варианта из двух возможных",
     "subtopics": null,
     "amount": 5
    },
    {
     "id": 53,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Выбор варианта из трех возможных",
     "subtopics": null,
     "amount": 27
    },
    {
     "id": 173,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Выбор варианта из четырех возможных",
     "subtopics": null,
     "amount": 5
    }
   ],
   "amount": 37,
   "name": "prob20"
  },
  {
   "open": false,
   "issue": "Д2",
   "type": "extra",
   "value": 0,
   "title": "Планиметрия: вычисление длин и площадей",
   "subtopics": [
    {
     "id": 255,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Координатная плоскость",
     "subtopics": null,
     "amount": 51
    },
    {
     "id": 254,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Окружности",
     "subtopics": null,
     "amount": 11
    },
    {
     "id": 253,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Четырехугольники",
     "subtopics": null,
     "amount": 22
    },
    {
     "id": 250,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Треугольники",
     "subtopics": null,
     "amount": 7
    }
   ],
   "amount": 91,
   "name": "prob21"
  },
  {
   "open": false,
   "issue": "Д3",
   "type": "extra",
   "value": 0,
   "title": "Планиметрия",
   "subtopics": [
    {
     "id": 127,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Вычисление длин и площадей. Прямоугольник",
     "subtopics": null,
     "amount": 1
    },
    {
     "id": 120,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Вычисление длин и площадей. Треугольники",
     "subtopics": null,
     "amount": 7
    },
    {
     "id": 124,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Вычисление длин и площадей. Трапеции",
     "subtopics": null,
     "amount": 2
    },
    {
     "id": 182,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Вычисление длин и площадей. Векторы",
     "subtopics": null,
     "amount": 36
    },
    {
     "id": 126,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Вычисление длин и площадей. Многоугольник",
     "subtopics": null,
     "amount": 1
    },
    {
     "id": 256,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Задачи, связанные с углами. Задачи на многоугольники и окружности",
     "subtopics": null,
     "amount": 40
    },
    {
     "id": 251,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Задачи, связанные с углами. Применение тригонометрии",
     "subtopics": null,
     "amount": 169
    }
   ],
   "amount": 256,
   "name": "prob22"
  },
  {
   "open": false,
   "issue": "Д4",
   "type": "extra",
   "value": 0,
   "title": "Задачи с прикладным содержанием",
   "subtopics": [
    {
     "id": 248,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Тригонометрические уравнения и неравенства",
     "subtopics": null,
     "amount": 2
    }
   ],
   "amount": 2,
   "name": "prob23"
  },
  {
   "open": false,
   "issue": "Д5 C1",
   "type": "extra",
   "value": 0,
   "title": "Сложные уравнения, си­сте­мы уравнений",
   "subtopics": [
    {
     "id": 203,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Системы тригонометрических уравнений",
     "subtopics": null,
     "amount": 24
    },
    {
     "id": 219,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Три­го­но­мет­ри­че­ские уравнения",
     "subtopics": null,
     "amount": 107
    },
    {
     "id": 220,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Три­го­но­мет­ри­че­ские уравнения, ис­сле­до­ва­ние ОДЗ",
     "subtopics": null,
     "amount": 95
    },
    {
     "id": 218,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Урав­не­ния смешанного типа",
     "subtopics": null,
     "amount": 79
    }
   ],
   "amount": 305,
   "name": "prob24"
  },
  {
   "open": false,
   "issue": "Д6 C2",
   "type": "extra",
   "value": 0,
   "title": "Стереометрическая задача",
   "subtopics": [
    {
     "id": 198,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Угол между плоскостями",
     "subtopics": null,
     "amount": 29
    },
    {
     "id": 179,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Расстояние от точки до прямой и до плоскости",
     "subtopics": null,
     "amount": 43
    },
    {
     "id": 199,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Расстояние между прямыми и плоскостями",
     "subtopics": null,
     "amount": 9
    },
    {
     "id": 200,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Сечения многогранников",
     "subtopics": null,
     "amount": 37
    },
    {
     "id": 213,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Объёмы многогранников",
     "subtopics": null,
     "amount": 8
    },
    {
     "id": 212,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Круглые тела: цилиндр, конус, шар",
     "subtopics": null,
     "amount": 9
    }
   ],
   "amount": 135,
   "name": "prob25"
  },
  {
   "open": false,
   "issue": "Д7 C2",
   "type": "extra",
   "value": 0,
   "title": "Сложная стереометрия",
   "subtopics": [
    {
     "id": 231,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Круглые тела",
     "subtopics": null,
     "amount": 117
    },
    {
     "id": 230,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Многогранники",
     "subtopics": null,
     "amount": 178
    }
   ],
   "amount": 295,
   "name": "prob26"
  },
  {
   "open": false,
   "issue": "Д8 C3",
   "type": "extra",
   "value": 0,
   "title": "Простые системы неравенств",
   "subtopics": [
    {
     "id": 169,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Системы, содержащие логарифмическое неравенство",
     "subtopics": null,
     "amount": 19
    },
    {
     "id": 204,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Рациональные, иррациональные, показательные неравенства",
     "subtopics": null,
     "amount": 37
    },
    {
     "id": 214,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Системы с логарифмами по переменному основанию",
     "subtopics": null,
     "amount": 48
    }
   ],
   "amount": 104,
   "name": "prob27"
  },
  {
   "open": false,
   "issue": "Д9 C3",
   "type": "extra",
   "value": 0,
   "title": "Сложные неравенства",
   "subtopics": [
    {
     "id": 246,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Неравенства различных типов",
     "subtopics": null,
     "amount": 186
    }
   ],
   "amount": 186,
   "name": "prob28"
  },
  {
   "open": false,
   "issue": "Д10 C3",
   "type": "extra",
   "value": 0,
   "title": "Системы сложных неравенств",
   "subtopics": [
    {
     "id": 223,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Рациональные, иррациональные, показательные неравенства",
     "subtopics": null,
     "amount": 29
    },
    {
     "id": 224,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Системы с логарифмами по переменному основанию",
     "subtopics": null,
     "amount": 31
    },
    {
     "id": 225,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Системы, содержащие логарифмическое неравенство",
     "subtopics": null,
     "amount": 22
    }
   ],
   "amount": 82,
   "name": "prob29"
  },
  {
   "open": false,
   "issue": "Д11 C4",
   "type": "extra",
   "value": 0,
   "title": "Планиметрическая задача",
   "subtopics": [
    {
     "id": 205,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Многоугольники и их свойства",
     "subtopics": null,
     "amount": 30
    },
    {
     "id": 170,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Окружности и треугольники",
     "subtopics": null,
     "amount": 49
    },
    {
     "id": 215,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Окружности и четырёхугольники",
     "subtopics": null,
     "amount": 20
    },
    {
     "id": 216,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Окружности и системы окружностей",
     "subtopics": null,
     "amount": 20
    }
   ],
   "amount": 119,
   "name": "prob30"
  },
  {
   "open": false,
   "issue": "Д12 C4",
   "type": "extra",
   "value": 0,
   "title": "Сложная планиметрия",
   "subtopics": [
    {
     "id": 262,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Комбинации фигур",
     "subtopics": null,
     "amount": 77
    },
    {
     "id": 260,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Многоугольники",
     "subtopics": null,
     "amount": 58
    },
    {
     "id": 261,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Окружности",
     "subtopics": null,
     "amount": 45
    },
    {
     "id": 259,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Треугольники",
     "subtopics": null,
     "amount": 111
    }
   ],
   "amount": 291,
   "name": "prob31"
  },
  {
   "open": false,
   "issue": "Д13 C5",
   "type": "extra",
   "value": 0,
   "title": "Сложные практические задачи",
   "subtopics": [
    {
     "id": 232,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Практические задачи",
     "subtopics": null,
     "amount": 192
    }
   ],
   "amount": 192,
   "name": "prob32"
  },
  {
   "open": false,
   "issue": "Д14 C6",
   "type": "extra",
   "value": 0,
   "title": "Сложные задачи с па­ра­мет­ром",
   "subtopics": [
    {
     "id": 258,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Уравнения с параметром",
     "subtopics": null,
     "amount": 112
    },
    {
     "id": 240,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Не­ра­вен­ства с параметром",
     "subtopics": null,
     "amount": 87
    },
    {
     "id": 241,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Системы с параметром",
     "subtopics": null,
     "amount": 84
    }
   ],
   "amount": 283,
   "name": "prob33"
  },
  {
   "open": false,
   "issue": "Д15 C7",
   "type": "extra",
   "value": 0,
   "title": "Числа и их свойства",
   "subtopics": [
    {
     "id": 288,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Последовательности и прогрессии",
     "subtopics": null,
     "amount": 13
    },
    {
     "id": 289,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Сюжетные задачи: кино, театр, мотки верёвки",
     "subtopics": null,
     "amount": 13
    },
    {
     "id": 286,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Числа и их свойства",
     "subtopics": null,
     "amount": 66
    },
    {
     "id": 287,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Числовые наборы на карточках и досках",
     "subtopics": null,
     "amount": 1
    }
   ],
   "amount": 93,
   "name": "prob34"
  },
  {
   "open": false,
   "issue": "Д16 C7",
   "type": "extra",
   "value": 0,
   "title": "Сложные задания на числа и их свойства",
   "subtopics": [
    {
     "id": 226,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Последовательности и прогрессии",
     "subtopics": null,
     "amount": 27
    },
    {
     "id": 227,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Сюжетные задачи",
     "subtopics": null,
     "amount": 37
    },
    {
     "id": 228,
     "value": null,
     "open": false,
     "checked": true,
     "title": "Числа и их свойства",
     "subtopics": null,
     "amount": 172
    }
   ],
   "amount": 236,
   "name": "prob35"
  }
 ]
}"""
