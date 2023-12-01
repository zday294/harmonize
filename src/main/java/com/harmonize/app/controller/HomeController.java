package com.harmonize.app.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HomeController {

    // create basic controller for home page
    @RequestMapping(value = "/")
    public String home() {
        return "home";
    }
    
}
