include ../../Makefile.defs

TESTNAME     = targetid-multi-image
TESTSRC_MAIN = targetid-multi-image.c
TESTSRC_AUX  =
TESTSRC_ALL  = $(TESTSRC_MAIN) $(TESTSRC_AUX)

OMP_FLAGS    = -fopenmp -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx90a:xnack- -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx90a:xnack+
CLANG        = clang
OMP_BIN      = $(AOMP)/bin/$(CLANG)
CC           = $(OMP_BIN) $(VERBOSE)
#-ccc-print-phases
#"-\#\#\#"

include ../Makefile.rules
run: $(TESTNAME)
	HSA_XNACK=1 ./$(TESTNAME)
# 	will pass only on machines where xnack+ is configured

	HSA_XNACK=0 ./$(TESTNAME)
	strings $(TESTNAME) |grep -i gfx
