# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AncillaryDataEvent/SConscript,v 1.6 2009/11/06 01:49:38 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataEvent-01-04-02
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

AncillaryDataEvent = libEnv.StaticLibrary('AncillaryDataEvent',
                                          listFiles(['src/*.cxx']))

progEnv.Tool('AncillaryDataEventLib')
test_AncillaryDataEvent = progEnv.Program('test_AncillaryDataEvent',
                                          [ 'src/test/testMain.cxx'])

progEnv.Tool('registerTargets', package = 'AncillaryDataEvent',
             staticLibraryCxts = [[AncillaryDataEvent, libEnv]],
             testAppCxts = [[test_AncillaryDataEvent, progEnv]],
             includes = listFiles(['AncillaryDataEvent/*.h']))




