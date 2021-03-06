#
# demo ds ChRIS plugin app
#
# (c) 2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp
import numpy as np
from PIL import Image

Gstr_title = """
     _                      
    | |                     
  __| | ___ _ __ ___   ___  
 / _` |/ _ \ '_ ` _ \ / _ \ 
| (_| |  __/ | | | | | (_) |
 \__,_|\___|_| |_| |_|\___/ 
                            
                            
"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       demo.py 

    SYNOPSIS

        python demo.py                                         \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-demo demo                        \
                /incoming /outgoing

    DESCRIPTION

        `demo.py` ...

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 
"""


class Demo(ChrisApp):
    """
    demo
    """
    PACKAGE                 = __package__
    TITLE                   = 'demo app'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = '' # url of an icon image
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        
        Random:
                self.add_argument('--imagefile',
        	dest		= 'imagefile',
        	type		= str,
        	optional	= False,
        	help		= 'Name of Image File')
        """
        self.add_argument('--inputfile',
        	dest	= 'inputfile',
        	type	= str,
        	optional	= False,
        	help = 'input file')

	
             
    def run(self, options):
        """
        Define the code to be run by this plugin app.
        
        Just random stuff:
        im = Image.open('{}/'+(options.imagefile).format(options.inputdir))
         file.writelines('hello\n')
        """
        
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        
        arr = np.array([])
        
        with open(f"{options.inputdir}/{options.inputfile}") as file:
        	for each in file:
        		each = each.rstrip("\n")
        		each = int(each)
        		arr = np.append(arr,each)
        file.close()
        
        arr = np.sort(arr)
        print(arr)
        
        file = open('{}/sorted.txt'.format(options.outputdir),'w')
        file.write('Ran Successfully \n')
        np.savetxt(file,arr,fmt ='% 4d')
        

       
        file.flush()
        file.close()
        
        print('Sorted')        

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_title)
        print(Gstr_synopsis)
