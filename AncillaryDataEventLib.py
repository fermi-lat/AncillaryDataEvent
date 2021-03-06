# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AncillaryDataEvent/AncillaryDataEventLib.py,v 1.1 2008/08/15 21:42:33 ecephas Exp $
def generate(env, **kw):
    if not kw.get('depsOnly', 0):
        env.Tool('addLibrary', library = ['AncillaryDataEvent'])
        if env['PLATFORM'] == "win32" and env.get('CONTAINERNAME','') == 'GlastRelease':
            env.Tool('findPkgPath', package = 'AncillaryDataEvent') 
            env.Tool('findPkgPath',package='AncillaryDataUtil') 
            env.Tool('findPkgPath', package = 'AdfEvent') 
    if kw.get('incsOnly', 0) == 1: 
        env.Tool('findPkgPath', package = 'AdfEvent')         
        env.Tool('findPkgPath', package = 'AncillaryDataUtil') 


def exists(env):
    return 1;
