import os 
from os.path import abspath,join
from argparse import ArgumentParser

parser = ArgumentParser(description='Process some integers.')
parser.add_argument('path', type=str, help='given project root path')
parser.add_argument('name', type=str, help='given project root name')

args = parser.parse_args()


ROOT = abspath(os.getcwd()) if args.path == '.' else args.path

PROJECT = args.name

project_path = join(ROOT,PROJECT)
src_path = join(project_path,'src')
screens = join(src_path,'screens')
assets_path = join(src_path,'assets')
fonts_path = join(assets_path,'fonts')
images_path = join(assets_path,'images')
icons_path = join(assets_path,'icons')
logos_path = join(assets_path,'logos')

components_path = join(src_path,'components')
navigations = join(src_path,'navigations')
styles = join(src_path,'styles')

os.makedirs(project_path)
os.chdir(project_path)

paths = [src_path,screens,assets_path,fonts_path,images_path,icons_path,components_path,navigations,styles]

for path in paths:
	print('created folder',path,sep=" : ")
	os.makedirs(path)

os.chdir(styles)
styles_files = ['index.js','colors.js','spacing.js','typography.js']

for file in styles_files:
	with open(file,'w') as file:
		pass
