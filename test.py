import numpy as np
import matplotlib.pyplot as plt

def mag_pole_dipolu(r_x,r_y,r0_x=0.0,r0_y=.0,m_x=0.0,m_y=1.0):
#
#   funkcia, ktora spocita zlozky B_x a B_y indukcie magnetickeho pola v mieste so suradnicami r_x,r_y
#   vysunutie polohy dipolu je pomocou zloziek vektora r0_x,r0_y
#   vektor momentu magnetickeho diplou ma zlozky m_x, my 
#
    r_x = r_x - r0_x
    r_y = r_y - r0_y
#   vypocet velkosti vzrialenosti miesta r od dipolu
    r = np.sqrt(r_x*r_x + r_y*r_y) 
#   vypocer zloziek podla vztahu na https://en.wikipedia.org/wiki/Magnetic_dipole
    B_x = 3*r_x*(m_x*x + m_y*r_y)/r**5 - m_x/r**3
    B_y = 3*r_y*(m_x*r_x + m_y*r_y)/r**5 - m_y/r**3
    return B_x,B_y

# vytvorenie mriezky bodov, v ktorych sa pocita magneticke pole
x,y = np.meshgrid(np.linspace(-10,10,20),np.linspace(-10,10,20))

# vypocet magnetickeho pola na bodoch mriezky
B_x,B_y = mag_pole_dipolu(x,y)
# vypocet velkosti magnetickeho pola v kazdom bode mriezky
B = np.sqrt(B_x**2 + B_y**2)
# smerovy vektor magnetickeho pola v kazdom bode mriezky 
n_x, n_y  = B_x/B, B_y/B

# vykreslenie magnetickeho pola pomocou matplotlib
plt.quiver(x,y,B_x,B_y,pivot='mid')
plt.show()

# vykreslenie len smerov magentickeho pola a silociar
plt.quiver(x,y,B_x/B,B_y/B,pivot='mid')
plt.streamplot(x,y,n_x,n_y,color="lightgrey")
plt.show()
