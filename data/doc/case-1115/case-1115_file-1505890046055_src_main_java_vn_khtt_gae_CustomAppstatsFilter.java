package vn.khtt.gae;

import com.google.appengine.tools.appstats.AppstatsFilter;

import java.io.IOException;

import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class CustomAppstatsFilter extends AppstatsFilter {
  private static final String DEFAULT_BASE_PATH = "/appstats/";
  private String basePath;

  public CustomAppstatsFilter() {
  }

  @Override
  public void init(FilterConfig config) {
    super.init(config);
    
    String path = config.getInitParameter("basePath");
    if (path == null) {
      basePath = DEFAULT_BASE_PATH;
    } else {
      basePath = path.endsWith("/") ? path : path + "/";
    }
  }

  @Override
  public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws IOException, ServletException {
    HttpServletRequest request = (HttpServletRequest)req;
    HttpServletResponse response = (HttpServletResponse)resp;
    
    String requestURI = request.getRequestURI();
    if (requestURI.startsWith(basePath)){
      chain.doFilter(request, response);
    } else {
      super.doFilter(request, response, chain);
    }
  }
}