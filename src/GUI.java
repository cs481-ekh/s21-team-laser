import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener; 

public class GUI {
	
	static JFrame frame; 
	final int FRAME_SIZE_HEIGHT = 800; 
	final int FRAME_SIZE_WIDTH = 1700; 
	static Menu menu; 
	static Tab tab; 

	public GUI() {
		frame = new JFrame("Laser Noise Analysis Application"); 
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(FRAME_SIZE_WIDTH, FRAME_SIZE_HEIGHT); 

		this.addMenu();
		this.addTab();

		frame.setVisible(true);
	}

	private void addMenu() {
		menu = new Menu(); 
		frame.setJMenuBar(menu.retMenu());
	}
	
	private void addTab() {
		tab = new Tab(); 
		frame.add(tab.retTabbedPane());
	}
	
	/*public static void main(String[] args) {
		new GUI(); 
	}*/


}
