import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.lang.ProcessBuilder.Redirect;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;

public class Menu {

	private JMenuBar menuBar; 
	private JMenu menu1, menu2, menu3;
	private JMenuItem mItem1, mItem2, mItem3, mItem4, mItem5, mItem6;  
	private int tabCount = 0; 
	private File chosenFile;
	
	public Menu() {
		menuBar = new JMenuBar(); 
		
		menu1 = new JMenu("File"); 
		menu2 = new JMenu("Menu 2"); 
		menu3 = new JMenu("Menu 3"); 

		menuBar.add(menu1);
		menuBar.add(menu2);
		menuBar.add(menu3);
		
		mItem1 = new JMenuItem("Create a tab");
		mItem2 = new JMenuItem("Open");
		mItem3 = new JMenuItem("Item 3");
		mItem4 = new JMenuItem("Item 4");
		mItem5 = new JMenuItem("Item 5");
		mItem6 = new JMenuItem("Item 6");
		
		menu1.add(mItem1);
		menu1.add(mItem2);
		menu2.add(mItem3);
		menu2.add(mItem4);
		menu3.add(mItem5);
		menu3.add(mItem6);
		
		mItem1.addActionListener (new ActionListener() {
			public void actionPerformed (ActionEvent e) {
				createNewTab();
			}
		});
		mItem2.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				Frame chooserFrame = new JFrame();
				File workingDirectory = new File(System.getProperty("user.dir"));
				JFileChooser chooser = new JFileChooser();
				chooser.setCurrentDirectory(workingDirectory);
				chooser.showOpenDialog(chooserFrame);  
				File chosenFile = chooser.getSelectedFile();
				File script = new File("src\\python_scripts\\analysis_SRTA_BSU.py");
				System.out.println(script.getAbsolutePath() + "\n" + chosenFile.getAbsolutePath());
			
					ProcessBuilder pb = new ProcessBuilder("python", script.getAbsolutePath(), chosenFile.getAbsolutePath());
					Process p;
				try {
					pb.redirectErrorStream(true); // merges err with out
					pb.redirectOutput(Redirect.appendTo(new File("out.txt")));
					p = pb.start();
					p.waitFor();

				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				catch(InterruptedException e1){
					e1.printStackTrace();
				}
					
					System.out.println("Process started");
				
			}
		});
	}
	
	private void createNewTab() {	
		JPanel panel = new JPanel(); 
		tabCount ++; 
		GUI.tab.retTabbedPane().add("Tab " + tabCount, panel);
	}
	
	public void setFile(File file){
		chosenFile = file;
	}

	public File getFile()
	{
		return chosenFile;
	}

	public JMenuBar retMenu() {
		return menuBar;
	}

	
	
}
