import argparse
import shlex
import logging

logger = logging.getLogger(__name__)
from pyuvvis.logger import logclass

SCRIPTNAME = 'specreport'
SEP_DEFAULT = '/'

@logclass(log_name=__name__, public_lvl='debug')
def main(args=None):
    
    if args:
        if isinstance(args, basestring):
            args=shlex.split(args)
        sys.argv = args               
    
    
    parser = argparse.ArgumentParser(SCRIPTNAME, description='GWU PyUvVis composite' 
            'latex report assembly script', epilog='Additional help not found', 
            usage='%s <cmd> --globals' % SCRIPTNAME)    
    
    parser.add_argument('-n', '--dryrun',
         help='Not implemented', action='store_true')
    
    parser.add_argument('-v', '--verbosity', help='Set screen logging '
                         'If no argument, defaults to info.', nargs='?',
                         default='warning', const='info', metavar='')    
    parser.add_argument('-s', '--sep', metavar='',
                         help='Latex section separator.  Defaults to %s.  '
                         'Set to None to avoid auto sub-sectioning' %SEP_DEFAULT)

    # Sub Commands
    subparsers = parser.add_subparsers(title='commands', metavar='', dest='op')    
    
    # TEMPLATE SUBCOMMAND
    p_template = subparsers.add_parser('template', help='template help')
    p_template.add_argument('sections', nargs='*', help='List of sections to add.'
        'or tree file.  If not tree file, default section template will be "template/section" '
        'section names will auto-break into subsections based on value of --sep') 
    p_template.add_argument('template_file', default=None) #XXX
    p_template.add_argument('outpath', default='./fooout') #XXX
    
    # BUILD SUBCOMMAND
    p_build = subparsers.add_parser('build', help='Adds latex doc header including ' 
        'begin/close document, title, author etc...')
    p_build.add_argument('bodyfile', help='File generated by p_template.')
    p_build.add_argument('--title', default='Untitled')
    p_build.add_argument('--author', default='Adam Hughes')
    p_build.add_argument('--pdf', type=bool, default=True)
    p_build.add_argument('--clean', action = 'store_true', help='Remove .aux, .log'
        ' and other latex temporary files.')

    # Compile and open
    p_build.add_argument('--compile', type=bool, default=False) #or just store_True?

   # Add to .tex template (%plotsize) [but those are already set... scrap?) 
    p_build.add_argument('--plotsize', default='5', help='plot dimensions in '
                         ' cm.  Defaults to width=5cm.')
    # p_build.add_argument('--view', type=bool, default=False, const='evince')
    
    #SUMMARY SUBCOMMAND (not implemented)
    p_summary = subparsers.add_parser('summary', help='summary help')
    p_summary.add_argument('bodyfile')


    ns = parser.parse_args()
    
    if ns.op == 'template':
        pass
    
    elif ns.op == 'build':
        pass
    
    else:
        raise NotImplemented

    # Subparsers
    # Put options separaetly, then make global later if common.
    # ns=blah balh
    # Report(title=ns.title, etc...)
       # - Let report handle it's own args; however, if arg is "None"
       # in namespace, makesure it's covnerted here.  May be easiest to do
       # on single arg, or to just add in like (for attr in ns, if attr='none')
    # If op=build,
        # report=ns.report()
        # report.make_header()
        # write.report() etc...
    # Elif op.template,
        # report=ns.report()
        # report.write()  
    pass

# REPORT should still track sections and metadata and stuff in dict for more extensiblye
# use later on.

if __name__ == '__main__':
    main()