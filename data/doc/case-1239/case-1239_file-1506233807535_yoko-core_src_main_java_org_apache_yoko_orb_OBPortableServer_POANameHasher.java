/*
 *  Licensed to the Apache Software Foundation (ASF) under one or more
*  contributor license agreements.  See the NOTICE file distributed with
*  this work for additional information regarding copyright ownership.
*  The ASF licenses this file to You under the Apache License, Version 2.0
*  (the "License"); you may not use this file except in compliance with
*  the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

package org.apache.yoko.orb.OBPortableServer;

//
// Note: We cannot use String[] as a Hashtable key, because
// different hashcodes are computed for equivalent string arrays.
//
final class POANameHasher {
    private String[] poaId_;

    private int hashCode_;

    POANameHasher(String[] poaId) {
        poaId_ = poaId;
        hashCode_ = ("").hashCode();
        for (int i = 0; i < poaId_.length; i++)
            hashCode_ ^= poaId_[i].hashCode();
    }

    public int hashCode() {
        return hashCode_;
    }

    public boolean equals(java.lang.Object o) {
        POANameHasher k = (POANameHasher) o;

        if (poaId_.length != k.poaId_.length)
            return false;

        for (int i = 0; i < poaId_.length; i++)
            if (!poaId_[i].equals(k.poaId_[i]))
                return false;

        return true;
    }
    
    public String toString() {
        StringBuffer buf = new StringBuffer(); 
        for (int i = 0; i < poaId_.length; i++) {
            buf.append('/'); 
            buf.append(poaId_[i]); 
        }
        return buf.toString(); 
    }
}