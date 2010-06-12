# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/AncillaryDataEvent/SConscript,v 1.7 2010/06/11 00:32:27 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataEvent-01-04-03
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




