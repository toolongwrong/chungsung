package jsp_server;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLDecoder;
import java.net.URLEncoder;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class do_anything
 */
@WebServlet("/do_anything")
public class do_anything extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public do_anything() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doPost(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		int korean, math, eng, avg;
		String name;

	
		
		response.setContentType("text/html; charset=UTF-8");
		
		PrintWriter out = response.getWriter();
		
		korean= Integer.parseInt(request.getParameter("korean"));
		math= Integer.parseInt(request.getParameter("math"));
		eng= Integer.parseInt(request.getParameter("eng"));
		
		//request.setCharacterEncoding("UTF-8");
		//name=request.getParameter("name");
		name = new String(request.getParameter("name").getBytes("ISO-8859-1"), "UTF-8");

	
		avg= (korean+math+eng)/3;
		
		out.println("<HTML>");
		out.println("<HEAD><title>입력 결과</title></head>");
		out.println("<body>");
		out.println("<hr>");
		out.println(name + "학생의 성적은");
		out.println("<br>");
		out.println("국어 " + korean + "점, 수학 "+math+ "점, 영어 " + eng +"점이며");
		out.println("<br>");
		out.println("평균은 "+ avg +"점입니다.");
		out.println("</body></html>");
	}
}
