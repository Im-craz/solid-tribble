from PIL import Image


def resize_image(size_one, size_two):
    image = Image.open('codewithtomi-logo.jpg')

    print(f'Current size: {image.size}')

    resized_image = image.resize((size_one, size_two))

    resized_image.save(f'codewithtomi-logo-{size_one}.jpeg')


size_one = int(input('Enter Width: '))
size_two = int(input('Enter Length: '))
resize_image(size_one, size_two)
