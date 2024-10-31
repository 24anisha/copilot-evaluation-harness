/*******************************************************************************
 Copyright 2006-2012 Lukas Käll <lukas.kall@scilifelab.se>

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

 *******************************************************************************/

#include "ProteinScoreHolder.h"

ProteinScoreHolder::ProteinScoreHolder(std::string name, bool isDecoy, ProteinScoreHolder::Peptide peptide,
    int groupId)
	: name_(name), q_(0.0), qemp_(0.0), pep_(0.0), p_(0.0), score_(0.0),
	  isDecoy_(isDecoy), groupId_(groupId), specCountsUnique_(0u), specCountsAll_(0u) {
  if (!peptide.name.empty()) addPeptide(peptide);
}

ProteinScoreHolder::~ProteinScoreHolder() {}
