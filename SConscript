# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AncillaryDataEvent/SConscript,v 1.9 2012/01/23 19:25:40 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataEvent-01-04-04
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




