# Testing ionospheric model NeQuick 2 using satellite measurements of electron density

The methodology for verifying the NeQuick 2 ionospheric model using Swarm satellite data from 2014 is outlined below. The process involves model calculations, error statistics analysis, creation of spatial distribution maps for mean errors, and plotting monthly mean error curves for various geomagnetic conditions and latitudinal zones. To ensure accurate analysis, time periods are classified into geomagnetic storm days and calm days, using Kp and AE indices.

The first script, raw_process.py, performs direct model calculations and generates output files for subsequent analysis in the second script, map.ipynb.
