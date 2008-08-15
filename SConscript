# -*- python -*-
# $Header$
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
test_AncillaryDataEvent = progEnv.GaudiProgram('test_AncillaryDataEvent',[[ 'src/test/testMain.cxx']], test = 1)

progEnv.Tool('registerObjects', package = 'AncillaryDataEvent', libraries = [AncillaryDataEvent], testApps = [test_AncillaryDataEvent], includes = listFiles(['AncillaryDataEvent/*.h']))