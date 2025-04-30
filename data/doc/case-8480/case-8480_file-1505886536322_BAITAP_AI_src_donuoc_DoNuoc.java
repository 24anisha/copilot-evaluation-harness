package donuoc;

import javax.swing.JTextArea;


/**
 *
 * @author KJ Mok
 */
public class DoNuoc {
    
    int Vx,Vy,z;
    JTextArea t;

    public DoNuoc(int Vx, int Vy, int z, JTextArea t) {
        this.Vx = Vx;
        this.Vy = Vy;
        this.z = z;
        this.t = t;
    }
    
    private int min(int a, int b)
    {
        return a>b?b:a;
    }
    
    public void dongNuoc()
    {
        int x=0,y=0,k;
        t.append("Chương trình bắt đầu tính toán.\n");
        
        for(int i=1; i <= 500; i++) {        
            if(i==500){
                t.append("\nTrường hợp này không giải được...làm khó tôi quá /(T^T)\\\n");
                break;
            }
            else if((x==z && y==0) || (x==0 && y==z)){
                break;
            }
            else if(x==Vx)
            {
                x=0;
                t.append("\nÁp dụng luật 1: x=" + x + " | y=" + y + ".\n");
            }
            else if(y==0)
            {
                y=Vy;
                t.append("\nÁp dụng luật 2: x=" + x + " | y=" + y + ".\n");
            }
            else if(y>0)
            {
                k=min(Vx-x,y);
                x=x+k;
                y=y-k;
                t.append("\nÁp dụng luật 3: x=" + x + " | y=" + y + ".\n");
            }            
        }
        t.append("\nChương trình kết thúc.");
    }
    
}