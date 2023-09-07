# Rafo DDVCS tests



## Edit locations:

Change lines 28 and 29 of RunChain.py, and line 56 of AnaDDVCSOSG.cc  

## Compile

```
module load clas12
./compile_AnaDDVCSOSG.sh
```


## Run the chain:

### comparison between versions

`python3.9 RunChain.py 303 "gemc 4.4.2 no vertex no bg" 307 "gemc 5.4 no vertex no bg " 309 "gemc 5.4  no vertex bg"`


### comparison same version, vertex, bg

`python3.9 RunChain.py 303 gemc 5.4 no vertex no bg " 309 "gemc 5.4  no vertex bg"  308 "gemc 5.4 standard vertex bg"` 




## Results

Figures rp_MC_Memep2.pdf(png, root) and rp_MC_Memep2_OldSW.pdf(png, root) are variables from MC::Particle bank, regardless of the GEMC and SW version,
the ratio should always be consistent with 1. Those plots are just to make sure normalization to the number of processed events is done properly.