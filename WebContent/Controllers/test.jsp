<%@page import="core.SubProcess"%>
<%@page import="core.DAOLibrary" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%><%
	SubProcess sp = new SubProcess(new String[] {"pwd"});
    sp.start();
    out.print(sp.getExitValue());
    out.print(sp.getResult());
    
    SubProcess sps = new SubProcess(new String[]{"ls"});
    sps.start();
    out.print(sps.getResult());
    
    /*DAOLibrary ds = new DAOLibrary();
	out.print(ds.search(request.getParameter("search")));*/
%>