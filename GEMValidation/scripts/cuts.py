from ROOT import *

#_______________________________________________________________________________
def AND(cut1,cut2):
    return TCut("(%s) && (%s)"%(cut1.GetTitle(),cut2.GetTitle()))

#_______________________________________________________________________________
def OR(cut1,cut2):
    return TCut("(%s) || (%s)"%(cut1.GetTitle(),cut2.GetTitle()))


#_______________________________________________________________________________
rm1 = TCut("region==-1")
rp1 = TCut("region==1")
l1 = TCut("layer==1")
l2 = TCut("layer==2")

eta_min = 1.64
eta_max = 2.12

ok_eta_min = TCut("TMath::Abs(eta) > %f"%(eta_min))
ok_eta_max = TCut("TMath::Abs(eta) < %f"%(eta_max))
ok_eta = AND(ok_eta_min,ok_eta_max)
ok_gL1sh = TCut("gem_sh_layer1 > 0")
ok_gL2sh = TCut("gem_sh_layer2 > 0")
ok_gL1dg = TCut("gem_dg_layer1 > 0")
ok_gL2dg = TCut("gem_dg_layer2 > 0")
ok_gL1pad = TCut("gem_pad_layer1 > 0")
ok_gL2pad = TCut("gem_pad_layer2 > 0")
ok_gL1rh = TCut("gem_rh_layer1 > 0")
ok_gL2rh = TCut("gem_rh_layer2 > 0")

ok_trk_gL1sh = TCut("has_gem_sh_l1 > 0")
ok_trk_gL2sh = TCut("has_gem_sh_l2 > 0")

ok_trk_gL1dg = TCut("has_gem_dg_l1 > 0")
ok_trk_gL2dg = TCut("has_gem_dg_l2 > 0")

ok_lx_odd =  TCut("TMath::Abs(TMath::ASin(gem_lx_odd/gem_trk_rho)) < 5*TMath::Pi()/180.")
ok_lx_even = TCut("TMath::Abs(TMath::ASin(gem_lx_even/gem_trk_rho)) < 5*TMath::Pi()/180.")
