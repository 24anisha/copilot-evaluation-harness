package com.pasodoff.hcp.badapple.resource;

import com.pasodoff.hcp.badapple.service.CmdService;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;

/**
 * Created by aaron on 19/06/2017.
 */
@RestController
public class NslookupResource {

    CmdService cmdService;

    public NslookupResource(CmdService cmdService) {
        this.cmdService = cmdService;
    }


    @RequestMapping("/nslookup/{address}")
    public String getAddressLookup(@PathVariable(value="address") String address, HttpServletResponse response){
        // TODO: Insecure cookie HttpOnly flag not set
        Cookie cookie = new Cookie("bad-apple-data", address);
        cookie.setPath("/");
        response.addCookie(cookie);
        return cmdService.nslookup(address);
    }
}