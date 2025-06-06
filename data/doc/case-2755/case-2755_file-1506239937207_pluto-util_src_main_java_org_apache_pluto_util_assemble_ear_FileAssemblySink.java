/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.pluto.util.assemble.ear;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Stores assembled bytes in an underlying <code>File</code>.
 */
class FileAssemblySink extends AssemblySink {
    
    private static final Logger LOG = LoggerFactory.getLogger( FileAssemblySink.class );
    private File sink = null;
    
    FileAssemblySink(File file) throws FileNotFoundException {
        super(new FileOutputStream(file));
        this.sink = file;        
    }
    
    public void writeTo(OutputStream out, int buflen) throws IOException {
        byte[] buf = new byte[buflen];
        int read = 0;
        InputStream sinkReader = new BufferedInputStream( 
                new FileInputStream(sink), buflen );
        while ( ( read = sinkReader.read(buf) ) != -1 ) {
            out.write(buf, 0, read);
        }
    }
    
}