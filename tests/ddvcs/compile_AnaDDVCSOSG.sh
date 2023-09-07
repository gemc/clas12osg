g++ AnaDDVCSOSG.cc -o AnaDDVCSOSG.exe -L"$HIPO"/lib -lhipo4 -llz4 -I"$HIPO"/hipo4 \
     -I/group/clas12/users/rafopar/clas12AnaTools/include -L/group/clas12/users/rafopar/clas12AnaTools/lib -lclas12AnaTools \
     "$(root-config --cflags --libs)"
