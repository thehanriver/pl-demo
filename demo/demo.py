#
# demo ds ChRIS plugin app
#
# (c) 2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os
import sys

from .inference import Inference

# import the Chris app superclass
from chrisapp.base import ChrisApp
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
    TITLE                   = 'COVID-Net inference for chest x-ray'
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
        self.add_argument('--parInst',
        	dest = 'parInst',
        	type = str,
        	optional = False,
        	help = 'Parent instance ID',
        	)
        	
        self.add_argument('--metaname', 
                    dest         = 'metaname', 
                    type         = str, 
                    optional     = True,
                    help         = 'Name of ckpt meta file',
                    default      = 'model.meta')
        self.add_argument('--imagefile', 
                    dest         = 'imagefile', 
                    type         = str, 
                    optional     = False,
                    help         = 'Name of image file to infer from')
        self.add_argument('--in_tensorname', 
                    dest         = 'in_tensorname', 
                    type         = str, 
                    optional     = True,
                    help         = 'Name of input tensor to graph',
                    default      = 'input_1:0')
        self.add_argument('--out_tensorname', 
                    dest         = 'out_tensorname', 
                    type         = str, 
                    optional     = True,
                    help         = 'Name of output tensor from graph',
                    default      = 'norm_dense_1/Softmax:0')
        self.add_argument('--input_size', 
                    dest         = 'input_size', 
                    type         = int, 
                    optional     = True,
                    help         = 'Size of input (ex: if 480x480, --input_size 480)',
                    default      = 480)
        self.add_argument('--top_percent', 
                    dest         = 'top_percent', 
                    type         = float, 
                    optional     = True,
                    help         = 'Percent top crop from top of image',
                    default      = 0.08)
                    
	
             
    def run(self, options):
        """
        Define the code to be run by this plugin app.
        
        Just random stuff:
        im = Image.open('{}/'+(options.imagefile).format(options.inputdir))
         file.writelines('hello\n')
        """
        
       # python covidnet.py inputimage output --imagefile ex-covid.jpeg
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        all_three_models = [
            # {
            #     'weightspath':'/models/COVIDNet-CXR3-A',
            #     'ckptname':'model-2856',
            #     'modelused':'modelA'
            # }, 
            {
                'weightspath':'/usr/local/lib/covidnet/COVIDNet-CXR4-B',
                'ckptname':'model-1545',
                'modelused':'modelB'
            },
            # {
            #     'weightspath': '/models/COVIDNet-CXR3-C',
            #     'ckptname':'model-0',
            #     'modelused':'modelC'
            # }
        ]
        for model in all_three_models:
            options.weightspath =model['weightspath']
            options.ckptname = model['ckptname']
            options.modelused = model['modelused']
            infer_obj = Inference(options)
            infer_obj.infer()
    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_title)
        print(Gstr_synopsis)

# chris app needs to write to files as outputs and taking inputs
# output a dicom image then ChRIS user interface will be able to show it
# csv, json, or custom html css files
