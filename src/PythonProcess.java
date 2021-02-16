import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class PythonProcess {
    private String s;
    private Process p;
    public PythonProcess(File analysis, File data) {        
        try {
            ProcessBuilder pb = new ProcessBuilder("python", analysis.getAbsolutePath(), data.getAbsolutePath());
            p = pb.start();
            p.waitFor();
            System.out.println("Process started");
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    public Process getProcess(){
        return p;
    }
}