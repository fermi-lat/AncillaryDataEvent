# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/AncillaryDataEvent/SConscript,v 1.8 2010/06/12 17:19:39 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataEvent-01-04-04
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




