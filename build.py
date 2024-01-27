import os
import shutil

def clear_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

oname = 'PavelRepnikovCV.pdf'
currd = os.path.dirname(os.path.realpath(__file__))
texfile = os.path.join(currd, 'main.tex')
odir = os.path.join(currd,'build')
clear_folder(odir)
ofile = os.path.join(odir,'main.pdf')
oname = os.path.join(odir,oname)
if not os.path.exists(odir):
    os.makedirs(odir)
command_ = f'pdflatex -synctex=1 -interaction=nonstopmode --output-directory={odir} {texfile}'
os.system(command_)
os.rename(ofile,oname)