import ROOT
import os

# Package macro path
packagePath = os.path.dirname(os.path.realpath(__file__))
ROOT.gROOT.SetMacroPath(ROOT.gROOT.GetMacroPath() + os.path.join(packagePath, 'macro') + ':')

from CMSlumi import CMSlumi
ROOT.CMSlumi = CMSlumi
ROOT.gROOT.ProcessLineSync(".L CMS_lumi.C")
