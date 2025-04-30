package com.amplifino.nestor.security.http;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import java.util.Optional;

import javax.servlet.http.HttpServletRequest;
import javax.xml.bind.DatatypeConverter;

import org.osgi.service.useradmin.User;
import org.osgi.service.useradmin.UserAdmin;

class BasicAuthentication extends UserAdminHttpAuthentication {
	
	BasicAuthentication(String realm, UserAdmin userAdmin) {
		super(realm, userAdmin);
	}
	
	@Override
	Optional<User> getUser(HttpServletRequest request, String in) {
		String[] userAndPass = new String(Base64.getDecoder().decode(in)).split(":");
		return getUser(userAndPass[0], user -> user.hasCredential("HA1" , ha1(userAndPass[0] , userAndPass[1])));	
	}
	
	private String ha1(String authenticationName, String password) {
		try {
			MessageDigest messageDigest = MessageDigest.getInstance("MD5");
			messageDigest.update(authenticationName.getBytes());
			messageDigest.update(":".getBytes());
			messageDigest.update(realm().getBytes());
			messageDigest.update(":".getBytes());
			messageDigest.update(password.getBytes());
			byte[] md5 = messageDigest.digest();
			return DatatypeConverter.printHexBinary(md5).toLowerCase();
		} catch (NoSuchAlgorithmException e) {
			throw new RuntimeException(e);
		}
  	}

	@Override
	String authorizationMethod() {
		return "Basic";
	}

	@Override
	String challenge() {
		return "";
	}
    
}