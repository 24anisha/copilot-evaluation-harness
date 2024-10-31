package com.biblio.security;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.oauth2.config.annotation.web.configuration.EnableResourceServer;
import org.springframework.security.oauth2.config.annotation.web.configuration.ResourceServerConfigurerAdapter;

@Configuration
@EnableResourceServer
public class OAuth2ResourceServerConfig extends ResourceServerConfigurerAdapter {

    @Override
    public void configure(HttpSecurity http) throws Exception {
        http
                .csrf().disable()
                .authorizeRequests()
                .antMatchers("/").permitAll()
                .antMatchers("/api/register/**").hasRole("ADMIN")
                .antMatchers("/hello/**").hasRole("ADMIN")
                .antMatchers("/user/**").hasRole("ADMIN")
                .antMatchers("/logout2/**").hasRole("ADMIN")
               
                .anyRequest().authenticated();
    }
}