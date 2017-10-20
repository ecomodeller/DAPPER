# As in Lorenz 1996 "Predictability..."

from common import *

from mods.LorenzXY.core import model_instance
LXY = model_instance(nX=36,J=10,F=10)
nX = LXY.nX






################
# Full
################

# 
t = Chronology(dt=0.005,dtObs=0.05,T=4**3,BurnIn=6)


f = {
    'm'    : LXY.m,
    'model': with_rk4(LXY.dxdt,autonom=True),
    'noise': 0,
    'jacob': LXY.dfdx,
    'plot' : LXY.plot_state
    }

X0 = GaussRV(C=0.01*eye(LXY.m))

R = 1.0
h = partial_direct_obs_setup(LXY.m,arange(LXY.nX))
h['noise'] = R

other = {'name': rel_path(__file__,'mods/')+'_full'}
setup_full = TwinSetup(f,h,t,X0,**other)


################
# Truncated
################

# Just change dt from 005 to 05
t = Chronology(dt=0.05, dtObs=0.05,T=4**3,BurnIn=6)

f = {
    'm'    : nX,
    'model': with_rk4(LXY.dxdt_parameterized),
    'noise': 0,
    }

X0 = GaussRV(C=0.01*eye(nX))

h = partial_direct_obs_setup(nX,arange(nX))
h['noise'] = R
 
other = {'name': rel_path(__file__,'mods/')+'_trunc'}
setup_trunc = TwinSetup(f,h,t,X0,**other)

####################
# Suggested tuning
####################
#                     # Expected RMSE_a ("U"-vars only!)
