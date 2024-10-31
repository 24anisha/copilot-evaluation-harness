/**
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
package org.apache.xbean.command;

import java.io.FileInputStream;
import java.io.InputStream;
import java.io.PrintStream;

/**
 * @author <a href="mailto:david.blevins@visi.com">David Blevins</a>
 */
public class Test implements Command {
    
    public static void _DONT_register() {
        CommandRegistry.register("test", Test.class);
    }

    public int main(String[] args, InputStream in, PrintStream out) {
        try {
            InputStream file = new FileInputStream("print.txt");
            int b = file.read();
            while (b != -1) {
                out.write(b);
                b = file.read();
            }
        } catch (Exception e) {
            e.printStackTrace();
            return -1;
        }
        return 0;
    }
}