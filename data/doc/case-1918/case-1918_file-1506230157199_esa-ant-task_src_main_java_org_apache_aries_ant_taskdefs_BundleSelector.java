/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package org.apache.aries.ant.taskdefs;

import java.io.File;
import java.util.jar.JarFile;
import java.util.jar.Manifest;

import org.apache.tools.ant.BuildException;
import org.apache.tools.ant.types.selectors.FileSelector;

/**
 * A simple Ant {@link FileSelector} that can be used to filter out valid OSGi
 * bundles
 * 
 * @version $Id: $
 */
public class BundleSelector implements FileSelector {

	@Override
	public boolean isSelected(File basedir, String filename, File file)
		throws BuildException {

		boolean isValid = false;

		if (file.isFile()) {

			isValid =
				(filename.toLowerCase().endsWith(".esa") || filename.toLowerCase().endsWith(".jar") );

			JarFile osgiBundle = null;

			try {

				osgiBundle = new JarFile(new File(basedir, filename));

				if(osgiBundle!=null){
					Manifest manifest = osgiBundle.getManifest();
					isValid = isValid && manifest != null;
				}
				

			}
			catch (Exception e) {
				// nothing to do
				isValid = false;
			}
			finally {
				try {
					
					if(osgiBundle!=null){
						osgiBundle.close();
					}
				}
				catch (Exception e) {
					// nothing to do
				}
			}
		}

		return isValid;
	}

}