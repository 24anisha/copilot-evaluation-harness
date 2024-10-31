/*
 * Copyright 2016 SerNet Service Network GmbH.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package de.sernet.fluke.rest.security;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

/**
 * Spring security configuration. See:
 * http://ryanjbaxter.com/2015/01/06/securing-rest-apis-with-spring-boot/
 *
 * @author Daniel Murygin
 */
@EnableWebSecurity
@Configuration
class WebSecurityConfiguration extends WebSecurityConfigurerAdapter {

    final private String[] UNSECURED_RESOURCES = {
        "/service/account/create/**"
    };
    
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests().antMatchers(UNSECURED_RESOURCES).permitAll();
        http.authorizeRequests().anyRequest().fullyAuthenticated().and().
                httpBasic().and().
                csrf().disable();
    }
}