package com.ra.controller;

import javax.servlet.http.HttpSession;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import com.ra.domain.Register;
import com.ra.repository.RegisterRepository;



@Controller
public class RegisterController {

	@Autowired
	RegisterRepository registerRepository;
	
	Logger log = LoggerFactory.getLogger(this.getClass());
	
    @RequestMapping(value="/registerform", method=RequestMethod.GET)
    public String customerForm(Model model) {
        model.addAttribute("register", new Register());
        return "registerform";
    }

    @RequestMapping(value="/registerform", method=RequestMethod.POST)
    public String customerSubmit(@ModelAttribute Register register, Model model) {
    	
        model.addAttribute("register", register);
        String info = String.format("Customer Submission: id = %d, firstname = %s, lastname = %s", 
        								register.getId(), register.getUsername(), register.getPassword(),register.getEmail());
        log.info(info);
        registerRepository.save(register);
                
        return "result";
    }
    

    
}