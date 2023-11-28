# converter/tool/word_counter.py
from django.shortcuts import render

def word_counter_text(text):
    words = text.split()
    word_count = len(words)
    return word_count

# def word_counter_text(request):
#     word_count = 0

#     if request.method == 'POST':
#         text = request.POST.get('text', '')
#         words = text.split()
#         word_count = len(words)

#     return render(request, 'converter/word_counter_text.html', {'word_count': word_count})



# def word_counter_Text(request):
#     word_count = 0
    
#     if request.method == 'POST':
#         text = request.POST.get('text', '')  # Assuming the text input field has the name 'text'
#         words = text.split()
#         word_count = len(words)

#     return render(request, 'word_counter_text.html', {'word_count': word_count})
