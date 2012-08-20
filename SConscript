# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/AncillaryDataEvent/SConscript,v 1.10 2012/08/18 00:17:12 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataEvent-01-05-00
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('addLinkDeps', package = 'AncillaryDataEvent', toBuild='static')
AncillaryDataEvent = libEnv.StaticLibrary('AncillaryDataEvent',
                                          listFiles(['src/*.cxx']))

progEnv.Tool('AncillaryDataEventLib')
test_AncillaryDataEvent = progEnv.Program('test_AncillaryDataEvent',
                                          [ 'src/test/testMain.cxx'])

progEnv.Tool('registerTargets', package = 'AncillaryDataEvent',
             staticLibraryCxts = [[AncillaryDataEvent, libEnv]],
             testAppCxts = [[test_AncillaryDataEvent, progEnv]],
             includes = listFiles(['AncillaryDataEvent/*.h']))




