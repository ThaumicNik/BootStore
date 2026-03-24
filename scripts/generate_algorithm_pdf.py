from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


OUTPUT_PATH = "docs/algorithm_development_flowchart.pdf"


def register_font() -> str:
    candidates = [
        "C:/Windows/Fonts/times.ttf",
        "C:/Windows/Fonts/timesbd.ttf",
    ]
    for font_path in candidates:
        try:
            pdfmetrics.registerFont(TTFont("TimesNewRoman", font_path))
            return "TimesNewRoman"
        except Exception:
            continue
    return "Helvetica"


def box(c: canvas.Canvas, x: int, y: int, w: int, h: int, text: str, font_name: str) -> None:
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.white)
    c.rect(x, y, w, h, stroke=1, fill=1)
    c.setFillColor(colors.black)
    c.setFont(font_name, 10)
    lines = text.split("\n")
    ty = y + h - 16
    for line in lines:
        c.drawCentredString(x + w / 2, ty, line)
        ty -= 12


def terminator(c: canvas.Canvas, x: int, y: int, w: int, h: int, text: str, font_name: str) -> None:
    c.roundRect(x, y, w, h, 14, stroke=1, fill=0)
    c.setFont(font_name, 10)
    c.drawCentredString(x + w / 2, y + h / 2 - 3, text)


def decision(c: canvas.Canvas, x: int, y: int, w: int, h: int, text: str, font_name: str) -> None:
    c.setStrokeColor(colors.black)
    c.setFillColor(colors.white)
    p = c.beginPath()
    p.moveTo(x + w / 2, y + h)
    p.lineTo(x + w, y + h / 2)
    p.lineTo(x + w / 2, y)
    p.lineTo(x, y + h / 2)
    p.close()
    c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(colors.black)
    c.setFont(font_name, 9)
    for idx, line in enumerate(text.split("\n")):
        c.drawCentredString(x + w / 2, y + h / 2 + 8 - idx * 11, line)


def arrow(c: canvas.Canvas, x1: int, y1: int, x2: int, y2: int, label: str = "", font_name: str = "Helvetica") -> None:
    c.setStrokeColor(colors.black)
    c.line(x1, y1, x2, y2)
    c.line(x2, y2, x2 - 5, y2 + 3)
    c.line(x2, y2, x2 + 5, y2 + 3)
    if label:
        c.setFont(font_name, 9)
        c.drawString((x1 + x2) / 2 + 4, (y1 + y2) / 2 + 2, label)


def main() -> None:
    font_name = register_font()
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    page_w, page_h = landscape(A4)

    c.setFont(font_name, 14)
    c.drawString(40, page_h - 30, "Блок-схема алгоритма разработки приложения учета обуви")
    c.setFont(font_name, 10)
    c.drawString(40, page_h - 46, "Практическая работа №1. Алгоритм разработки (ГОСТ 19.701-90).")

    # Row 1
    terminator(c, 40, 420, 150, 42, "Начало", font_name)
    box(c, 230, 410, 200, 60, "Анализ задания\nи требований модулей", font_name)
    box(c, 470, 410, 220, 60, "Проектирование БД:\nтаблицы, ключи, связи (3НФ)", font_name)
    box(c, 730, 410, 220, 60, "Создание SQL-схемы\nи подготовка ER-диаграммы", font_name)
    box(c, 990, 410, 260, 60, "Подготовка данных import\nи загрузка в БД", font_name)

    arrow(c, 190, 441, 230, 441, font_name=font_name)
    arrow(c, 430, 441, 470, 441, font_name=font_name)
    arrow(c, 690, 441, 730, 441, font_name=font_name)
    arrow(c, 950, 441, 990, 441, font_name=font_name)

    # Row 2
    box(c, 990, 300, 260, 70, "Разработка UI и навигации:\nроли, страницы, авторизация", font_name)
    box(c, 690, 300, 260, 70, "Реализация модулей:\nтовары, поиск/фильтр/сортировка,\nCRUD", font_name)
    box(c, 390, 300, 260, 70, "Реализация заказов\n(модуль 4, доп. баллы)", font_name)
    box(c, 90, 300, 260, 70, "Интеграция БД с приложением\nи вывод данных", font_name)

    arrow(c, 1120, 410, 1120, 370, font_name=font_name)
    arrow(c, 990, 335, 950, 335, font_name=font_name)
    arrow(c, 690, 335, 650, 335, font_name=font_name)
    arrow(c, 390, 335, 350, 335, font_name=font_name)

    # Row 3
    decision(c, 110, 180, 220, 80, "Функциональность\nсоответствует\nтребованиям?", font_name)
    box(c, 390, 190, 240, 60, "Настройка линтера\nи исправление замечаний", font_name)
    box(c, 670, 190, 240, 60, "Рефакторинг и\nулучшение структуры кода", font_name)
    box(c, 950, 190, 280, 60, "Подключение CodeClimate\nи добавление бейджа в README", font_name)

    arrow(c, 220, 300, 220, 260, font_name=font_name)
    arrow(c, 330, 220, 390, 220, "Да", font_name)
    arrow(c, 630, 220, 670, 220, font_name=font_name)
    arrow(c, 910, 220, 950, 220, font_name=font_name)

    # Iteration branch
    box(c, 80, 80, 280, 60, "Доработка требований,\nисправление ошибок и повторное тестирование", font_name)
    arrow(c, 110, 220, 80, 110, "Нет", font_name)
    arrow(c, 360, 110, 560, 110, font_name=font_name)
    arrow(c, 560, 110, 560, 300, font_name=font_name)
    arrow(c, 560, 300, 350, 300, font_name=font_name)

    # Finish
    box(c, 950, 80, 280, 60, "Подготовка артефактов:\nисходники, SQL, PDF, DOCX", font_name)
    terminator(c, 1260, 90, 120, 42, "Конец", font_name)
    arrow(c, 1090, 190, 1090, 140, font_name=font_name)
    arrow(c, 1230, 110, 1260, 110, font_name=font_name)

    c.showPage()
    c.save()
    print(f"Создан PDF: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
