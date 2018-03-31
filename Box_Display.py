# Collect sentence to display in centre of the box
sentence = input("Enter a Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
margin = (screen_width - box_width)// 2

#Designing our box
print()
print(' ' * margin + '+' + '-' * (box_width - 2) + '+')
print(' '* margin + '|' + ' ' * (box_width - 2) + '|')
print(' ' * margin + '|' + ' ' * 2 + sentence + ' ' * 2 + '|')
print(' '* margin + '|' + ' ' * (box_width - 2) + '|')
print(' ' * margin + '+' + '-' * (box_width - 2) + '+')
print()
