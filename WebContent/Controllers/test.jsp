<%@page import="core.SubProcess"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%><%
    
   SubProcess sp = new SubProcess(new String[] {"ls","-1"});
   sp.start();
    out.print(sp.getExitValue());
    out.print(sp.getResult());
    
    %>