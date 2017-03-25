"""This is the entry point of the program."""


def create_box(height, width, char):
    result = ''
    if height >= 1 and width >= 1:
        for i in range(height):
            result += char * width + '\n'
        return result
    return "invalid input"
    
def create_hollow_box(height, width, character):
    box = character * width
    top_bot = str(box) + '\n'
    if height >= 1 and width >= 1:
        for i in range(width):
            middle = character+((width - 2)*' ')+character+'\n'
        return top_bot+(middle * (height - 2))+top_bot
    return "invalid input"

if __name__ == '__main__':
    create_box(3, 4, '*')
    
if __name__ == '__main__':
    create_hollow_box(4, 5, '*')
    