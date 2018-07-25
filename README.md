# tessellate
This script outpust a list of RA and DEC locations for one or two concentric rings around a central source.


Example:

From the command line:
```

>>> python tessellate_beam_rings.py -h

usage: tessellate_beam_rings.py [-h] [-b BEAM_SIZE] [-s SOURCE]
                                [-o OUTHER_RING]

Tessellates beam positions around a central RA and DEC in one or two
concentric rings.

optional arguments:
  -h, --help      show this help message and exit
  -b BEAM_SIZE    Beam size in arcminutes. Default = 9' (L-band GBT).
  -s SOURCE       Source name. Default: SagA* (can use any source name
                  available in astropy.SkyCoord).
  -o OUTHER_RING  Calculates the outher ring. Default:False


>> python tessellate_beam_rings.py -s Pollux

Pollux    7:45:18.9499 28:01:34.316
Pollux_B1    7:45:18.9499 28:10:34.316
Pollux_B2    7:45:50.1268 28:06:04.316
Pollux_B3    7:45:50.1268 27:57:04.316
Pollux_B4    7:45:18.9499 27:52:34.316
Pollux_B5    7:44:47.773 27:57:04.316
Pollux_B6    7:44:47.773 28:06:04.316
```
