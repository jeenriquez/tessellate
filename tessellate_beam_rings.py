#! /usr/bin/env python
'''
This script outpust a list of RA and DEC locations for concentric rings around a central source.
'''

import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord
from argparse import ArgumentParser


def cal_first_ring(coords,BW=9.):
    #Calculate beam positions for first ring (B)

    Beam_B1 = SkyCoord(ra= coords.ra + 0., dec= coords.dec + BW)
    Beam_B2 = SkyCoord(ra= coords.ra + BW*(np.sqrt(3)/2.), dec= coords.dec + BW*(1/2.))
    Beam_B3 = SkyCoord(ra= coords.ra + BW*(np.sqrt(3)/2.), dec= coords.dec + BW*(-1/2.))
    Beam_B4 = SkyCoord(ra= coords.ra + 0., dec= coords.dec + BW*(-1))
    Beam_B5 = SkyCoord(ra= coords.ra + BW*(-1*np.sqrt(3)/2.), dec= coords.dec + BW*(-1/2.))
    Beam_B6 = SkyCoord(ra= coords.ra + BW*(-1*np.sqrt(3)/2.), dec= coords.dec + BW*(1/2.))

    first_ring = [Beam_B1,Beam_B2,Beam_B3,Beam_B4,Beam_B5,Beam_B6]

    return first_ring

def cal_second_ring(coords,BW=9.):
    #Calculate  beam positions for second ring (C)

    Beam_C1 = SkyCoord(ra= coords.ra + 0., dec= coords.dec + BW*2)
    Beam_C2 = SkyCoord(ra= coords.ra + BW*(np.sqrt(3)/2.), dec= coords.dec + BW*(3/2.))
    Beam_C3 = SkyCoord(ra= coords.ra + BW*(np.sqrt(3)), dec= coords.dec + BW)

    Beam_C4 = SkyCoord(ra= coords.ra + BW*(np.sqrt(3)), dec= coords.dec + 0.)
    Beam_C5 = SkyCoord(ra= coords.ra + BW*(np.sqrt(3)), dec= coords.dec + BW*(-1))
    Beam_C6 = SkyCoord(ra= coords.ra + BW*(np.sqrt(3)/2.), dec= coords.dec + BW*(-3/2.))

    Beam_C7 = SkyCoord(ra= coords.ra + 0., dec= coords.dec + BW*(-2.))
    Beam_C8 = SkyCoord(ra= coords.ra + BW*(-1*np.sqrt(3)/2.), dec= coords.dec + BW*(-3/2.))
    Beam_C9 = SkyCoord(ra= coords.ra + BW*(-1*np.sqrt(3)), dec= coords.dec + BW*(-1))

    Beam_C10 = SkyCoord(ra= coords.ra + BW*(-1*np.sqrt(3)), dec= coords.dec + 0.)
    Beam_C11 = SkyCoord(ra= coords.ra + BW*(-1*np.sqrt(3)), dec= coords.dec + BW)
    Beam_C12 = SkyCoord(ra= coords.ra + BW*(-1*np.sqrt(3)/2.), dec= coords.dec + BW*(3/2.))

    second_ring = [Beam_C1,Beam_C2,Beam_C3,Beam_C4,Beam_C5,Beam_C6,Beam_C7,Beam_C8,Beam_C9,Beam_C10,Beam_C11,Beam_C12]

    return second_ring


def format_skycoord_lsit(skycoord_list,name_root='',name_only=False):

    skycoord_list = [ fomat_skycoord_str(beam.ra.to_string(u.hour))+' '+fomat_skycoord_str(beam.dec.to_string()) for beam in  skycoord_list]

    if name_root:
        skycoord_list = [ name_root+str(i+1) +'    '+ beam     for i,beam in  enumerate(skycoord_list)]

    if name_only:

        skycoord_list = [ "'"+name_root+str(i+1) +"'," for i in  range(len(skycoord_list))]
    return skycoord_list


def fomat_skycoord_str(skycoord_str):

    skycoord_str = str(skycoord_str)
    skycoord_str = skycoord_str.replace('s','').replace('h',':').replace('m',':').replace('d',':')

    return skycoord_str



def tessellate_rings(beam_size = 9., source = 'SagA*', outher_ring = False):


    #GC_coords = ["17:45:40.0409 -29:00:28.118"]
    #center_skycoords = SkyCoord(GC_coords, ICRS, unit=(u.deg, u.hourangle))
    center_skycoords = SkyCoord.from_name(source)

    if source == 'SagA*':
        source_name = 'Galactic_Center'
    else:
        source_name = source

    print source_name +'    '+ fomat_skycoord_str(center_skycoords.ra.to_string(u.hour))+' '+fomat_skycoord_str(center_skycoords.dec.to_string())

    #Beamwidth
    # 9' for Lband
    BW = beam_size*u.arcminute

    #Calculate first ring
    first_ring = cal_first_ring(center_skycoords,BW=BW)
    first_ring = format_skycoord_lsit(first_ring,name_root=source_name+'_B')
    print '\n'.join(first_ring)

    if outher_ring:
        #Calculate second ring
        second_ring = cal_second_ring(center_skycoords,BW=BW)
        second_ring = format_skycoord_lsit(second_ring,name_root=source_name+'_C')
        print '\n'.join(second_ring)


def main():
    """ Command line tool for using tesselate. """

    parser = ArgumentParser(description="Tessellates beam positions around a central RA and DEC in one or two concentric rings.")
    #parser.add_argument('filename', type=str, help='Name of file to read')

    parser.add_argument('-b', action='store',  default=9., dest='beam_size', type=float,
                        help="Beam size in arcminutes. Default = 9' (L-band GBT).")
    parser.add_argument('-s', action='store',  default='SagA*', dest='source', type=str,
                        help="Source name. Default: SagA* (can use any source name available in astropy.SkyCoord).")
    parser.add_argument('-o', action='store', default=False, dest='outher_ring',
                       help='Calculates the outher ring. Default:False')
#    parser.add_argument('-b', action='store', default=None, dest='f_start', type=float,
#                        help='')
    parse_args = parser.parse_args()

    #Initialize
    beam_size = parse_args.beam_size
    source = parse_args.source
    outher_ring = parse_args.outher_ring


    tessellate_rings(beam_size = beam_size, source = source, outher_ring = outher_ring)

if __name__ == "__main__":
    main()


