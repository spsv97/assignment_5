import random
import math
from django.shortcuts import render
from .forms import PuzzleForm

def puzzle_view(request):
    result = {}
    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            text = form.cleaned_data['text']

            # Number Puzzle
            if number % 2 == 0:
                number_result = f"{number} is even. Square root: {math.sqrt(number):.2f}"
            else:
                number_result = f"{number} is odd. Cube: {number ** 3}"

            # Text Puzzle
            binary_text = ' '.join(format(ord(char), '08b') for char in text)
            vowels = sum(1 for c in text.lower() if c in 'aeiou')

            # Treasure Hunt
            treasure_steps = []
            treasure_number = random.randint(1, 100)
            won = False
            for i in range(1, 6):
                guess = random.randint(1, 100)
                treasure_steps.append(f"Attempt {i}: Guessed {guess}")
                if guess == treasure_number:
                    won = True
                    treasure_steps.append("Treasure Found!")
                    break
            if not won:
                treasure_steps.append("Treasure Not Found!")

            result = {
                'number_result': number_result,
                'binary_text': binary_text,
                'vowel_count': vowels,
                'treasure_steps': treasure_steps
            }
    else:
        form = PuzzleForm()
    return render(request, 'puzzle/result.html', {'form': form, 'result': result})
