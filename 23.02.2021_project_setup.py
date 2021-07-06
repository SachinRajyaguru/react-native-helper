# export const WIDTH_90P = wp(90);

def print_fonts():
  for i in range(1,101):
    print(f'export const fs{i} = RFValue({i});')


def print_height_width():
  for i in range(1,101):
    print(f'export const w{i} = wp({i});')

  for i in range(1,101):
    print(f'export const h{i} = hp({i});')

def print_icons(path):
  import os
  os.chdir(path)

  file_for_import = []

  for file in os.listdir():
    if not file.endswith('x.png'):
      file,ext = os.path.splitext(file)
      file_for_import.append(file)
      print(f'export const icn{file[0].upper()+file[1:]} = require("./{file}.png");')

  file_for_import = ', '.join(file_for_import)
  print('\n'*3)
  print(file_for_import)


def print_images(path):
  import os
  os.chdir(path)

  file_for_import = []

  for file in os.listdir():
    if not file.endswith('x.png'):
      file,ext = os.path.splitext(file)
      file_for_import.append(file)
      print(f'export const img{file[0].upper()+file[1:]} = require("./{file}.png");')

  file_for_import = ', '.join(file_for_import)
  print('\n'*3)
  print(file_for_import)

def print_logos(path):
  import os
  os.chdir(path)

  file_for_import = []

  for file in os.listdir():
    if not file.endswith('x.png'):
      file,ext = os.path.splitext(file)
      file_for_import.append(file)
      print(f'export const img{file[0].upper()+file[1:]} = require("./{file}.png");')

  file_for_import = ', '.join(file_for_import)
  print('\n'*3)
  print(file_for_import)

# path = input('enter full path for icon dir : ')
# print_icons(path)

# print_height_width()
print_fonts()
# print_logos('/Users/hyperlink/Downloads/_logos')

# print_height_width()