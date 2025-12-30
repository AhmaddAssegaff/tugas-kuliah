import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Board here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public abstract class Board extends Actor {
    /**
     * Act - do whatever the Board wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    private static final int FONT_SIZE = 25;
    protected static final Color TEXT_COLOR = Color.WHITE;
    
    protected void drawBoard(String text) {
        GreenfootImage img = new GreenfootImage(
            text,
            FONT_SIZE,
            TEXT_COLOR,
            new Color(0, 0, 0, 0)
        );
        setImage(img);
    }
    
    protected void updateBoardText(String label, int value) {
        drawBoard(label + ": " + value);
    }
}
