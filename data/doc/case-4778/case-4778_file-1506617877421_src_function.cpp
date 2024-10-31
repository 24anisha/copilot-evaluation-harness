#include "function.h"

	int Collision (int& n){
		for (int i=0; i<H; i++)
		for (int j=0; j<W ; j++){
			if (TileMap[i][j]=='r'){
				n = n-1;
				TileMap[i][j] = '1';
				if (n==0) return 7;
	    }
			if (TileMap[i][j]=='Z')TileMap[i][j]='2';
			if (TileMap[i][j]=='q'){
				return 5;
				break;
			}
		}
	}