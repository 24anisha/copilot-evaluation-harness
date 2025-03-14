/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.    
 */

package org.apache.wink.json4j.internal;

import org.apache.wink.json4j.JSONString;

/**
 * An simple class provided for API compatibility to other JSON models that 'represents' 
 * 'null' in an actual object.
 */
public class Null implements JSONString {

    /**
     * Equals function that returns true for comparisons to null.
     */
    public boolean equals(Object obj) {
        if (obj == null) {
            return true;
        } else {
            return false;
        }
    }

    /**
     * toString method that just returns 'null' as the string.
     */
    public String toString() {
        return "null";

    }

    /**
     * Method to return a JSON compliant representation of this object.
     * @return a JSON formatted string.
     */
    public String toJSONString() {
        return this.toString();
    }

}