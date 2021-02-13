import javax.swing.*;

public class Tab {

	private JTabbedPane tabbedPane; 
	
	public Tab() {
		tabbedPane = new JTabbedPane();
	}
	
	public void add(String tabName, JPanel tab) {
		this.add(tabName, tab);
	}

	public JTabbedPane retTabbedPane() {
		return tabbedPane;
	}
}
