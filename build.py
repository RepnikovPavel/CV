import os
oname = 'PavelRepnikovCV.pdf'
currd = os.path.dirname(os.path.realpath(__file__))
texfile = os.path.join(currd, 'main.tex')
odir = os.path.join(currd,'build')
ofile = os.path.join(odir,'main.pdf')
oname = os.path.join(odir,oname)
if not os.path.exists(odir):
    os.makedirs(odir)
command_ = f'pdflatex -synctex=1 -interaction=nonstopmode --output-directory={odir} {texfile}'
os.system(command_)
os.rename(ofile,oname)