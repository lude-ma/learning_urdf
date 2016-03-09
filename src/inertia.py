from __future__ import division
from numpy import pi


DENSITY = 2.7e3  # density of aluminum [kg/m^3]


def cuboid(x, y, z):
    vol = x*y*z
    mass = DENSITY*vol
    Ix = mass/12*(y**2 + z**2)
    Iy = mass/12*(x**2 + z**2)
    Iz = mass/12*(x**2 + y**2)
    return mass, (Ix, Iy, Iz)


def cube(x):
    return cuboid(x=x, y=x, z=x)


def rod(r, z):
    vol = pi*r**2*z
    mass = DENSITY*vol
    Ix = mass/12*(3*r**2 + z**2)
    # Iy = Ix
    Iz = .5*mass*r**2
    return mass, (Ix, Ix, Iz)


def sphere(r):
    vol = 4/3*pi*r**3
    mass = DENSITY*vol
    Ix = 2*mass*r**2/5
    # Iy = Ix
    # Iz = Ix
    return mass, (Ix, Ix, Ix)


def hemisphere(r):
    mass, I = sphere(r=r)
    return mass/2, (I[0]/2, I[1]/2, I[2]/2)


if __name__ == '__main__':
    parts = ['body', 'leg', 'foot', 'wheel', 'head', 'pole', 'eye']
    geomtrs = [rod(r=.2, z=.6), cuboid(x=.6, y=.2, z=.1),
               cuboid(x=.1, y=.4, z=.1), rod(r=.035, z=.1), hemisphere(r=.2),
               rod(r=.02, z=.3), cube(x=.08)]

    for name, mI in zip(parts, geomtrs):
        m, I = mI
        print "{0}\t{1}kg\t{2}kgm^2".format(name, m, I)
