package org.apache.archiva.redback.integration.filter.authentication.digest;

/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * Digest
 *
 * @author <a href="mailto:joakim@erdfelt.com">Joakim Erdfelt</a>
 *
 */
public class Digest
{
    public static String md5Hex( String data )
    {
        MessageDigest digest = getDigest( "MD5" );
        return Hex.encode( digest.digest( data.getBytes() ) );
    }

    public static MessageDigest getDigest( String algorithm )
    {
        try
        {
            return MessageDigest.getInstance( algorithm );
        }
        catch ( NoSuchAlgorithmException e )
        {
            throw new RuntimeException( "Error initializing MessageDigest: " + e.getMessage(), e );
        }
    }
}