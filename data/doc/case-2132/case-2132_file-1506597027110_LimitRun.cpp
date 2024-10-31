//
// Created by Arnav Gupta on 12/09/16.
//

#include <cstdio>
#include <cstring>
#include <getopt.h>
#include <cerrno>
#include "libLimitRun.h"


#ifdef LOG_DEBUG
static bool DEBUG = true;
#else //LOG_DEBUG
static bool DEBUG = false;
#endif //LOG_DEBUG

using namespace std;
int main (int argc, char **argv) {
    int opt;
    string progToRun;
    rlim_t tLimit, mLimit;

    while ((opt = getopt (argc, argv, "t:m:f:")) != -1) {
        switch (opt) {
            case 't':
                tLimit = stoi(optarg);
                if (DEBUG) fprintf(stdout, "\nCPU Time limit :\t %d s", tLimit);
                break;
            case 'm':
                mLimit = stoi(optarg);
                if (DEBUG) fprintf(stdout, "\nAddress Space limit :\t %d bytes", mLimit);
                break;
            case 'f':
                progToRun = optarg;
                if (DEBUG) fprintf(stdout, "\nFile to execute :\t %s", optarg);

                break;
        }
    }
    if (strlen(progToRun.c_str()) == 0) {
        fprintf(stderr, "\nPlease enter name of program to run with -f argument\n");
        return EINVAL;
    }
    setLimitAndRun(progToRun, tLimit, mLimit);
}