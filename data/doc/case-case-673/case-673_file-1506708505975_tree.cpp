/*
 * Author: hasseo
 * COP3530 Project #3
 * Due Date: Friday March 15, 2013
 * ----
 * This project does some crazy stuff with XML and something about slime molds...
 * ----
 * tree.cpp WAS CREATED IN VERSION 1.1.
 * tree.cpp WAS LAST UPDATED IN VERSION 1.1.
 */
 

#include "tree.h"
#include "node.h"
#include <vector>
#include <string>
#include <stdio.h>
#include <string.h>

using namespace std;

tree::tree(node* root){
	this->root = root;
}

void tree::addNode(node* node){
	nodeVector.push_back(node);
}
node* tree::search(const char* searchTerm){
	for(int i = 0; i < nodeVector.size(); i++){
		if(strcmp(nodeVector[i]->scientific_name, searchTerm) == 0 || strcmp(nodeVector[i]->common_name, searchTerm) == 0){
			return nodeVector[i];
		}
	}
}