import os
from glob import glob
from subprocess import Popen
from shutil import rmtree, move

class convertToPDF():

    def __init__(self, sourceFolder, projectFolder):
        self.sourceFolder = sourceFolder
        self.projectFolder = projectFolder

    def editing_path(self):

        joined_paths = glob(os.path.join(self.sourceFolder, self.projectFolder,'**','**'), recursive=True)
        """Editing folder and filepaths to remove any special characters""" 
        directory = joined_paths
        for pth in directory:
            foldr = os.path.dirname(pth)
            for f in os.listdir(foldr):
                try:
                    os.rename(os.path.join(foldr, f), os.path.join(foldr, os.path.basename(f).replace(' ', '_').replace('(','').replace(')','').replace('&','').replace('.','',f.count('.')-1)))
                except:
                    pass

    def read_edited_path(self):

        joined_paths = glob(os.path.join(self.sourceFolder, self.projectFolder,'**','**'), recursive=True)
        """convert doc files to pdf"""
        for f in joined_paths:
            if (f.split('.')[-1].lower().strip() == 'doc'):
                import time
                try:
                    if not os.path.exists('tmp'):
                        os.makedirs('tmp')

                    Popen(['/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf --outdir tmp '+f], shell=True, stdin=PIPE)
                    time.sleep(20)
                    try:
                        move(os.path.join('tmp',os.path.basename(f).split('.')[0]+'.pdf'),os.path.join(os.path.dirname(f),os.path.basename(f).split('.')[0]+'.pdf'))
                    except Exception as e:
                        print(f'Move Error: {e}')
                except:
                    pass
            try:
                rmtree('tmp')
            except:
                pass
        #------ convert docx files to pdf ------#
        print('-----| Converting docx to pdf |-----')
        for f in joined_paths:
            if (f.split('.')[-1].lower().strip() == 'docx'):
                import time
                try:
                    if not os.path.exists('tmp'):
                        os.makedirs('tmp')
                    Popen(['/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to pdf --outdir tmp '+f], shell=True, stdin=PIPE)
                    time.sleep(20)
                    try:
                        move(os.path.join('tmp',os.path.basename(f).split('.')[0]+'.pdf'),os.path.join(os.path.dirname(f),os.path.basename(f).split('.')[0]+'.pdf'))
                    except Exception as e:
                        print(f'Move Error: {e}')
                except:
                    pass
            try:
                rmtree('tmp')
            except:
                   pass








    