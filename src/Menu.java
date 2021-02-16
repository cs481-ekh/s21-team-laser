import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;

public class Menu {

	private JMenuBar menuBar; 
	private JMenu menu1, menu2, menu3;
	private JMenuItem mItem1, mItem2, mItem3, mItem4, mItem5, mItem6;  
	private int tabCount = 0; 
 
	
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
				FileNameExtensionFilter filter = new FileNameExtensionFilter(
						"JPG & GIF Images", "jpg", "gif");
				chooser.setFileFilter(filter);
				chooser.showOpenDialog(chooserFrame);  
				File chosenFle = chooser.getSelectedFile();
			}
		});
	}
	
	private void createNewTab() {	
		JPanel panel = new JPanel(); 
		tabCount ++; 
		GUI.tab.retTabbedPane().add("Tab " + tabCount, panel);
	}
	
	public JMenuBar retMenu() {
		return menuBar;
	}

	
	
}
