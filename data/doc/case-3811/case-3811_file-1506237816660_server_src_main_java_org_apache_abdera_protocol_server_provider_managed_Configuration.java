/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  The ASF licenses this file to You
 * under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.  For additional information regarding
 * copyright in this work, please see the NOTICE file in the top level
 * directory of this distribution.
 */
package org.apache.abdera.protocol.server.provider.managed;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public abstract class Configuration {

    static Properties loadFileAsProperties(String fileLocation) throws IOException {
        Properties props = new Properties();
        props.load(new FileInputStream(fileLocation));
        return props;
    }

    static InputStream loadFileAsInputStream(String fileLocation) throws IOException {
        return Thread.currentThread().getContextClassLoader().getResourceAsStream(fileLocation);
    }

    static String getProperty(Properties prop, String key) {
        String val = prop.getProperty(key);
        if (val == null)
            throw new RuntimeException();
        return val;
    }

    protected Configuration() {
    }
}