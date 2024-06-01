from pptx import Presentation
from pptx.util import Inches, Cm, Pt
from pptx.enum.shapes import MSO_SHAPE


#def generate_presentation(main_entry, font, switch_1, switch_2, url=None):
def generate_presentation():
    # Создание презентации
    prs = Presentation()

    # Настройка размеров слайда (1200x593 пикселей)
    prs.slide_width = Inches(1200 / 96)  # Конвертируем пиксели в дюймы
    prs.slide_height = Inches(593 / 96)

    # Создание слайда
    slide_layout = prs.slide_layouts[6]  # Пустой слайд, пятый макет
    slide = prs.slides.add_slide(slide_layout)

    # Добавление заголовка
    title_box = slide.shapes.add_textbox(Cm(1), Cm(2), Cm(15.24), Cm(1.93))
    title_frame = title_box.text_frame
    p = title_frame.add_paragraph()
    p.font.bold = True
    p.font.size = Pt(40)
    p.text = "Место для заголовка"

    # Добавление подзаголовка
    subtitle_box = slide.shapes.add_textbox(Cm(1), Cm(5), Cm(15.24), Cm(1.93))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.text = "Подзаголовок"

    # Добавление объекта для изображения (используем прямоугольник как плейсхолдер)
    image_placeholder = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Cm(17.5), Cm(0), Cm(14.25), Cm(15.69))
    image_placeholder.text = "Место для изображения"

    # Добавление кнопки с гиперссылкой
    button_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Cm(1), Cm(12), Cm(7), Cm(1.5))
    button_shape.text = "Перейти по ссылке"
    link = button_shape.click_action.hyperlink
    link.address = "https://example.com"

    # Сохранение презентации
    prs.save("presentation.pptx")

    #title.text = main_entry
    #subtitle.text = f"Font: {font}, Switch 1: {switch_1}, Switch 2: {switch_2}"

    #if url:
    #    subtitle.text += f", URL: {url}"

    #prs.save('test.pptx')


generate_presentation()