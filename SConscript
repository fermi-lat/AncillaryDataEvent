# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AncillaryDataEvent/SConscript,v 1.1 2008/08/15 21:22:39 ecephas Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataEvent-01-04-01
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('AncillaryDataEventLib', depsOnly = 1)
AncillaryDataEvent = libEnv.StaticLibrary('AncillaryDataEvent', listFiles(['src/*.cxx']))

progEnv.Tool('AncillaryDataEventLib')
test_AncillaryDataEvent = progEnv.Program('test_AncillaryDataEvent',[ 'src/test/testMain.cxx'])

progEnv.Tool('registerObjects', package = 'AncillaryDataEvent', libraries = [AncillaryDataEvent], testApps = [test_AncillaryDataEvent], includes = listFiles(['AncillaryDataEvent/*.h']))
