from django.urls import path, include
from .views import pdf_to_docx_converter_view, word_counter_text_view, lorem_ipsum_generator
# from .tools import word_counter_text

urlpatterns = [
    path('pdf_to_docx_converter/', pdf_to_docx_converter_view, name='pdf_to_docx_converter'),
    path('word_counter_text/', word_counter_text_view, name='word_counter_text'),
    path('lorem_ipsum_generator/', lorem_ipsum_generator, name='lorem_ipsum_generator'),

]